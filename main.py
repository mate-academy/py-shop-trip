from app.config_loader import get_config_path, load_config
from app.config_parser import extract_config_values
from app.factories import create_customers, create_shops
from app.utils import format_money


def shop_trip() -> None:
    try:
        config_path = get_config_path()
        config = load_config(config_path)
        fuel_price, customers_data, shops_data = extract_config_values(config)
    except (RuntimeError, KeyError) as e:
        print(e)
        return

    customers = create_customers(customers_data)
    shops = create_shops(shops_data)

    for customer in customers:
        initial_cash = customer.count_cash()
        print(
            f"{customer.name} has {format_money(initial_cash)} dollars"
        )

        trip_costs = customer.calculate_trip_costs(shops, fuel_price)

        for shop, cost in trip_costs:
            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{format_money(cost)}"
            )

        affordable_shops = customer.find_affordable_shops(trip_costs)

        if not affordable_shops:
            print(
                f"{customer.name} doesn't have enough money to make "
                f"a purchase in any shop"
            )
            continue

        best_shop, total_cost = customer.choose_best_shop(affordable_shops)

        print(f"{customer.name} rides to {best_shop.name}\n")
        customer.travel_to(best_shop.location)
        customer.visit_shop(best_shop, total_cost)
        customer.travel_to(customer.start_location)

        print(f"{customer.name} rides home")

        cash = customer.count_cash()
        print(
            f"{customer.name} now has {format_money(cash)} dollars\n"
        )


if __name__ == "__main__":
    shop_trip()
