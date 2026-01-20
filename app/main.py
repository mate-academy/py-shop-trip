from typing import TYPE_CHECKING

from app.shop import ShopManager

if TYPE_CHECKING:
    from app.shop import Shop


def shop_trip() -> None:
    """
    Orchestrates the shopping trip simulation for all customers.

    For each customer, it calculates the cost of a trip to every shop,
    selects the cheapest option, and simulates the purchase if the
    customer has enough money.
    """
    shop_manager = ShopManager()
    fuel_price = shop_manager.fuel_price

    for customer in shop_manager.customers:
        print(f"{customer.name} has {customer.money} dollars")

        # Calculate trip costs for all available shops.
        trip_costs = customer.calculate_trip_cost(
            shop_manager.shops, fuel_price
        )

        for shop_name, cost, _ in trip_costs:
            print(
                f"{customer.name}'s trip to the "
                f"{shop_name} costs {round(cost, 2)}"
            )

        # If there are no trip options, continue to the next customer.
        if not trip_costs:
            print(f"No available shops for {customer.name}.")
            print()
            continue

        # Find the cheapest trip using min instead of sorting.
        cheapest_shop_name, cheapest_cost, shopping_cost = min(
            trip_costs, key=lambda item: item[1]
        )

        # Check if the customer can afford the cheapest trip.
        if customer.money < cheapest_cost:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
            continue

        # Simulate the trip and purchase.
        print(f"{customer.name} rides to {cheapest_shop_name}")
        print()

        # Find the chosen shop object.
        chosen_shop: "Shop" = next(
            s for s in shop_manager.shops if s.name == cheapest_shop_name
        )

        # Print the purchase receipt.
        chosen_shop.print_purchase_receipt(customer, shopping_cost)
        print()
        print(f"{customer.name} rides home")

        # Calculate remaining money and print the final status.
        final_money = customer.money - cheapest_cost
        print(f"{customer.name} now has {round(final_money, 2)} dollars")
        print()


if __name__ == "__main__":
    shop_trip()
