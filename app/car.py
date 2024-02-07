class Car:
    @staticmethod
    def count_distance(
            customer_location: list[int, int],
            shop_location: list[int, int]
    ) -> float:
        customer_x, customer_y = customer_location
        shop_x, shop_y = shop_location
        distance = ((customer_x - shop_x) ** 2
                    + (customer_y - shop_y) ** 2) ** 0.5
        return distance

    @staticmethod
    def count_amount_full_of_fuel(
            distance: float,
            fuel_consumption: int | float,
            fuel_price: int | float
    ) -> int | float:
        amount_of_fuel = (distance * fuel_consumption / 100) * 2
        price_in_both_sides = round(amount_of_fuel * fuel_price, 2)
        return price_in_both_sides

    @staticmethod
    def go_home(
            customer_name: str,
            customer_money: int | float
    ) -> None:
        print(f"{customer_name} rides home\n"
              f"{customer_name} now has {customer_money} dollars\n")
