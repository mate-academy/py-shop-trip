def trip_cost(
        customer_loc: list,
        shop_loc: list,
        fuel_price: float,
        fuel_consump: float
) -> float:
    x1, y1, x2, y2 = customer_loc + shop_loc
    way = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round((way * fuel_price * (fuel_consump / 100)) * 2, 2)


def shopping_cost(num_to_buy: dict, prod_price: dict) -> float:
    costs = []
    prod_pack = {}
    for key in num_to_buy:
        if key in prod_price:
            result = num_to_buy[key] * prod_price[key]
            prod_pack[key] = [num_to_buy[key], result]
            costs.append(result)
    return [round(sum(costs), 2), prod_pack]


def shopping_start(
        name: str,
        budget: float,
        receipt: float,
        cost: float,
        shop: str,
        prod_pack: dict
) -> None:
    if budget > cost:
        print(
            f"{name} rides to {shop}\n\n"
            "Date: 04/01/2021 12:33:41\n"
            f"Thanks, {name}, for you purchase!\n"
            "You have bought: "
        )
        for product in prod_pack:
            print(
                f"{prod_pack[product][0]} {product}s"
                f" for {prod_pack[product][1]} dollars"
            )
        print(
            f"Total cost is {receipt} dollars\n"
            "See you again!\n\n"
            f"{name} rides home\n"
            f"{name} now has {budget - cost} dollars\n"
        )
    else:
        print(f"{name} doesn't have enough money"
              f" to make purchase in any shop")
