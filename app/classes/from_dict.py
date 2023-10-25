from abc import ABC, abstractmethod


class FromDict(ABC):
    @staticmethod
    @abstractmethod
    def from_dict(cls_dict: dict) -> None:
        pass
