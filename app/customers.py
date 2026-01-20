from app.data import customers_list, fuel_price


class Customer:
    def __init__(
            self,
            name,
            product_cart,
            location,
            money,
            fuel_consumption
    ):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money,
        self.fuel_consumption = fuel_consumption

    def distance(self, shop):
        a = self.location
        b = shop.location
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

    def riding(self, shop):
        fuel_km = self.fuel_consumption / 100
        return round(fuel_km * self.distance(shop) * fuel_price * 2, 2)

    def shopping(self, shop):
        products = list(self.product_cart.keys())
        products_count = list(self.product_cart.values())
        products_costs = [count * shop.prices[i]
                          for i, count in enumerate(products_count)]
        shopping_cost = sum(products_costs)
        total_cost = shopping_cost + self.riding(shop)

        return [
            self.name,
            self.money[0],
            shop.name,
            products_count,
            products,
            products_costs,
            shopping_cost,
            total_cost
        ]


customers = [
    Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        customer["car"]["fuel_consumption"]
    )
    for customer in customers_list
]
