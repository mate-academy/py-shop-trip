import datetime

from app.location import Location


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self._name = name
        self._location = Location(*location)
        self._products = products

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> Location:
        return self._location

    @property
    def products(self) -> dict:
        return self._products

    def __repr__(self) -> str:
        return f"shop {self.name} located {self.location} has {self.products}"

    def calculate_cart_price(
        self,
        customer_cart: dict,
        printout: bool = False
    ) -> float | str:
        total_sum = 0
        total_check = []
        for product, quantity in customer_cart.items():
            product_sum = self.products[product] * quantity
            total_check.append((
                f"{quantity} {product}{'s' if quantity > 1 else ''} "
                f"for {product_sum} dollars"
            ))
            total_sum += product_sum
        total_check.append(f"Total cost is {total_sum} dollars")
        if printout:
            return "\n".join(total_check)
        return total_sum

    def checkout(self, customer_name: str, customer_cart: dict) -> None:
        print("\nDate:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer_name}, for you purchase!\nYou have bought: ")
        print(self.calculate_cart_price(customer_cart, printout=True))
        print("See you again!\n")
