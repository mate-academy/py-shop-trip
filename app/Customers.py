from app.Info import Info
from math import sqrt


class ShopTrip(Info):
    shop = ""
    money = 0
    price_trip = 0

    def __init__(self, name: str) -> None:

        super().__init__()
        self.name = name
        self.shop_name = None
        self.total_cost1 = {}
        self.choose_min = []

    def cost_meat(self) -> None:
        for (name_product1,
             num_product) in self.customer_product_cart()[self.name].items():

            price_product = self.shops_price()[self.shop_name][name_product1]

            price = price_product * num_product

            self.total_cost1[self.shop_name] = price

            ShopTrip.price_trip += self.total_cost1[self.shop_name]

    def customers_money(self) -> None:
        for name in self.info["customers"]:
            if name["name"] == self.name:
                ShopTrip.money = name["money"]
                print(f"{self.name} has {name['money']} dollars")
                break

    def calculate_cost_trip(self) -> None:

        for name, shop_location in self.shops_location().items():
            x_coord = self.customer_location()[self.name][0]
            y_coord = self.customer_location()[self.name][1]

            km_to_the_shop = sqrt(((shop_location[0] - x_coord) ** 2)
                                  + ((shop_location[1] - y_coord) ** 2))

            liter_fuel_to_the_shop = (km_to_the_shop
                                      * self.cars_customer()[self.name]) / 100

            price_trip_to_the_shop = (liter_fuel_to_the_shop
                                      * self.info["FUEL_PRICE"])

            ShopTrip.price_trip = price_trip_to_the_shop * 2

            self.shop_name = name

            self.cost_meat()

            print(f"{self.name}'s trip to the {name} costs "
                  f"{round(ShopTrip.price_trip, 2)}")

            self.total_cost1[name] = round(ShopTrip.price_trip, 2)

    def ride_to_the_shop(self) -> None | bool:
        min_cost = min(self.total_cost1.values())

        for name in self.total_cost1:
            if self.total_cost1[name] == min_cost:
                ShopTrip.shop = name

        ShopTrip.price_trip = min_cost

        if ShopTrip.money > min_cost:
            print(f"{self.name} rides to {ShopTrip.shop}\n")

        elif ShopTrip.money < min_cost:
            print(f"{self.name} "
                  f"doesn't have enough money to make purchase in any shop")
            return False
