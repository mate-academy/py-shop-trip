from app.data import import_data_from_json
from app.data import calculate_distance
from app.data import calculate_trip_to_shop
from app.receipt import shopping_info


def shop_trip() -> None:
    fuel_price, customers, shops = import_data_from_json()
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        min_total_cost = float("inf")

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

            if total_cost_to_shop < min_total_cost:
                cheapest_shop = (shop, total_cost_to_shop, trip_to_shop)
                min_total_cost = total_cost_to_shop

        if cheapest_shop and customer.money >= cheapest_shop[1]:
            shopping_info(customer, cheapest_shop)
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")


shop_trip()
