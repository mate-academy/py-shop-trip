from app.shop import make_instances, open_file


def shop_trip() -> None:
    shops = make_instances(open_file("shops"))
    customers = make_instances(open_file("customers"))
    current = "04/01/2021 12:33:41"

    min_ = 1000000
    market = None
    cost = 0
    total_cost = 0
    for human in customers:
        print(f"{human.name} has {human.money} dollars")
        for store in shops:
            print(
                f"{human.name}'s trip to the {store.name} "
                f"costs {store.calculate_trip(human)}"
            )
            if store.calculate_trip(human) < min_:
                min_ = store.calculate_trip(human)
        if human.money > min_:
            for store in shops:
                if store.calculate_trip(human) == min_:
                    market = store
                    print(f"{human.name} rides to {store.name}\n")
            print(f"Date: {current}")
            print(f"Thanks, {human.name}, for you purchase!")
            print("You have bought: ")
            for prod, amt in human.product_cart.items():
                for product, price in market.products.items():
                    if prod == product:
                        cost = amt * price
                        total_cost += cost
                print(f"{amt} {prod}s for {cost} dollars")
                cost = 0
            print(f"Total cost is {total_cost} dollars")
            total_cost = 0
            print("See you again!\n")
            print(f"{human.name} rides home")
            print(
                f"{human.name} now has "
                f"{human.money - market.calculate_trip(human)}"
                f" dollars\n"
            )
        else:
            print(
                f"{human.name} doesn't have enough "
                f"money to make purchase in any shop"
            )


print(shop_trip())
