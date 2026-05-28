from app.customer import Customer
from app.shop import Shop


class Printer:

    @staticmethod
    def print_customer_balance(
            customer: Customer,
            now: bool = False
    ) -> None:
        print(f"{customer.name}{' now ' if now else ' '}"
              f"has {round(customer.balance, 2)} dollars")

    @staticmethod
    def print_expenses(
            customer_name: str,
            trip_expenses: dict[Shop, float | int]
    ) -> None:
        for shop, cost in trip_expenses.items():
            print(f"{customer_name}'s trip "
                  f"to the {shop.name} costs {round(cost, 2)}")

    @staticmethod
    def print_ride_failure(customer_name: str) -> None:
        print(f"{customer_name} doesn't have "
              f"enough money to make a purchase in any shop")

    @staticmethod
    def print_ride(customer_name: str, shop_name: str) -> None:
        print(f"{customer_name} rides to {shop_name}\n")

    @staticmethod
    def print_receipt(receipt: str) -> None:
        print(receipt)

    @staticmethod
    def print_ride_home(customer_name: str) -> None:
        print(f"{customer_name} rides home")
