from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int, int],
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def customer_trip_to_shop(
            self,
            shop_list: list[Shop],
            info_in_file: dict
    ) -> bool:
        has_money = False
        for shop in range(len(shop_list)):
            car = Car(self.car["fuel_consumption"],
                      info_in_file["FUEL_PRICE"],
                      shop_list[shop],
                      self.location)
            temper_result = shop_list[shop].get_spent_money(
                self,
                car.get_fuel_cost(),
                True
            )
            if temper_result < self.money:
                has_money = True
        if has_money is False:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return False
        return True

    def show_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def show_cost_to_shop(
            self,
            shop: Shop,
            fuel_price: float | int
    ) -> int | float:
        get_car = Car(
            self.car["brand"],
            self.location,
            self.car["fuel_consumption"],
            fuel_price
        )
        return get_car.get_cost_trip(shop["location"])
