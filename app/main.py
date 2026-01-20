from app.config_utils import parse_info_from_json


def shop_trip() -> None:
    fuel_price, customers, shops = parse_info_from_json()
    for customer in customers:
        print(customer)
        costs_per_shop = {}
        for shop in shops:
            if not all(k in shop.products for k in customer.product_cart):
                continue
            shop_costs = customer.total_cost_for_shop(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {shop_costs:.2f}")
            costs_per_shop[shop.name] = shop_costs
        if not costs_per_shop:
            print(f"{customer.name} cannot make a purchase in any shop "
                  f"(missing products everywhere)")
            print("")
            continue
        min_shop_name = min(costs_per_shop, key=costs_per_shop.get)
        if customer.money < costs_per_shop[min_shop_name]:
            print(f"{customer.name} doesn't have enough money to make "
                  f"a purchase in any shop")
            continue
        print(f"{customer.name} rides to {min_shop_name}")
        print("")
        min_shop_obj = next(shop for shop in shops if
                            shop.name == min_shop_name)
        customer.ride_to_shop(min_shop_obj)
        customer.money -= costs_per_shop.get(min_shop_name)
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money:.2f} dollars")
        customer.location = customer.home_location
        print("")
