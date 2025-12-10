from typing import Any


def check_values(dict_for_test: dict, *keys: Any) -> bool:
    for key in keys:
        if key not in dict_for_test:
            return False
    return True
