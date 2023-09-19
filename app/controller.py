from app.shops.shop import Shop
from app.customers.customer import Customer
from app.days.day import DayMark
from app.messages.trip_calculator import Calculator
from app.messages.message import Messages


class CustomersTrips:
    def __init__(self,
                 customers: list[Customer],
                 shops: list[Shop],
                 day: DayMark) -> None:
        self.customers = customers
        self.shops = shops
        self.day = day

    def activate_calculator(self,
                            customer: Customer) -> Calculator:
        calculator = Calculator(
            customer=customer,
            shops=self.shops,
            day=self.day
        )
        return calculator

    def print_trip_message(self) -> None:
        for customer in self.customers:
            calculator = self.activate_calculator(customer)
            messages = Messages(customer=customer)
            messages.print_all_trips_cost(calculator.trips_checks)
            customer_check = calculator.get_shop_check()
            messages.print_customer_check(date=self.day.date,
                                          prices_dict=customer_check)
