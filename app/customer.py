import datetime


class Customer:
    def __init__(
            self,
            name: str,
            products_to_buy: dict,
            location: list,
            money: float,
            car: dict
    ) -> None:
        self.name = name
        self.products_to_buy = products_to_buy
        self.location = location
        self.money = money
        self.car = car
        self.location_home = self.location

    def distance_to_shop(self, shop_location: list) -> float:
        return ((self.location[0] - shop_location[0]) ** 2
                + (self.location[1] - shop_location[1]) ** 2) ** 0.5

    def select_shop_and_trip(self, list_of_shops: dict) -> None:
        cheapest_shop = min(list_of_shops, key=list_of_shops.get)
        cheapest_shop_sum = min(list_of_shops.values())

        if self.money > cheapest_shop_sum:
            print(f"{self.name} rides to {cheapest_shop.name}\n")
            self.location = cheapest_shop.location

            current_date = datetime.datetime.now().strftime(
                "%d/%m/20%y %H:%M:%S"
            )
            print(f"Date: {current_date}")
            print(f"Thanks, {self.name}, for you purchase!")
            print("You have bought: ")

            products_sum_ls = cheapest_shop.products_cost(self.products_to_buy)
            check_sum = sum(products_sum_ls.values())

            for product, amount in self.products_to_buy.items():
                print(f"{amount} {product}s for "
                      f"{products_sum_ls[product]} dollars")

            print(f"Total cost is {check_sum} dollars")
            print("See you again!")

            print(f"\n{self.name} rides home")
            print(f"{self.name} now has "
                  f"{self.money - cheapest_shop_sum} dollars\n")
            self.location = self.location_home

        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make purchase in any shop")
