class ConfigException(Exception):
    pass


class EmptyConfigException(ConfigException):
    def __init__(self, message: str) -> None:
        super().__init__(message)
