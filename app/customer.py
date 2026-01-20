class Customer:
    def __init__(self,
                 name,
                 product_cart,
                 location,
                 money,
                 fuel_consumption):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.fuel_consumption = fuel_consumption

    def riding_home(self, shop):
        return f"{self.name} rides home\n" \
               f"{self.name} now has {self.money - shop.total_cost} dollars"
