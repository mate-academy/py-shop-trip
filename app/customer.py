from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name, product_cart, location, money) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car

    def has_money(self):
        print(f"{self.name} has {self.money} dollars")

    def total_shopping_list_price(self, shop: Shop) -> dict:
        total_cost = {}
        for product_name, price in shop.products.items():
            total_cost[shop.name] = (price * self.product_cart.get(product_name, 0))
        return total_cost

    def price_summery(self, shops: Shop):
        cheapest_shopping = []
        for shop_name, total_amount in self.total_shopping_list_price(shops).items():
            print(f"{self.name}'s trip to the {shop_name} costs {total_amount}")
            cheapest_shopping.append(total_amount)
            cheapest_shop = {i for i in self.total_shopping_list_price(shops) if
                             self.total_shopping_list_price(shops)[i] == min(cheapest_shopping)}
            if min(cheapest_shopping) <= self.has_money():
                print(f"{self.name} rides to {cheapest_shop}")

    def shopping(self, shops: Shop, fuel_cost: float) -> None:
        print(f"{self.name} rides home")
        print(
            f"{self.name} now has {self.money - self.total_shopping_list_price(shops) - Car.calculate_road_expenses(shops, self.name, fuel_cost)} dollars\n")

