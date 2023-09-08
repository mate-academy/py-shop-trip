from typing import List, Dict, Any
import datetime


class Shop:
    def __init__(
        self,
        name: str,
        location: List[int | float],
        products: Dict[str, int | float],
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def get_shops_list(data: dict) -> List["Shop"]:
        shops_list = []
        for shop in data["shops"]:
            products = {
                name: price for name, price in shop["products"].items()
            }
            shop_instance = Shop(
                name=shop["name"], location=shop["location"], products=products
            )
            shops_list.append(shop_instance)
        return shops_list

    def make_purchase(self, customer: Any, cost: float) -> None:
        print(
            f"\nDate: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: "
        )
        customer.money -= cost
        products_in_bill = customer.bill_total(self, False)
        for name, quantity in customer.products.items():

            print(f"{quantity} {name}s for {products_in_bill[name]} dollars")
        bill_total = customer.bill_total(self, True)
        print(f"Total cost is {bill_total} dollars\nSee you again!\n")
