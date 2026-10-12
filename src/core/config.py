import json
from pathlib import Path
from typing import Any

from .exceptions import ConfigError


class AppConfig:
    """应用配置管理器：单例模式."""

    _instance = None
    _initialized = False

    DEFAULTS = {
        "app_name": "AI学习平台",
        "debug": False,
        "log_level": "INFO",
        "database_url": "sqlite:///dev.db",  # 默认数据库地址，各环境可在工厂中覆盖
    }
    REQUIRED_KEYS = ["app_name", "debug", "log_level"]
    VALID_LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if AppConfig._initialized:
            return
        self._config = self.DEFAULTS.copy()
        AppConfig._initialized = True

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def set(self, key: str, value: Any):
        self._config[key] = value

    def load_from_dict(self, data: dict):
        self._config.update(data)

    def load_from_file(self, filepath: str):
        path = Path(filepath)
        if not path.exists():
            raise ConfigError(f"配置文件不存在: {filepath}")
        with open(path, "r", encoding="utf-8") as f:
            self.load_from_dict(json.load(f))

    @staticmethod
    def is_valid_log_level(level: str) -> bool:
        return level in AppConfig.VALID_LOG_LEVELS

    @classmethod
    def from_dict(cls, data: dict):
        # 单例版不能再用 cls(data)：__init__ 不接收配置参数，
        # 所以先拿到唯一实例，再用 load_from_dict 覆盖配置
        config = cls()
        config.load_from_dict(data)
        return config

    def validate(self):
        for key in self.REQUIRED_KEYS:
            if key not in self._config:
                raise ConfigError(f"缺少必填配置项: {key}")
        if not self.is_valid_log_level(self.get("log_level")):
            raise ConfigError(f"无效日志级别: {self.get('log_level')}")

    def to_dict(self) -> dict:
        return self._config.copy()


class ConfigFactory:
    """配置工厂：统一创建不同环境配置."""

    @staticmethod
    def create(env: str) -> AppConfig:
        AppConfig._instance = None
        AppConfig._initialized = False

        configs = {
            "dev": {"app_name": "AI学习平台-开发环境", "debug": True, "log_level": "DEBUG", "database_url": "sqlite:///dev.db"},
            "test": {
                "app_name": "AI学习平台-测试环境",
                "debug": True,
                "log_level": "DEBUG",
                "database_url": "sqlite:///:memory:",
            },
            "prod": {"app_name": "AI学习平台", "debug": False, "log_level": "INFO", "database_url": "sqlite:///app.db"},
        }

        if env not in configs:
            raise ConfigError(f"不支持的环境: {env}")

        config = AppConfig.from_dict(configs[env])
        config.validate()
        return config
