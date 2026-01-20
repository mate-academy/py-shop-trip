from app.customers.customer import Customer
from app.shops.shop import Shop
from app.trips.point import Point
from app.shops.cart import Cart


class Trip:
    def __init__(
            self,
            fuel_price: float,
            customer: Customer,
            shops: list[Shop]
    ) -> None:
        self.fuel_price = fuel_price
        self.customer = customer
        self.shops = shops
        self.cost = {}

    def print_trip_log(self) -> None:
        print(f"{self.customer.name} has {self.customer.money} dollars")

        for shop in self.shops:
            self.cost[shop] = self.calculate_shop_trip_cost(shop)

            print(
                f"{self.customer.name}'s trip to the "
                f"{shop.name} costs {self.cost[shop]['total']}"
            )

        closest_shop = self.find_closest_shop()

        if self.customer.money > self.cost[closest_shop]["total"]:
            print(f"{self.customer.name} rides to {closest_shop.name}\n")

            closest_shop.print_shop_log(self.cost[closest_shop], self.customer)

            print(f"{self.customer.name} rides home")
            print(f"{self.customer.name} now has "
                  f"{self.customer.money} dollars\n")

        else:
            print(
                f"{self.customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )

    def calculate_shop_trip_cost(self, shop: Shop) -> dict:
        distance = Point.calculate_distance(
            self.customer.location,
            shop.location
        )
        trip_fuel_price = 2 * self.customer.car.calculate_fuel_spent(
            distance, self.fuel_price
        )

        product_cost = Cart(
            self.customer.cart,
            shop.products
        ).calculate_product_cost()

        total_spending = round(product_cost + trip_fuel_price, 2)

        return {"products_cost": product_cost, "total": total_spending}

    def find_closest_shop(self) -> dict:
        return min(self.cost, key=lambda shop: self.cost[shop]["total"])
