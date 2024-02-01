from app.information_unpacker import unpacker


def shop_trip() -> None:
    customers, shops, fuel_price = unpacker("app/config.json")
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cost_trips = [
            [
                shop, round((customer.road_cost(shop.location, fuel_price)
                             * 2 + shop.cost_cart(customer.product_cart)), 2)
            ]
            for shop in shops
        ]
        cheap_trip = cost_trips[0]
        for cost_trip in cost_trips:
            print(f"{customer.name}'s trip to "
                  f"the {cost_trip[0].name} costs {cost_trip[1]}")
            cheap_trip = (cost_trip
                          if cost_trip[1] < cheap_trip[1] else cheap_trip)
        if customer.money < cheap_trip[1]:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")
            break
        print(f"{customer.name} rides to {cheap_trip[0].name}\n")
        cheap_trip[0].purchase(customer)
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has "
              f"{customer.money - cheap_trip[1]} dollars\n")
