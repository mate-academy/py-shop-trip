class Customer:
    def __init__(self, customer_dict: dict) -> None:
        for key, value in customer_dict.items():
            setattr(self, key, value)
