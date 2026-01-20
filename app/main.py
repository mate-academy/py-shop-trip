from app.information_unpacker import unpacking


def shop_trip() -> None:
    customers, shops, fuel_price = unpacking("app/config.json")
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cost_trips = [
            (
                shop, shop.total_cost_trip(customer, fuel_price)
            )
            for shop in shops
        ]
        cheap_trip = None
        for cost_trip in cost_trips:
            print(f"{customer.name}'s trip to "
                  f"the {cost_trip[0].name} costs {cost_trip[1]}")
            cheap_trip = (cost_trip
                          if cheap_trip is None or cost_trip[1] < cheap_trip[1]
                          else cheap_trip)
        if customer.money < cheap_trip[1]:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")
            break
        print(f"{customer.name} rides to {cheap_trip[0].name}\n")
        cheap_trip[0].purchase(customer)
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has "
              f"{customer.money - cheap_trip[1]} dollars\n")
