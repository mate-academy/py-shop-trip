from app.Customers import ShopTrip
from datetime import datetime


class Shop(ShopTrip):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.total_cost = 0
        self.customer_location = self.customer_location()[self.name]

    def change_location(self) -> None:
        shop_location = self.shops_location()[ShopTrip.shop]

        self.customer_location = shop_location

    def purchase(self) -> None:
        for (name_product1,
             num_product) in self.customer_product_cart()[self.name].items():

            product_price = self.shops_price()[ShopTrip.shop][name_product1]

            price = product_price * num_product

            self.total_cost += price

            print(f"{num_product} {name_product1}s"
                  f" for {price} dollars")

        print(f"Total cost is {self.total_cost} dollars")

    def receipt(self) -> None:
        print(f"Date: {datetime.now().strftime('04/01/2021 12:33:41')}\n"
              f"Thanks, {self.name}, for you purchase!\n"
              f"You have bought: ")
        self.purchase()

        print("See you again!\n")

    def ride_home(self) -> None:
        remaining_money = round(ShopTrip.money
                                - ShopTrip.price_trip, 2)

        print(f"{self.name} rides home\n"
              f"{self.name} now has {remaining_money} dollars\n")
