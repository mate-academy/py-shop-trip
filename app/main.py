from app.data_from_json import get_fuel_price, get_customers, get_shops


def shop_trip() -> None:
    options_of_trip_costs = {}
    for customer in get_customers():
        print(f"{customer.name} has {customer.money} dollars")
        for shop in get_shops():
            trip_costs = customer.fuel_costs(shop, get_fuel_price()) \
                + customer.products_costs(shop)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_costs}")
            options_of_trip_costs[trip_costs] = shop
        chosen_shop = options_of_trip_costs[min(options_of_trip_costs.keys())]
        if customer.money < min(options_of_trip_costs.keys()):
            print(f"{customer.name} doesn't have "
                  f"enough money to make purchase in any shop")
            break
        print(f"{customer.name} rides to {chosen_shop.name}\n")
        customer.shop_prints(chosen_shop)
        print(f"{customer.name} rides home")
        customer.money_after_shopping(chosen_shop, get_fuel_price())
