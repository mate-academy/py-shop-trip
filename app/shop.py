class Shop:

    def __init__(self, name, location: list, products: dict):
        self.name = name
        self.location = location
        self.products = products

    def full_amount_shopping(self, customer, petrol):
        coast = 0

        for key, value in self.products.items():

            coast += value * customer.product_cart[key]

        full_coast = round(customer.distance(
            self.location) * 2 / 100 * customer.car[
            "fuel_consumption"] * petrol + coast, 2)
        return full_coast

    def check_shop(self, customer):
        coast = 0
        """check - complete information about each purchase"""
        check = ""
        for key, value in self.products.items():
            coast = value * customer.product_cart[key]
            check += f"{customer.product_cart[key]}" \
                     f" {key}s for {coast} dollars\n"
        print(check[:-1])

    def total_coast(self, customer):
        coast = 0
        for key, value in self.products.items():
            coast += value * customer.product_cart[key]
        return coast
