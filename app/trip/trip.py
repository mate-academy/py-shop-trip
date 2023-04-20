from app.customer.customer import Customer
from app.shop.shop import Shop
from app.trip.calculation import fuel_costs, shopping_cost
from datetime import datetime


class Trip:
    """A class to create a single customer trip to shop."""

    def __init__(self, customer: Customer, shops: list[Shop]) -> None:
        self.customer = customer
        self.shops = shops
        self.shop_to_ride = None
        self.milk_price = None
        self.bread_price = None
        self.butter_price = None
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
            customer = self.customer
            product_cart = customer.product_cart
            price_list = shop.price_list
            fuel_cost = fuel_costs(customer, shop)
            cost_of_shopping = shopping_cost(product_cart, price_list)
            shopping_expenses = round(fuel_cost + cost_of_shopping, 2)

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

        milk_number = self.customer.product_cart.milk
        milk_cost = milk_number * self.milk_price

        bread_number = self.customer.product_cart.bread
        bread_cost = bread_number * self.bread_price

        butter_number = self.customer.product_cart.butter
        butter_cost = butter_number * self.butter_price

        total_cost = milk_cost + butter_cost + bread_cost

        self.customer.money -= self.minimal_shop_expenses()

        print(
            f"Thanks, {self.customer.name}, for your purchase!\n"
            f"You have bought: \n"
            f"{milk_number} milks for {milk_cost} dollars\n"
            f"{bread_number} breads for {bread_cost} dollars\n"
            f"{butter_number} butters for {butter_cost} dollars\n"
            f"Total cost is {total_cost} dollars\n"
            f"See you again!\n\n"
            f"{self.customer.name} rides home\n"
            f"{self.customer.name} now has {self.customer.money} dollars\n"
        )
