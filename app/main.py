from app.extract_json import extract_json


def shop_trip() -> None:
    customers, shops, cost_of_fuel = extract_json("config.json")
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        whole_price = []
        for shop in shops:
            price_in_shop = shop.count_total_price(customer)
            trip_cost = (customer.car.price_for_km(cost_of_fuel)
                         * customer.calculate_distance_to_shop(shop.location))
            total_price = round(trip_cost * 2 + price_in_shop, 2)
            whole_price.append((shop, total_price))
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_price}")
        lowest_price_shop = min(whole_price, key=lambda x: x[1])

        if lowest_price_shop[1] <= customer.money:
            print(f"{customer.name} rides to {lowest_price_shop[0].name}")
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
            continue

        lowest_price_shop[0].sell_products(customer)

        print(f"{customer.name} rides home")
        customer.money -= lowest_price_shop[1]
        print(f"{customer.name} now has {customer.money} dollars")
