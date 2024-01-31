from app.information_unpacker import unpacker


def shop_trip() -> None:
    customers, shops, fuel_price = unpacker("D:/py-shop-trip/app/config.json")
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cost_trip = [shops[0], 100]
        for shop in shops:
            road_cost = round((customer.road_cost(shop.location, fuel_price)
                               * 2 + shop.cost_cart(customer.product_cart)), 2)
            cost_trip = ([shop, road_cost]
                         if road_cost < cost_trip[1] else cost_trip)
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {road_cost}")
        if customer.money < cost_trip[1]:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")
            break
        print(f"{customer.name} rides to {cost_trip[0].name}\n")
        cost_trip[0].purchase(customer)
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has "
              f"{customer.money - cost_trip[1]} dollars\n")
