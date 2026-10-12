class AppError(Exception):
    """应用异常基类."""

    def __init__(self, message: str, error_code: str = "APP_ERROR"):
        self.message = message
        self.error_code = error_code
        super().__init__(message)

    def __str__(self):
        return f"[{self.error_code}] {self.message}"


class ConfigError(AppError):
    """配置错误."""

    def __init__(self, message: str):
        super().__init__(message, "CONFIG_ERROR")


class ValidationError(AppError):
    """数据校验错误."""

    def __init__(self, field: str, reason: str):
        super().__init__(f"字段 {field} 校验失败: {reason}", "VALIDATION_ERROR")


class APIError(AppError):
    """API 调用错误.

    统一构造签名：APIError(message, status_code=None, detail=None)
    """

    def __init__(self, message: str, status_code: int | None = None, detail: str | None = None):
        if status_code is not None:
            message = f"{message} (HTTP {status_code})"
        if detail:
            message = f"{message} - {detail}"
        super().__init__(message, "API_ERROR")
        self.status_code = status_code
        self.detail = detail
