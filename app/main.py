from app.customers import (
    customers,
    shops,
    distance,
    product_cost,
    fuel_cost_for_distance,
    bill_from_the_shop,
    format_output
)


def shop_trip() -> None:

    for customer in customers:
        data_shops = []
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            if not all(p in shop.products for p in customer.product_cart):
                continue

            dist_k = distance(customer.location, shop.location)

            fuel_cost = fuel_cost_for_distance(
                dist_k,
                customer.car.fuel_consumption
            )

            prod_cost = product_cost(
                customer.product_cart,
                shop.products
            )

            total_cost = fuel_cost * 2 + prod_cost

            data_shops.append((total_cost, shop))

            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {format_output(total_cost)}"

            )

        if not data_shops:
            continue

        best_cost, best_shop = min(data_shops, key=lambda x: x[0])

        if best_cost > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {best_shop.name}")

        customer.home = customer.location
        customer.location = best_shop.location

        bill_from_the_shop(customer, best_shop)

        print(f"{customer.name} rides home")

        customer.location = customer.home

        customer.money -= best_cost

        print(
            f"{customer.name} now has "
            f"{format_output(customer.money)} dollars\n"
        )
