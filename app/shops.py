class Shop:
    def __init__(self, shops_dict: dict) -> None:
        for key, value in shops_dict.items():
            setattr(self, key, value)
