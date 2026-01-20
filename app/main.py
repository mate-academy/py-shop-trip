from app import data_settings


def shop_trip() -> None:

    for customer in data_settings.customers_ls:
        print(f"{customer.name} has {customer.money} dollars")
        list_of_shops = {}
        for shop in data_settings.shops_ls:
            cost_of_distance = (customer.distance_to_shop(shop.location)
                                * customer.car["fuel_consumption"] / 100
                                * data_settings.fuel_price * 2)
            products_sum = shop.sum_cost_of_products(customer.products_to_buy)
            cost_of_trip = round(cost_of_distance + products_sum, 2)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {cost_of_trip}")
            list_of_shops.update({shop: cost_of_trip})

        customer.select_shop_and_trip(list_of_shops)
