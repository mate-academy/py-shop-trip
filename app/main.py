from app.shop.shop import Shop
from app.trip.get_data import get_data
from app.customer.customer import Customer
from app.trip.calculation import fuel_costs, shopping_cost
from datetime import datetime


class Trip:
    """A class to create a single customer trip to shop."""

    def __init__(self, customer: Customer, shops: list[Shop]) -> None:
        self.shop = None
        self.customer = customer
        self.shops = shops
        self.shop_to_ride = None
        self.milk_price = None
        self.bread_price = None
        self.butter_price = None
        self.go_shopping()

    def go_shopping(self) -> None:
        self.customer_has_money()
        self.trips_cost()
        self.minimal_shop_expenses()
        self.define_shop_to_ride()
        if self.customer_has_enough_money():
            print(f"{self.customer.name} rides to {self.shop_to_ride}")
            self.print_date()
            self.print_summary()
        else:
            print(
                f"{self.customer.name} doesn't have enough"
                f" money to make a purchase in any shop"
            )

    def customer_has_money(self) -> None:
        """Print sum of money customer has."""
        print(f"{self.customer.name} has {self.customer.money} dollars")

    def trips_cost(self) -> None:
        """Print the costs of customer`s shop trips."""
        for shop in self.shops:
            cost_of_shopping = shopping_cost(
                self.customer.product_cart, shop.price_list
            )
            shopping_expenses = round(
                fuel_costs(self.customer, shop) + cost_of_shopping, 2
            )

            print(
                f"{self.customer.name}'s trip to the {shop.name} "
                f"costs {shopping_expenses}"
            )
            shop.expenses = shopping_expenses

    def minimal_shop_expenses(self) -> float:
        """Return minimal expenses among shops."""
        return min(shop.expenses for shop in self.shops)

    def define_shop_to_ride(self) -> None:
        """Define shop to ride."""
        for shop in self.shops:
            if shop.expenses == self.minimal_shop_expenses():
                self.shop_to_ride = shop.name
                self.milk_price = shop.price_list.milk
                self.bread_price = shop.price_list.bread
                self.butter_price = shop.price_list.butter

    def customer_has_enough_money(self) -> None:
        """Check if customer has enough money."""
        return self.customer.money >= self.minimal_shop_expenses()

    @staticmethod
    def print_date() -> None:
        """Print current date"""
        datetime_object = datetime.strptime(
            "Date: 04/01/2021 12:33:41", "Date: %m/%d/%Y %H:%M:%S"
        )
        formatted_date = datetime_object.strftime("%m/%d/%Y %H:%M:%S")
        print(f"\nDate: {formatted_date}")

    def print_summary(self) -> None:
        """Print summary of shopping session"""

        total_cost = 0
        print(
            f"Thanks, {self.customer.name}, for your purchase!\n"
            f"You have bought: "
        )
        for product, quantity in self.customer.product_cart.__dict__.items():
            if quantity > 0:
                price = getattr(self, f"{product}_price")
                cost = price * quantity
                total_cost += cost
                print(f"{quantity} {product}s for {cost} dollars")

        self.customer.money -= self.minimal_shop_expenses()

        print(
            f"Total cost is {total_cost} dollars\n"
            f"See you again!\n\n"
            f"{self.customer.name} rides home\n"
            f"{self.customer.name} now has {self.customer.money} dollars\n"
        )


def shop_trip() -> None:
    data = get_data()
    shops = get_list_of_shops(data)
    customers = get_list_of_customers(data)

    for customer in customers:
        Trip(customer, shops)


def get_list_of_shops(data: dict) -> list[Shop]:
    """Get a list of available shops."""
    shop_list = data["shops"]
    return [Shop(shop) for shop in shop_list]


def get_list_of_customers(data: dict) -> list[Customer]:
    """Get a list of customers."""
    customers_list = data["customers"]
    return [Customer(customer) for customer in customers_list]
