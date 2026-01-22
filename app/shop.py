from app.customer import Customer


class Shop:
    def __init__(
        self,
        name: str,
        location: list[int],
        products: dict,
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __repr__(self) -> str:
        return (
            f"Shop ({self.name}, "
            f"{self.location}, {self.products})"
        )

    def check(self, customer: Customer) -> None:

        print(
            f"Date: 04/01/2021 12:33:41\n"  # noqa E231
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought:"  # noqa E231
        )
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            product_price = self.products.get(product)
            cost = quantity * product_price
            cost = int(cost) if cost == int(cost) else float(cost)
            total_cost += cost
            print(
                f"{quantity} {product}s for {cost} dollars"
            )
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
