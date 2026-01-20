from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int, int],
            money: int | float
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.home_location = location
        self.location = self.home_location
        self.money = money
        self.trip_costs = {}
        self.chosen_shop = None
        self.spent_money = 0

    def amount_of_money_at_start(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def cost_of_all_trips(
            self,
            stores: list[dict],
            fuel_consumption: float,
            fuel_price: float
    ) -> None:
        for store in stores:
            shop = Shop(
                name=store["name"],
                location=store["location"],
                products=store["products"]
            )
            distance = (((shop.location[0] - self.location[0]) ** 2)
                        + ((shop.location[1] - self.location[1]) ** 2)) ** 0.5
            trip_cost = 2 * (distance * fuel_consumption / 100) * fuel_price
            product_cost = shop.purchase(product_cart=self.product_cart)
            total_cost = round((trip_cost + product_cost), 2)
            self.trip_costs[total_cost] = shop
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")

    def choose_the_shop(self) -> None:
        minimum_cost = min(self.trip_costs.keys())
        if self.money < minimum_cost:
            print(f"{self.name} doesn't have "
                  f"enough money to make a purchase in any shop")
        else:
            self.chosen_shop = self.trip_costs[minimum_cost]
            self.spent_money = minimum_cost
            print(f"{self.name} rides to {self.chosen_shop.name}\n")
            self.go_to_the_shop()
            self.go_home_and_count_money()

    def go_to_the_shop(self) -> None:
        self.location = self.chosen_shop.location
        self.chosen_shop.receipt(
            customer_name=self.name,
            product_cart=self.product_cart
        )

    def go_home_and_count_money(self) -> None:
        self.location = self.home_location
        print(f"{self.name} rides home\n{self.name} "
              f"now has {self.money - self.spent_money} dollars\n")
