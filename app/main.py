from app.data import import_data_from_json
from app.data import calculate_distance
from app.data import calculate_trip_to_shop
from app.shopping_info import shopping_info


def shop_trip() -> None:
    fuel_price, customers, shops = import_data_from_json()
    for customer in customers:
        cheapest_shop = []
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            cost_of_distance_to_shop = calculate_distance(
                customer.location,
                shop.location,
                fuel_price,
                customer.car.fuel_consumption
            )
            trip_to_shop = calculate_trip_to_shop(
                customer.product_cart,
                shop.products)
            total_cost_to_shop = round(
                trip_to_shop + cost_of_distance_to_shop, 2)
            print(f"{customer.name}'s trip to the"
                  f" {shop.name} costs {total_cost_to_shop}")
            cheapest_shop.append([
                shop,
                total_cost_to_shop,
                trip_to_shop])
        cheapest_shop = min(cheapest_shop, key=lambda x: x[1])
        if customer.money >= cheapest_shop[1]:
            shopping_info(customer, cheapest_shop)
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")


shop_trip()
