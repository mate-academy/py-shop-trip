from app.functions import (
    get_dict_from_json,
    trip,
    costs_value,
)


def shop_trip() -> None:
    data = get_dict_from_json()
    customers = data["customers"]
    shops = data["shops"]

    for customer in customers:
        # amount of money
        print(f"{customer.name} has "
              f"{customer.money} dollars")

        products = customer.product_cart.keys()
        # path cost calculation
        costs = costs_value(shops, customer, products)
        shop_min_cost = "".join(
            ([k for k, v in costs.items() if v == min(costs.values())])
        )

        for shop in shops:
            if shop.name == shop_min_cost:
                selected_shop = shop

        trip(costs, customer, selected_shop, products)
