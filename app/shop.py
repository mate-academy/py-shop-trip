from datetime import datetime
from app.info import full_info


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int, int],
            products: dict[str, int]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def shop_receipt(self, name: str, product_carts: dict) -> str:
        now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        total_cost = 0
        print(f""
              f"\n"
              f"Date: {now}\n"
              f"Thanks, {name}, for your purchase!"
              f"\nYou have bought:"
              f"")
        for key, value in product_carts.items():
            cost = 0
            cost += self.products[key] * value
            print(f"{value} {key}s for {cost} dollars")
            total_cost += cost
        return f"Total cost is {total_cost} dollars\nSee you again!\n"


def shop_to_class(json_file: str) -> list[Shop]:
    info = full_info(json_file)
    shop_list = []

    for shop in info["shops"]:
        shop_class = Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        shop_list.append(shop_class)
    return shop_list
