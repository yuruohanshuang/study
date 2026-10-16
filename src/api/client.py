import logging
import time

import requests

from src.core import APIError


class APIClient:
    """进阶 API 调用客户端."""

    def __init__(self, base_url, timeout=(3, 10), headers=None, max_retries=2):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update(headers or {"Accept": "application/json"})
        self.logger = logging.getLogger(__name__)

    def set_token(self, token):
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def _build_url(self, path):
        return f"{self.base_url}/{path.lstrip('/')}"

    def _merge_headers(self, headers=None):
        merged = dict(self.session.headers)
        if headers:
            merged.update(headers)
        return merged

    def _handle_response(self, response):
        try:
            response.raise_for_status()
            if not response.text:
                return None
            return response.json()
        except requests.exceptions.HTTPError:
            status = response.status_code
            if status == 404:
                raise APIError(f"资源不存在: {response.url}", status)
            elif status == 401:
                raise APIError("认证失败，请刷新 Token", status)
            elif status == 403:
                raise APIError("无权限访问该资源", status)
            elif 400 <= status < 500:
                raise APIError(f"客户端错误 {status}", status)
            else:
                raise APIError(f"服务端错误 {status}", status)
        except ValueError as e:
            raise APIError("响应不是有效 JSON", response.status_code, str(e))

    def _request(self, method, path, headers=None, **kwargs):
        url = self._build_url(path)
        request_headers = self._merge_headers(headers)
        last_error = None
        start_time = time.time()

        for attempt in range(self.max_retries + 1):
            try:
                self.logger.info(f"{method} {url} 尝试 {attempt + 1}")
                response = self.session.request(
                    method,
                    url,
                    headers=request_headers,
                    timeout=self.timeout,
                    **kwargs,
                )
                elapsed = time.time() - start_time
                self.logger.info(f"{method} {url} {response.status_code} {elapsed:.2f}s")
                return self._handle_response(response)
            except APIError as e:
                if e.status_code and 400 <= e.status_code < 500:
                    elapsed = time.time() - start_time
                    self.logger.error(f"{method} {url} {e.status_code} {elapsed:.2f}s: {e}")
                    raise
                last_error = e
            except requests.exceptions.RequestException as e:
                last_error = e

        elapsed = time.time() - start_time
        self.logger.error(f"{method} {url} 失败 after {elapsed:.2f}s: {last_error}")
        raise APIError("API 请求多次失败", 0, str(last_error))

    def get(self, path, params=None, headers=None):
        return self._request("GET", path, params=params, headers=headers)

    def post(self, path, json_data=None, headers=None):
        return self._request("POST", path, json=json_data, headers=headers)

    def put(self, path, json_data=None, headers=None):
        return self._request("PUT", path, json=json_data, headers=headers)

    def delete(self, path, headers=None):
        return self._request("DELETE", path, headers=headers)
