import math
from app.shop import Shop
from app.customer import Customer


class PriсeKm:
    def __init__(self, customer: Customer) -> list:
        self.location_customer1 = customer.location_customer1

    def distance_priсe() -> dict:
        dict_priсe_ = []
        (
            location_customer1,
            fuel_consumption_car3,
            priсe_fuel,
            product_cart3,
            money_custom,
            name_customer
        ) = Customer.customer_location()
        for name_cust in name_customer:
            coordinates_customer = location_customer1.get(name_cust)
            fuel_consumption_car2 = fuel_consumption_car3.get(name_cust)
            distance_custom_x = coordinates_customer[0]
            distance_custom_y = coordinates_customer[1]
            location_shop, name_shop, product_shop = Shop.shop_location_shop()
            for name_shop_element in name_shop:
                coordinates_shop = location_shop.get(name_shop_element)
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
