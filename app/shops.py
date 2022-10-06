import dataclasses
import json
import datetime


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict

    @classmethod
    def open_json_shop(cls):
        with open("app/config.json") as json_file:
            config = json.load(json_file)

            shops = []
            for shop in config["shops"]:
                shops.append(Shop(shop["name"],
                                  shop["location"],
                                  shop["products"]))
            return shops

    def print_the_bill(self, other):
        milk_count = other.product_cart["milk"] * self.products["milk"]
        bread_count = other.product_cart["bread"] * self.products["bread"]
        butter_count = other.product_cart["butter"] * self.products["butter"]
        total_product = milk_count + bread_count + butter_count
        print("Date:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {other.name}, for you purchase!")
        print("You have bought: ")
        print(f"{other.product_cart['milk']}"
              f" milks for {milk_count} dollars")
        print(f"{other.product_cart['bread']} "
              f"breads for {bread_count} dollars")
        print(f"{other.product_cart['butter']} "
              f"butters for {butter_count} dollars")
        print(f"Total cost is {total_product} dollars")
        print("See you again!\n")
