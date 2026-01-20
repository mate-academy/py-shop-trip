import dataclasses


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    home_location: list
    money: int
    car: dict
    fuel_price: float

    def fuel_cost(self, shop):
        first_diff_square = (self.location[0] - shop.location[0]) ** 2
        second_diff_square = (self.location[1] - shop.location[1]) ** 2
        distance = (first_diff_square + second_diff_square) ** 0.5
        return self.fuel_price * self.car["fuel_consumption"] * distance / 100

    def find_cheapest_shop_and_print_info(self, shops):
        print(f"{self.name} has {self.money} dollars")
        the_cheapest = shops[0]
        for shop in shops:
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {shop.trip_to_shop(self)}")
            if shop.trip_to_shop(self) < the_cheapest.trip_to_shop(self):
                the_cheapest = shop
        if the_cheapest.trip_to_shop(self) > self.money:
            print(f"{self.name} doesn't have enough money "
                  f"to make purchase in any shop")
        else:
            print(f"{self.name} rides to {the_cheapest.name}\n")
            self.location = the_cheapest.location
            the_cheapest.purchase_receipt(self)
            print(f"{self.name} rides home")
            self.location = self.home_location
            self.money -= the_cheapest.trip_to_shop(self)
            print(f"{self.name} now has {self.money} dollars\n")
