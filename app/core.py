from app.customer import Customer
from app.parser import Parser
from app.printer import Printer
from app.shop import Shop


class Core:
    def __init__(self, data: dict) -> None:
        parsed_data = Parser(data).parse_data()
        self.fuel_price, self.customers, self.shops = parsed_data

    def run(self) -> None:
        for customer in self.customers:
            customer_home = customer.location
            trip_expenses = self.calculate_expenses(customer)

            Printer.print_customer_balance(customer)
            Printer.print_expenses(customer.name, trip_expenses)

            cheapest_shop = min(trip_expenses, key=trip_expenses.__getitem__)

            if trip_expenses[cheapest_shop] > customer.balance:
                Printer.print_ride_failure(customer.name)
                continue

            customer.refuel(cheapest_shop.location, self.fuel_price)
            customer.drive_to(cheapest_shop.location)
            Printer.print_ride(customer.name, cheapest_shop.name)

            receipt = cheapest_shop.checkout(customer)
            Printer.print_receipt(receipt)

            customer.refuel(customer_home, self.fuel_price)
            customer.drive_to(customer_home)
            Printer.print_ride_home(customer.name)
            Printer.print_customer_balance(customer, now=True)
            print()

    def calculate_expenses(
            self,
            customer: Customer
    ) -> dict[Shop, float | int]:
        trip_expenses = {}
        for shop in self.shops:
            fuel_cost = customer.car.get_fuel_cost(
                customer.location, shop.location, self.fuel_price
            )
            expense = (shop.calculate_cart_cost(customer.product_cart)
                       + (2 * fuel_cost))
            trip_expenses[shop] = expense
        return trip_expenses
