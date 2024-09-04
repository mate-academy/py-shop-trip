import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def create_shops(cls, shops_config: list) -> list:
        return [
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            for shop in shops_config
        ]

    def get_check(self, customer: "Customer") -> None:
        total_cost = 0
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought:"
        )

        for product, count in customer.product_cart.items():
            cost = count * self.products[product]
            total_cost += cost
            cost = int(cost) if cost == int(cost) else cost
            print(
                f"{count} {product}s for "
                f"{cost} dollars"
            )
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
