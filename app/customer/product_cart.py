class ProductCart:
    """A class to create a customer`s product cart"""
    def __init__(self, products: dict) -> None:
        self.milk = products["milk"]
        self.bread = products["bread"]
        self.butter = products["butter"]
