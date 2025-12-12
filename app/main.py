from app.data_loader import load_data, build_objects


def shop_trip() -> None:
    data = load_data()
    fuel_price, customers, shops = build_objects(data)

    for customer in customers:
        print(f"{customer.name} has {customer.money:g} dollars")

        for shop in shops:
            total = customer.trip_total_cost(shop, fuel_price)
            if total is None:
                continue
            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{total:.2f}"
            )

        best = customer.choose_best_shop(shops, fuel_price)

        if best is None or not customer.can_afford(best[1]):
            print(
                f"{customer.name} doesn't have enough money to "
                f"make a purchase in any shop"
            )
            continue

        best_shop, best_cost = best
        customer.ride_to(best_shop)
        best_shop.print_receipt(customer.name, customer.product_cart)
        customer.pay(best_cost)
        customer.ride_home()
        print(f"{customer.name} now has {customer.money:.2f} dollars")
        print()
