import datetime

from app import data_loader, general_calculations


def shop_trip() -> None:
    fuel_price, customers, shops = data_loader.load_data()

    for person in customers:
        print(f"{person.name} has {person.money} dollars")
        shops_cost = {}
        home_location = person.location.copy()
        for place in shops:
            distance = (general_calculations.calculate_distance
                        (person.location, place.location))
            products_cost = (person.calculate_product_cost
                             (place.products))
            ride_cost = round(person.transport.calculate_ride_cost
                              (distance, fuel_price) * 2, 2)
            total_cost = products_cost + ride_cost
            shops_cost[place] = total_cost
            print(f"{person.name}'s "
                  f"trip to the {place.name} "
                  f"costs {total_cost}")
        if not any(person.is_enough_money(total)
                   for total in shops_cost.values()):
            print(f"{person.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue
        cheapest_shop = min(shops_cost.items(), key=lambda item: item[1])
        print(f"{person.name} rides to {str(cheapest_shop[0].name)}\n")
        person.location = cheapest_shop[0].location
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {person.name}, for your purchase!")
        print("You have bought:")
        total_for_products = 0
        for product, quantity in person.product_cart.items():
            print(f"{quantity} {product}s "
                  f"for {quantity * cheapest_shop[0].products[product]:g} "
                  f"dollars")
            total_for_products += quantity * cheapest_shop[0].products[product]
        print(f"Total cost is {total_for_products} dollars")
        print("See you again!")
        print()
        print(f"{person.name} rides home")
        person.location = home_location
        print(f"{person.name} now has "
              f"{person.money - cheapest_shop[1]} dollars")
        print()
