from app.customer import customers
from app.shop import shops
from app.Calculations.calculate_distance import calculate_distance
from app.Calculations.fuel_costs import prize_for_fuel


def shop_trip() -> None:
    for customer in customers():
        name = customer["name"]
        money = customer["money"]
        car = customer["car"]
        fuel_consumption = car["fuel_consumption"]
        location = customer["location"]
        cart = customer["product_cart"]

        print(f"{name} has {money} dollars")
        trip_costs = []

        for shop in shops():
            shop_name = shop["name"]
            shop_location = shop["location"]
            products = shop["products"]

            distance = calculate_distance(location, shop_location)
            fuel_cost = prize_for_fuel(distance, fuel_consumption)
            product_cost = 0

            for product, qty in cart.items():
                if product not in products:
                    break
                product_cost += products[product] * qty
            else:
                total_cost = fuel_cost * 2 + product_cost
                total_cost = int(total_cost) if \
                    total_cost == int(total_cost) \
                    else round(total_cost,
                               2)  # precise rounding
                trip_costs.append((total_cost,
                                   shop,
                                   product_cost,
                                   fuel_cost))
                print(f"{name}'s trip to the"
                      f" {shop_name} costs {total_cost}")

        if not trip_costs:
            print(f"{name} doesn't have enough"
                  f" money to make a purchase in any shop")
            continue

        trip_costs.sort(key=lambda x: x[0])
        (cheapest_cost, selected_shop,
         product_cost,
         fuel_cost) = trip_costs[0]

        if cheapest_cost > money:
            print(f"{name} doesn't have enough"
                  f" money to make a purchase in any shop")
            continue

        shop_name = selected_shop["name"]
        print(f"{name} rides to {shop_name}\n")
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")

        for product, qty in cart.items():
            price = selected_shop["products"][product]
            cost = qty * price
            cost = int(cost) if cost == int(cost) else round(cost, 2)
            print(f"{qty} {product}s for {cost} dollars")

        product_cost = int(product_cost) \
            if product_cost == int(product_cost) \
            else round(product_cost, 2)
        print(f"Total cost is {product_cost} dollars")
        print("See you again!\n")

        customer["location"] = selected_shop["location"]

        print(f"{name} rides home")

        remaining = money - cheapest_cost
        remaining = int(remaining) \
            if remaining == int(remaining) \
            else round(remaining, 2)
        print(f"{name} now has {remaining} dollars\n")
