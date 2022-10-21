import math
from datetime import datetime
from app.customer import Customer
from app.shop import Shop


def count_trip_distance(client: Customer,
                        shop: Shop,
                        fuel_price: float) -> float:
    trip_road_distance = math.dist(client.location,
                                   shop.location) * 2
    one_km_cost = client.car.fuel_consumption * fuel_price / 100
    trip_price = trip_road_distance * one_km_cost
    return round(trip_price, 2)


def goods_price_counting(get_client: Customer, get_shop: Shop) -> float:
    total = []
    for product_name in get_client.product_cart:
        if product_name in get_shop.products:
            product_client = get_client.product_cart.get(product_name)
            product_shop = get_shop.products.get(product_name)
            total.append(product_client * product_shop)
    return sum(total)


def shop_bill(shop_client: Customer,
              shop: str,
              shops: list
              ) -> None:
    now = datetime(2021, 1, 4, 12, 33, 41)
    date_today = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {date_today}")
    print(f"Thanks, {shop_client.name}, for you purchase!")
    print("You have bought: ")
    shop_price = [name.products for name in shops if name.store == shop]
    sum_shopping = []
    for product_name in shop_client.product_cart:
        quantity = shop_client.product_cart.get(product_name)
        price = shop_price[0].get(product_name) * quantity
        sum_shopping.append(price)
        if quantity > 1:
            product_name = product_name + "s"
        print(f"{quantity} {product_name} for {price} dollars")
    print(f"Total cost is {sum(sum_shopping)} dollars")
    print("See you again!\n")
    print(f"{shop_client.name} rides home")
