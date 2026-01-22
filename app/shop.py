import datetime

from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self._name = name
        self._location = location
        self._products = products

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> list[int]:
        return self._location

    @property
    def products(self) -> dict:
        return self._products

    def print_check(self, customer: Customer) -> str:
        total_cost = 0
        current_time = datetime.datetime.now()
        text_check = (f"Date: {current_time.strftime('%d/%m/%Y %H:%M:%S')}"
                      f"\nThanks, {customer.name}, for your purchase!\n"
                      f"You have bought: \n"
                      )

        for product, item in customer.products.items():
            product_cost = round(item * self.products[product], 2)
            total_cost += product_cost

            text_check += f"{item} {product}s for {product_cost} dollars\n"

        text_check += f"Total cost is {total_cost} dollars\nSee you again!"

        return text_check
