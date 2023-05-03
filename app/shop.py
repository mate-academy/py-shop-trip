class Shop:
    def __init__(self,
                 name: str,
                 location: list[int],
                 product_information: dict) -> None:
        self.name = name
        self.location = location
        self.product_information = product_information
