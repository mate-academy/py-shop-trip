from app.protocol import CustomerProtocol


class Shop:
    def __init__(self,
                 name: str,
                 location: list[int],
                 products: dict[str, int | float]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def check_products(self, cart: dict[str, int]) -> bool:
        for product in cart:
            if product not in self.products:
                return False
        return True

    def buy_products(self,
                     customer: CustomerProtocol,
                     fuel_price: float) -> None:
        # started_location = customer.location
        print(f"{customer.name} rides to {self.name}")
        # customer.location = self.location
        print()
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, "
              f"for your purchase!\nYou have bought:")
        total = 0
        for product, amount in customer.product_cart.items():
            price_for_couple = amount * self.products[str(product)]
            print(f"{amount} {product}s for {price_for_couple} dollars")
            total += price_for_couple
        print(f"Total cost is {total} dollars\nSee you again!")
        print()
        remind = customer.money - customer.calc_trip_cost(self, fuel_price)
        # customer.location = started_location
        print(f"{customer.name} rides home\n{customer.name} "
              f"now has {remind} dollars\n")
