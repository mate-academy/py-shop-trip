class Customer:
    def __init__(self, customer):
        self.name = customer["name"]
        self.money = customer["money"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.car = customer["car"]

    def get_money_before_trip(self):
        # Prints the buyer's money before the trip
        print(f"{self.name} has {self.money} dollars")

    def get_money_after_trip(
            self,
            location_of_shop,
            price_of_fuel,
            shop_of_products
    ):
        # Prints the amount of money after a trip to the shop
        cost_of_trip = self.get_cost_of_trip(location_of_shop, price_of_fuel)
        cost_of_products = self.get_cost_of_products(shop_of_products)
        spending = cost_of_trip + cost_of_products
        return f"{self.name} rides home\n" \
               f"{self.name} now has {round(self.money - spending, 2)} dollars"

    def get_cost_of_products(self, shop_products):
        # Returns the amount of money for products in the shop
        cost = 0
        for product in self.product_cart:
            if product in shop_products.products:
                customer_product = self.product_cart[product]
                shop_product = shop_products.products[product]
                cost += customer_product * shop_product
        return cost

    def get_full_cost_to_shop(
            self,
            shop_of_products,
            location_of_shop,
            price_of_fuel
    ):
        # Returns money for travel and purchases
        cost_of_trip = self.get_cost_of_trip(location_of_shop, price_of_fuel)
        cost_of_products = self.get_cost_of_products(shop_of_products)
        full_cost = round(cost_of_trip + cost_of_products, 2)
        print(f"{self.name}'s trip to the"
              f" {shop_of_products.name} costs {full_cost}")
        return full_cost

    def get_cost_of_trip(self, location_of_shop, price_of_fuel):
        # Returns money for the trip in two directions
        location_x = (self.location[0] - location_of_shop[0]) ** 2
        location_y = (self.location[1] - location_of_shop[1]) ** 2
        fuel_consumption = self.car["fuel_consumption"] * price_of_fuel
        return pow((location_x + location_y), 0.5) / 100 * fuel_consumption * 2
