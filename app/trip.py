import math
from app.customer import Customer
from app.shop import Shop


class Trip:
    def __init__(self,
                 customer: Customer,
                 shop: Shop,
                 fuel_price: float) -> None:
        self.shop = shop
        self.trip_name = shop.name
        self.__get_cost_of_products(shop.products,
                                    customer.product_cart)
        self.__get_distance(shop.location,
                            customer.location)
        self.__get_fuel_cost(fuel_price,
                             customer.car.fuel_consumption)
        self.__get_trip_cost()

    def __get_cost_of_products(self,
                               product_in_shop: dict,
                               costumer_product_cart: dict) -> None:
        self.sum_of_product_price = 0
        for product in costumer_product_cart:
            quantity = costumer_product_cart[product]
            self.sum_of_product_price += product_in_shop[product] * quantity

    def __get_distance(self,
                       shop_location: list[int],
                       customer_location: list[int]) -> None:
        x_var = (customer_location[0] - shop_location[0]) ** 2
        y_var = (customer_location[1] - shop_location[1]) ** 2
        self.distance = math.sqrt(x_var + y_var)

    def __get_fuel_cost(self,
                        fuel_price: float,
                        fuel_consumption: float) -> None:
        self.fuel_cost = ((fuel_consumption / 100)
                          * fuel_price * self.distance) * 2

    def __get_trip_cost(self) -> None:
        self.trip_cost = round(self.sum_of_product_price + self.fuel_cost, 2)

    def __str__(self) -> str:
        return f"trip to the {self.trip_name} costs {self.trip_cost}"
