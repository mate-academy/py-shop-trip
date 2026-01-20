class PriceList:
    """A class to create a shop price list """
    def __init__(self, products: dict) -> None:
        self.milk = products["milk"]
        self.bread = products["bread"]
        self.butter = products["butter"]
