import math
from app.shop import Shop
from app.customer import Customer
from app.customer import customers_and_content


class PriсeKm:
    def __init__(self, customer: Customer) -> list:
        self.location_customer = customer.location_customer

    def distance_priсe() -> list:
        dict_priсe_ = []
        (
            location_customer,
            fuel_consumption_car,
            priсe_fuel,
            product_cart,
            money_custom,
            name_customer
        ) = Customer.customer_location()
        for name_cust in name_customer:
            coordinates_customer = location_customer.get(name_cust)
            fuel_consumption_car_ = fuel_consumption_car.get(name_cust)
            distance_custom_x = coordinates_customer[0]
            distance_custom_y = coordinates_customer[1]
            customers, content = customers_and_content()
            shops = content.get("shops")
            for element in shops:
                name_shop_element = element.get("name")
                location_shop_ = element.get("location")
                product_shop_ = element.get("products")
                shop = Shop(
                    element,
                    name_shop_element,
                    location_shop_,
                    product_shop_
                )
                coordinates_shop = shop.location_shop_
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
                    * fuel_consumption_car_
                    * priсe_fuel
                )
                priсe_distance = round(priсe_distance, 2)
                dict_priсe_.append(priсe_distance)
        return dict_priсe_
