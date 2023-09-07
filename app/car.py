import math
from app.shop import Shop
from app.customer import Customer
from app.customer import customers_and_content


class PriсeKm:
    def __init__(self, customer: Customer) -> list:
        self.location_customer = customer.location_customer

    def distance_priсe() -> list:
        customers, content = customers_and_content()
        dict_priсe_ = []
        customer = content.get("customers")
        customer_instances = []
        for name_custom in customer:
            money_custom = name_custom.get("money")
            product_cart = name_custom.get("product_cart")
            priсe_fuel = content.get("FUEL_PRICE")
            fuel_consumption_car = (
                name_custom.get("car").get("fuel_consumption")
            )
            location_customer = name_custom.get("location")
            name_customer = name_custom.get("name")
            customer_instance = Customer(
                location_customer,
                fuel_consumption_car,
                priсe_fuel,
                product_cart,
                money_custom,
                name_customer
            )
            customer_instances.append(customer_instance)
            distance_custom_x = location_customer[0]
            distance_custom_y = location_customer[1]
            customers, content = customers_and_content()
            shops = content.get("shops")
            for element in shops:
                name = element.get("name")
                location = element.get("location")
                product = element.get("products")
                shop = Shop(
                    name,
                    location,
                    product
                )
                coordinates_shop = shop.location
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
                    * fuel_consumption_car
                    * priсe_fuel
                )
                priсe_distance = round(priсe_distance, 2)
                dict_priсe_.append(priсe_distance)
        return dict_priсe_
