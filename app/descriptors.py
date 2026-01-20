from typing import Optional, Type, Any

from app.car import Car
from app.location import Location


class ArgsLoader:
    def __init__(self, obj: Optional[Type[Car | Location]] = None) -> None:
        self.obj = obj

    def __set_name__(self, instance: Car | Location, name: str) -> None:
        self.name = name
        self.private_name = "__" + name

    def __get__(
            self,
            instance: Car | Location,
            owner: None = None
    ) -> Type[Car | Location]:
        value = getattr(instance, self.private_name)
        return value

    def __set__(
            self,
            instance: Car | Location,
            value: Any
    ) -> None:
        if self.obj:
            if isinstance(value, list):
                value = self.obj(*value)
            if isinstance(value, dict):
                value = self.obj(**value)

        setattr(instance, self.private_name, value)
