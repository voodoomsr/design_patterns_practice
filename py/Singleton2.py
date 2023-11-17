from typing import Any

class Singleton:
    _instance: Any = None
    data: Any = None

    def __new__(cls, data: Any = None) -> Any:
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.data = data
        return cls._instance
