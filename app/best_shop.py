import datetime


def locate_and_buy_in_the_best_shop(
        customers: list,
        shops: list,
        fuel_price: float) -> None:
    for customer in customers:
        print(f"{customer.name} has "
              f"{customer.money} dollars")

        best_shop = None
        best_cost = float("inf")
        home_location = customer.location

        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {cost}")
            if cost < best_cost:
                best_cost = cost
                best_shop = shop

        if customer.money > best_cost:
            total_shop_cost = []
            print(f"{customer.name} rides to {best_shop.name}\n")
            customer.location = best_shop.location
            date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {date}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for prod, qty in customer.product_cart.items():
                price = round(qty * best_shop.products[prod], 2)
                if price.is_integer():
                    pretty = int(price)
                    print(f"{qty} {prod}s for {pretty} dollars")
                else:
                    print(f"{qty} {prod}s for {price} dollars")
                total_shop_cost.append(price)
            print(f"Total cost is {round(sum(total_shop_cost), 2)} dollars")
            print("See you again!\n")
            customer.location = home_location
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{round(customer.money - best_cost, 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't have "
                  "enough money to make a purchase in any shop")
