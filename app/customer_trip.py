import json
import datetime
from app.shop import Shop


class Customer:
    def __init__(self, data: dict) -> None:
        self.data = data

    @staticmethod
    def open_file(file_name: str) -> dict:
        with open(file_name, "r") as j_son:
            data = json.load(j_son)
        return data

    @staticmethod
    def transform_in_plural(data: list[str]) -> list:
        return [element + "s" for element in data]

    @staticmethod
    def print_date(customer: dict) -> None:
        name = customer["name"]
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(
            f"\nDate: {date}\nThanks, {name}, "
            f"for your purchase!\nYou have bought:"
        )

    def check_perf_purchase(
        self,
        customer: dict,
        shop_data: tuple,
    ) -> bool:
        name = customer["name"]
        shop_index = shop_data[1][1]
        if customer["money"] < shop_data[1][0] + Shop.check_money(
            customer["product_cart"],
            self.data["shops"][shop_index]["products"]
        ):
            print(
                f"{name} doesn't have enough money to make a "
                f"purchase in any shop"
            )
            return False
        else:
            shop_name = self.data["shops"][shop_index]["name"]
            print(f"{name} rides to {shop_name}")
            customer["location"] = self.data["shops"][shop_index]["location"]
            return True

    def customer_trip(self) -> None:
        # Loop of customers data.
        for customer in self.data["customers"]:
            name = customer["name"]
            money = customer["money"]
            print(f"{name} has {money} dollars")

            # Loop of shop data.
            shop_data = Shop(self.data,
                             customer,
                             self.data["FUEL_PRICE"]).iter_shops(name)

            # Check the possibility to perform purchase for all customer.
            if not self.check_perf_purchase(customer, shop_data):
                return
            Customer.print_date(customer)

            # Convert to plural the list of "product cart".
            list_prod = Customer.transform_in_plural(
                list(customer["product_cart"].keys())
            )

            # Loop for each product inside "product cart".
            Shop(self.data, customer, self.data["FUEL_PRICE"]).iter_products(
                shop_data, list_prod
            )
