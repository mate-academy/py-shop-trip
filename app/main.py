from app import config_from_json


def shop_trip() -> None:
    (
        fuel_price,
        customers,
        shops
    ) = config_from_json.unpack_json("app/config.json")
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop, total_cost = None, None
        for shop in shops:
            cost = customer.full_price_for_shopping(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
            if total_cost is None or cost < total_cost:
                total_cost = cost
                best_shop = shop
        if total_cost < customer.money:
            customer.money -= total_cost
            print(f"{customer.name} rides to {best_shop.name}\n")
            customer.print_receipt(best_shop)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
            continue
