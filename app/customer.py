from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def count_the_price(self, shops: list[Shop], fuel_price: float) -> dict:
        shop_dict = {}
        for shop in shops:
            distance = (
                (shop.location[0] - self.location[0]) ** 2
                + (shop.location[1] - self.location[1]) ** 2) ** 0.5
            amount_of_fuel = (distance * self.car.l_per_km()) * 2
            price_for_road = round((amount_of_fuel * fuel_price), 2)
            price_for_products = (
                shop.count_total_cost_of_products(self.product_cart))
            total_price = price_for_road + price_for_products
            shop_dict[shop] = total_price
        return shop_dict

    def chose_the_shop(self, shop_dict: dict) -> None:
        print(f"{self.name} has {self.money} dollars")
        for shop, price in shop_dict.items():
            print(f"{self.name}'s trip to the {shop.name} costs {price}")
        cheapest_shop = min(shop_dict, key=shop_dict.get)
        cheapest_price = shop_dict[cheapest_shop]
        remaining_money = self.money - cheapest_price
        if remaining_money >= 0:
            print(f"{self.name} rides to {cheapest_shop.name}\n")
            cheapest_shop.purchase_receipt(self.name, self.product_cart)
            print(f"{self.name} rides home\n"
                  f"{self.name} now has {remaining_money} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
