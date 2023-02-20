from app.customers import Customer
from app.shop import Shop


def shop_trip() -> None:
    for customer in Customer.create_customer():
        customer.print_customers_money()
        cost_list = {}
        product_cost = {}
        for shop in Shop.create_shop():
            trip_cost = (shop.distance_cost(customer, customer.car)
                         + shop.product_costs(customer))
            print(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}"
            )
            cost_list[shop.name] = trip_cost
            product_cost[shop.name] = shop.product_costs(customer)

        min_trip_cost = min(cost_list.values())
        cheap_shop = min(cost_list, key=cost_list.get)

        if customer.money < min_trip_cost:
            print(f"{customer.name} doesn't have enough money to make purchase"
                  f" in any shop")
        else:
            print(
                f"{customer.name} rides to {cheap_shop}\n"
                "\nDate: 04/01/2021 12:33:41\n"
                f"Thanks, {customer.name}, for you purchase!\n"
                "You have bought: "
            )

            for shop in Shop.create_shop():
                if shop.name == cheap_shop:
                    shop.print_purchase(customer)

            print(
                f"Total cost is {product_cost[cheap_shop]} dollars\n"
                "See you again!\n"
                f"\n{customer.name} rides home\n"
                f"{customer.name} now has {customer.money - min_trip_cost} "
                f"dollars\n"
            )
