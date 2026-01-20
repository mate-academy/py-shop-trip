import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as f:
        config_data = json.load(f)

    customers = [Customer.from_config(customer)
                 for customer in config_data["customers"]]
    shops = [Shop.from_config(shop)
             for shop in config_data["shops"]]
    fuel_price = config_data["FUEL_PRICE"]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_costs = {}
        for shop in shops:
            distance_to_shop = shop.calculate_distance_to_shop(customer)
            fuel_cost_to_shop = customer.calculate_fuel_cost_to_shop(
                distance_to_shop, fuel_price)

            product_cost = shop.calculate_product_cost(customer.product_cart)

            fuel_cost_to_home = fuel_cost_to_shop

            total_cost = round(fuel_cost_to_shop
                               + product_cost + fuel_cost_to_home, 2)
            trip_costs[shop.name] = total_cost
            print(f"{customer.name}'s trip"
                  f" to the {shop.name} costs {total_cost}")

        cheapest_shop_name = min(trip_costs, key=trip_costs.get)
        cheapest_shop = next((shop for shop in shops
                              if shop.name == cheapest_shop_name), None)

        if customer.money >= trip_costs[cheapest_shop_name]:
            print(f"{customer.name} rides to {cheapest_shop_name}")
            customer.location = cheapest_shop.location

            cheapest_shop.purchase_and_print_receipt(customer)
            print(f"\n{customer.name} rides home")
            customer.location = customer.location

            remaining_money = customer.money - trip_costs[cheapest_shop_name]
            print(f"{customer.name} now has {remaining_money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
