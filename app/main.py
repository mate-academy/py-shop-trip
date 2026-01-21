import datetime
from app.customer import Customer, customers
from app.shop import Shop, shops
from app.car import distance_cost


customers_list = [
    Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        customer["car"]
    ) for customer in customers]
shops_list = [
    Shop(
        shop["name"],
        shop["location"],
        shop["products"]
    ) for shop in shops]


def shop_trip() -> None:
    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        available_shops = [
            shop for shop in shops_list if shop.products_cost(customer) is not None
        ]

        trip_costs = {
            shop: distance_cost(customer, shop) + shop.products_cost(customer)
            for shop in available_shops
        }

        if not trip_costs:
            print(
                f"{customer.name} doesn't have enough money to make a purchase in any shop\n"
            )
            continue

        cheapest_shop = min(trip_costs, key=trip_costs.get)
        min_cost = trip_costs[cheapest_shop]

        for shop, cost in trip_costs.items():
            print(f"{customer.name}'s trip to the {shop.name} costs {cost:.2f}")

        if min_cost <= customer.money:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            home = customer.location
            customer.location = cheapest_shop.location
            date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {date}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product, quantity in customer.product_cart.items():
                line_cost = cheapest_shop.products[product] * quantity
                print(f"{quantity} {product}s for {line_cost:.2f} dollars")
            total_cost = cheapest_shop.products_cost(customer)
            print(f"Total cost is {total_cost:.2f} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            customer.location = home
            customer.money = customer.money - min_cost
            print(
                f"{customer.name} now has "
                f"{customer.money:.2f} dollars\n"
            )
        else:
            print(
                f"{customer.name} doesn't have "
                f"enough money to make a purchase in any shop"
            )

shop_trip()