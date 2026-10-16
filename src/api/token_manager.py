import functools
from typing import Dict, Optional

import requests


# ========== 第一部分：Token 管理器 ==========
class TokenManager:
    def __init__(self, token_url, client_id, client_secret):
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.refresh_token = None
        self.expires_at = 0

    def set_token(self, token_data: Dict):
        # 设置 Token，计算过期时间（提前 60 秒）
        pass

    def is_expired(self) -> bool:
        # 检查是否过期
        pass

    def get_valid_token(self) -> Optional[str]:
        # 获取有效 Token，过期则自动刷新
        pass

    def _refresh_token(self) -> bool:
        # 用 refresh_token 刷新
        pass


# ========== 第二部分：重试装饰器 ==========
def retry_on_exception(max_retries=3, delay=1.0, backoff=2.0, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 实现指数退避重试逻辑
            pass

        return wrapper

    return decorator


# ========== 第三部分：安全 API 客户端 ==========
class SecureAPIClient:
    def __init__(self, base_url, token_manager=None):
        self.base_url = base_url.rstrip("/")
        self.token_manager = token_manager
        self.session = requests.Session()

    def _request(self, method, endpoint, **kwargs) -> Dict:
        # 1. 注入 Token
        # 2. 发送请求
        # 3. 401 则刷新 Token 后重试
        # 4. raise_for_status
        pass

    def get(self, endpoint, params=None) -> Dict:
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint, data=None) -> Dict:
        return self._request("POST", endpoint, json=data)


# ========== 测试 ==========
if __name__ == "__main__":
    tm = TokenManager(
        token_url="http://127.0.0.1:8000/oauth/token", client_id="test_client_id", client_secret="test_client_secret"
    )
    client = SecureAPIClient("http://127.0.0.1:8000", token_manager=tm)
    result = client.get("/api/test", params={"token": tm.get_valid_token()})
    print(result)
