from app.create_report import create_config_report
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:

    report = create_config_report("app/config.json")
    customers_dict = report["customers"]
    shops_dict = report["shops"]
    Car.fuel_price = report["FUEL_PRICE"]

    list_of_shop_object = list()
    list_of_customer_object = list()

    for shop in shops_dict:
        list_of_shop_object.append(Shop(shop["name"],
                                        shop["location"],
                                        shop["products"]
                                        ))

    for customer_info in customers_dict:
        customer = Customer(customer_info["name"],
                            customer_info["product_cart"],
                            customer_info["location"],
                            customer_info["money"],
                            Car(customer_info["car"]["brand"],
                                customer_info["car"]["fuel_consumption"]
                                )
                            )
        list_of_customer_object.append(customer)

    for customer in list_of_customer_object:
        customer.print_customer_money_information()
        min_shop_cost = customer.summary_cost(list_of_shop_object[0])
        cheapest_trip = list_of_shop_object[0]

        for shop in list_of_shop_object:
            if min_shop_cost > customer.summary_cost(shop):
                cheapest_trip = shop
            customer.print_trips(shop)

        customer.shop_choice(cheapest_trip)
        if customer.is_ride_to_shop is False:
            continue

        else:
            customer.print_shop_information(cheapest_trip)
