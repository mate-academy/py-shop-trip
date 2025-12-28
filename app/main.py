from app.customer import create_customers_list
from app.shop import create_shops_list


def shop_trip() -> None:
    for customer in create_customers_list():
        customer.check_money()
        cheapest_shop = [None, 100]
        for shop in create_shops_list():
            price_per_trip = customer.check_total_price_per_trip(shop)
            if cheapest_shop[1] > price_per_trip:
                cheapest_shop[1] = price_per_trip
                cheapest_shop[0] = shop
        if cheapest_shop[1] <= customer.money:
            customer.make_trip(cheapest_shop[0])
            cheapest_shop[0].sell_products(customer)
            customer.ride_home(cheapest_shop[1])
        else:
            customer.no_trip()
