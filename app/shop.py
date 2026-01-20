import dataclasses
import datetime

from app.customer import Customer


@dataclasses.dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    @staticmethod
    def get_shop_list(config: dict) -> list:
        shop_list = config.get("shops")
        result = []

        for shop in shop_list:
            result.append(Shop(
                shop["name"],
                shop["location"],
                shop["products"])
            )

        return result

    def get_receipt(self, customer: Customer) -> tuple:
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        receipt = [
            f"Date: {current_date}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            "You have bought:\n"
        ]

        amount = 0

        for item in customer.product_card:
            cost = self.products[item] * customer.product_card[item]
            amount += cost
            formatted_cost = f"{cost: .2f}".rstrip("0").rstrip(".")
            receipt.append(
                f"{customer.product_card[item]}"
                f" {item}s for"
                f"{formatted_cost}"
                f" dollars\n"
            )

        receipt.append(
            f"Total cost is {round(amount, 2)} dollars\n" f"See you again!\n"
        )

        return "".join(receipt), amount
