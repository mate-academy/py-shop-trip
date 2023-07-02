import datetime

from app.customer import Customer
from app.shop import Shop


class ShoppingTrip:
    def __init__(
            self,
            shops: list[Shop],
            customer: Customer,
            fuel_price: float
    ) -> None:
        self.shops = shops
        self.customer = customer
        self.fuel_price = fuel_price

    def _calculate_trip_cost(self) -> dict[str]:
        trip_options = {}

        for shop in self.shops:
            distance = (
                (
                    (shop.location[0] - self.customer.location[0]) ** 2
                    + (shop.location[1] - self.customer.location[1]) ** 2
                ) ** 0.5
            )

            fuel_cost = round(
                2 * distance / 100 * self.customer.car["fuel_consumption"]
                * self.fuel_price, 2
            )

            products_cost = sum([
                shop.products[product] * amount
                for product, amount
                in self.customer.product_cart.items()
            ])

            trip_options[shop.name] = {}
            trip_options[shop.name]["trip_cost"] = fuel_cost + products_cost
            trip_options[shop.name]["products"] = shop.products
            trip_options[shop.name]["products_cost"] = products_cost

        return trip_options

    def go_to_shop(self) -> None:
        print(f"{self.customer.name} has {self.customer.money} dollars")

        cheapest_shop = ""
        total_cost = 0
        trip_options = self._calculate_trip_cost()

        for shop_name, trip_data in trip_options.items():
            trip_cost = trip_data["trip_cost"]
            print(f"{self.customer.name}'s trip to the {shop_name} "
                  f"costs {trip_cost}")
            if total_cost == 0 or total_cost > trip_data["trip_cost"]:
                cheapest_shop = shop_name
                total_cost = trip_data["trip_cost"]

        if total_cost > self.customer.money:
            print(f"{self.customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return

        print(
            f"{self.customer.name} rides to {cheapest_shop}\n",
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
            f"Thanks, {self.customer.name}, for your purchase!",
            "You have bought: ",
            sep="\n"
        )

        for product, amount in self.customer.product_cart.items():
            cost = amount * trip_options[cheapest_shop]["products"][product]
            if amount > 1:
                product += "s"
            print(f"{amount} {product} for {cost} dollars")

        products_cost = trip_options[cheapest_shop]["products_cost"]
        money_left = self.customer.money - total_cost
        print(
            f"Total cost is {products_cost} dollars\n"
            f"See you again!\n\n"
            f"{self.customer.name} rides home\n"
            f"{self.customer.name} now has {money_left} dollars\n"
        )
