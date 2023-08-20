from app.customer import Customer
import datetime
from app.error import InitialDataError


class Shop:
    def __init__(self,
                 name: str,
                 location: list[int],
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_distance(self, customer: list[int]) -> float:
        distance = ((customer[0] - self.location[0]) ** 2
                    + (customer[1] - self.location[1]) ** 2) ** (1 / 2)
        return distance

    @staticmethod
    def calculate_fuel_cost(
            distance: float,
            fuel_consumption: float,
            fuel_price: float
    ) -> float:
        fuel_cost = distance * fuel_price * fuel_consumption / 100
        return fuel_cost

    def calculate_products_cost(self, product_cart: dict) -> float:
        price = 0
        for product, count in product_cart.items():
            price += self.products.get(product, 0) * count
        return price

    def shop_visit(self, customer: Customer, cheapest_cost: float) -> None:
        print()
        current_data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_data}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        for product, count in customer.product_cart.items():
            print(f"{count} {product}s "
                  f"for {count * self.products[product]} dollars")
        print(f"Total cost is {cheapest_cost} dollars")
        print("See you again!")


def make_shop_trip(
        customer: Customer,
        shop_list: list[Shop],
        fuel_price: float
) -> None:

    print(f"{customer.name} has {customer.money} dollars")

    if len(shop_list) == 0:
        raise InitialDataError("Shops not set in file")

    cost_of_trips = {}

    for store in shop_list:
        distance_to_shop = store.calculate_distance(customer.location)
        fuel_cost = store.calculate_fuel_cost(
            distance_to_shop,
            customer.car.fuel_consumption,
            fuel_price)
        products_cost = store.calculate_products_cost(customer.product_cart)
        cost_of_trip = 2 * fuel_cost + products_cost
        cost_of_trip = round(cost_of_trip, 2)

        print(f"{customer.name}'s trip to the {store.name} "
              f"costs {cost_of_trip}")

        cost_of_trips[cost_of_trip] = [store, products_cost]

    cheapest_cost = min(cost_of_trips)
    cheapest_shop = cost_of_trips[cheapest_cost][0]
    cheapest_products_cost = cost_of_trips[cheapest_cost][1]

    if cheapest_cost > customer.money:
        print(f"{customer.name} doesn't have enough money "
              f"to make a purchase in any shop")
        return

    print(f"{customer.name} rides to {cheapest_shop.name}")
    customer_location = customer.location
    customer.location = cheapest_shop.location

    cheapest_shop.shop_visit(customer, cheapest_products_cost)

    print(f"\n{customer.name} rides home")
    customer.location = customer_location
    print(f"{customer.name} now has {customer.money - cheapest_cost} "
          f"dollars\n")
