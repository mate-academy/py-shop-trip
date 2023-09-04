from app.car.car_class import Car


class Customer:
    def __init__(self, customer: dict, fuel_price: str) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = Car(customer["car"], float(fuel_price))

    def go_to_shop(self, shops: dict) -> None:
        print(f"{self.name} has {self.money} dollars")

        cheapest_store = self.find_cheapest_store(shops)

        if cheapest_store:
            self.detailed_store_transactions(cheapest_store)

    def cost_of_way(self, shop_location: list) -> float:
        return self.car.cost_of_way(self.location, shop_location)

    def cost_of_products_in_shop(
            self,
            shop: dict,
    ) -> list[float, dict]:
        sum_of_all_products_in_shop = 0

        for key, value in shop["products"].items():
            sum_of_all_products_in_shop += round(
                self.product_cart.get(key) * value, 2
            )

        sum_of_all_products_in_shop += self.cost_of_way(shop["location"])

        print(
            f"{self.name}'s trip to the "
            f"{shop['name']} costs {sum_of_all_products_in_shop}"
        )

        return [sum_of_all_products_in_shop, shop]

    def find_cheapest_store(self, shops: dict) -> None | dict:
        sum_of_all_costs = 0
        shop_detail = None

        for shop in shops:
            result = self.cost_of_products_in_shop(shop)
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

    def detailed_store_transactions(self, shop: dict) -> None:
        print(
            f"Date: 04/01/2021 12:33:41\n"
            f"Thanks, {self.name}, for your purchase!\n"
            f"You have bought: "
        )

        sum_of_all_products_in_shop = 0

        for key, value in shop["products"].items():
            sum_of_product = round(self.product_cart.get(key) * value, 2)

            print(
                f"{self.product_cart.get(key)} {key}s "
                f"for {sum_of_product} dollars"
            )

            sum_of_all_products_in_shop += sum_of_product

        print(
            f"Total cost is {sum_of_all_products_in_shop} dollars\n"
            "See you again!\n"
        )

        sum_of_all_products_in_shop += self.cost_of_way(shop["location"])

        self.money -= sum_of_all_products_in_shop

        print(
            f"{self.name} rides home\n"
            f"{self.name} now has {self.money} dollars\n"
        )
