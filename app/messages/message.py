from dataclasses import dataclass


from app.customers.customer import Customer
from app.messages.keys import DictKeys


@dataclass
class Messages:
    customer: Customer
    currency: str = "dollars"

    @staticmethod
    def keys() -> DictKeys:
        return DictKeys()

    def customer_name(self) -> str:
        return self.customer.name.title()

    def print_all_trips_cost(self, shops_info: dict) -> None:
        keys = self.keys()
        print(f"{self.customer_name()} "
              f"has {self.customer.money} {self.currency}")
        for shop_name, prices_data in shops_info.items():
            trip_price = prices_data[keys.trip_price]
            print(f"{self.customer_name()}'s trip "
                  f"to the {shop_name} costs {trip_price}")

    def print_trip_check(self, date: str,
                         prices_dict: dict[str: int | float],
                         ) -> None:
        customer = self.customer_name()
        keys = self.keys()
        print(f"Date: {date}\n"
              f"Thanks, {customer}, for your purchase!\n"
              f"You have bought: ")
        for product, count in self.customer.product_cart.items():
            prods = f"{product}s" if count > 1 else product
            print(f"{count} {prods} "
                  f"for {prices_dict[product]} {self.currency}")
        trip_price = prices_dict[keys.trip_price]
        money_left = self.customer.money - trip_price
        store_check = prices_dict[keys.store_check]
        print(f"Total cost is {store_check} {self.currency}\n"
              f"See you again!\n"
              f"\n"
              f"{customer} rides home\n"
              f"{customer} now has {round(money_left, 2)} "
              f"{self.currency}\n")

    def money_not_enough_message(self) -> None:
        print(f"{self.customer_name()} doesn't have "
              f"enough money to make a purchase in any shop")

    def print_customer_check(self,
                             date: str,
                             prices_dict: dict | None) -> None:
        keys = self.keys()
        if isinstance(prices_dict, dict):
            shop_name = prices_dict[keys.shop_name].title()
            print(f"{self.customer_name()} rides to {shop_name}\n")
            self.print_trip_check(date=date,
                                  prices_dict=prices_dict)
        else:
            self.money_not_enough_message()
