from app.customers import customers
from app.shops import shops
from app.fuel import fuel_price


def shop_trip() -> None:
    for customer in customers.values():
        print(f"{customer.name} has {customer.money} dollars")
        trip = customer.calculate_trip_fuel(shops, fuel_price)
        prices = customer.calculate_trip_products(shops)
        sum_of_shopping_with_fuel = (
            customer.calc_sum_price_with_fuel
            (prices, trip)
        )
        store_we_go_to = (
            customer.calc_cheapest
            (sum_of_shopping_with_fuel)
        )

        cheapest_shop_name = next(iter(store_we_go_to.values()))
        cheapest_cost = next(iter(store_we_go_to))

        for shop, cost in sum_of_shopping_with_fuel.items():
            print(f"{customer.name}'s trip to the {shop} costs {cost:.2f}")

        if customer.money > cheapest_shop_name:
            print(
                f"{customer.name} rides to "
                f"{cheapest_cost}"
            )
            location_home = customer.location
            customer.location = shops[cheapest_cost].location

            print()

            customer.receipt(prices, cheapest_cost)

            print()

            print(f"{customer.name} rides home")
            customer.location = location_home

            remaining_money = (
                customer.money
                - cheapest_shop_name
            )
            print(f"{customer.name} now has {remaining_money:.2f} dollars")

            print()
        else:
            print(
                f"{customer.name} doesn't have enough "
                "money to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
