class ConfigError(Exception):
    pass


def validate_location(location: list, context: str) -> tuple:
    if not isinstance(location, (tuple, list)):
        raise ConfigError(f"{context} location must be a list or tuple.")
    if len(location) != 2:
        raise ConfigError(
            f"{context} location must have"
            f" exactly 2 elements, got {len(location)}"
        )
    return tuple(location)
