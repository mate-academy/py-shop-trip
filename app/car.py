import math
from app.shop import Shop
from app.customer import Customer


class PriсeKm:
    def __init__(
            self, location_customer1: dict,
            fuel_consumption_car3: dict, priсe_fuel: float
    ) -> list:
        self.location_customer1 = location_customer1
        self.fuel_consumption_car3 = fuel_consumption_car3
        self.priсe_fuel = priсe_fuel

    def distance_priсe() -> dict:
        (location_customer1,
         fuel_consumption_car3,
         priсe_fuel) = Customer.customer_location()
        dict_priсe_ = []
        for number in location_customer1:
            coordinates_customer = location_customer1.get(number)
            fuel_consumption_car2 = fuel_consumption_car3.get(number)
            distance_custom_x = coordinates_customer[0]
            distance_custom_y = coordinates_customer[1]
            for vel in Shop.shop_location_shop():
                coordinates_shop = Shop.shop_location_shop().get(vel)
                distance_location_shop_x = coordinates_shop[0]
                distance_location_shop_y = coordinates_shop[1]
                distance = (
                    math.sqrt((distance_custom_x
                               - distance_location_shop_x) ** 2
                              + (distance_custom_y
                                 - distance_location_shop_y) ** 2)
                )
                priсe_distance = (
                    (distance
                        * 2 / 100)
                    * fuel_consumption_car2
                    * priсe_fuel
                )
                priсe_distance = round(priсe_distance, 2)
                dict_priсe_.append(priсe_distance)
        return dict_priсe_
