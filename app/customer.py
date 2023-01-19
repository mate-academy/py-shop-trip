import dataclasses
import datetime


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: dict

    def the_cheapest_trip_to_the_store(self, shops: dict) -> str:
        result = "Outskirts Shop"
        cost = self.money
        for shop_name, shop_value in shops.items():
            if shop_value < cost:
                cost = shop_value
                result = shop_name
        return result

    def print_check(self, cheapest_shop: dict, total_cost: float) -> None:
        date_of_purchase = \
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(
            f"""Date: {date_of_purchase}
Thanks, {self.name}, for you purchase!
You have bought: 
{self.product_cart["milk"]} milks for {cheapest_shop["milk"]} dollars
{self.product_cart["bread"]} breads for {cheapest_shop["bread"]} dollars
{self.product_cart["butter"]} butters for {cheapest_shop["butter"]} dollars
Total cost is {total_cost} dollars
See you again!\n"""
        )
