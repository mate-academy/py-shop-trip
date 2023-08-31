import math
from app.shop import Shop
from app.customer import Customer


class PriсeKm:
    def __init__(self, customer: Customer) -> list:
        self.location_customer1 = customer.location_customer1
        self.fuel_consumption_car3 = customer.fuel_consumption_car3
        self.priсe_fuel = customer.priсe_fuel

    def distance_priсe() -> dict:
        dict_priсe_ = []
        (
            location_customer1,
            fuel_consumption_car3,
            priсe_fuel,
            product_cart3,
            money_costum,
            name_custom
        ) = Customer.customer_location()
        for number in location_customer1:
            coordinates_customer = location_customer1.get(number)
            fuel_consumption_car2 = fuel_consumption_car3.get(number)
            distance_custom_x = coordinates_customer[0]
            distance_custom_y = coordinates_customer[1]
            location_shop, name_shop, product_shop = Shop.shop_location_shop()
            for vel in location_shop:
                coordinates_shop = location_shop.get(vel)
            #    print(coordinates_shop)
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
