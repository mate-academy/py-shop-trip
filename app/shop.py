class Shop:

    def __init__(self, name, location: list, products: dict):
        self.name = name
        self.location = location
        self.products = products

    def full_amount_shopping(self, customer, petrol):
        cost = 0

        for key, value in self.products.items():
            cost += value * customer.product_cart[key]

        full_cost = round(customer.distance(
            self.location) * 2 / 100 * customer.car[
            "fuel_consumption"] * petrol + cost, 2)
        return full_cost

    def bill_shop(self, customer):
        """check - complete information about each purchase"""
        bill = ""
        for key, value in self.products.items():
            cost = value * customer.product_cart[key]
            bill += f"{customer.product_cart[key]}" \
                    f" {key}s for {cost} dollars\n"
        print(bill[:-1])

    def total_cost(self, customer):
        cost = 0
        for key, value in self.products.items():
            cost += value * customer.product_cart[key]
        return cost
