from app.car.car_class import Car


class Customer:
    def __init__(self, customer: dict, fuel_price: str) -> None:
        self.name = customer["name"]
        self.cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = Car(customer["car"], float(fuel_price))

    def go_to_shop(self, shops: dict) -> None:
        print(f"{self.name} has {self.money} dollars")

        shop = self.cost_of_trip(shops)

        if shop:
            self.cost_of_product(shop, True)

    def cost_of_way(self, shop_location: list) -> float:
        return self.car.cost_of_way(self.location, shop_location)

    def cost_of_product(
            self,
            shop: dict,
            detail: bool = False
    ) -> list[float, dict]:
        if detail:
            print(
                f"Date: 04/01/2021 12:33:41\n"
                f"Thanks, {self.name}, for your purchase!\n"
                f"You have bought: "
            )

        sum_of_prices = 0

        for key, value in shop["products"].items():
            cost_of_product = round(self.cart.get(key) * value, 2)
            sum_of_prices += cost_of_product
            if detail:
                print(
                    f"{self.cart.get(key)} {key}s "
                    f"for {cost_of_product} dollars"
                )

        sum_of_prices += self.cost_of_way(shop["location"])

        if detail:
            self.money -= sum_of_prices
            cost_of_product = round(
                sum_of_prices - self.cost_of_way(shop["location"]
                                                 ), 2)
            print(
                f"Total cost is {cost_of_product} dollars\n"
                "See you again!\n\n"
                f"{self.name} rides home\n"
                f"{self.name} now has {self.money} dollars\n"
            )

        if not detail:
            print(
                f"{self.name}'s trip to the "
                f"{shop['name']} costs {sum_of_prices}"
            )

        return [sum_of_prices, shop]

    def cost_of_trip(self, shops: dict) -> None:
        sum_of_all_costs = 0
        shop_detail = None

        for shop in shops:
            result = self.cost_of_product(shop)
            if sum_of_all_costs == 0 or sum_of_all_costs > result[0]:
                sum_of_all_costs = result[0]
                shop_detail = result[1]

        if self.money > sum_of_all_costs:
            print(f"{self.name} rides to {shop_detail['name']}\n")
            return shop_detail
        else:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
