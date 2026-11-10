from app.models.customer.customer import Customer
from app.models.shop.shop import Shop
from app.models.shop.shopping_result import ShoppingResult


def calculate_customer_shopping_results(
        customers: list[Customer],
        shops: list[Shop],
        fuel_price: int | float
) -> list[ShoppingResult]:
    shopping_results: list[ShoppingResult] = []

    for customer in customers:
        name, money = customer.get_money_info()

        (
            shopping_options,
            lowest_total_cost_shop,
            money_after_purchase,
        ) = evaluate_shopping_options(shops, customer, money, fuel_price)

        result = ShoppingResult(
            customer=customer,
            shopping_options=shopping_options,
            lowest_total_cost_shop=lowest_total_cost_shop,
            money_after_purchase=money_after_purchase,
        )
        shopping_results.append(result)

    return shopping_results


def evaluate_shopping_options(
        shops: list[Shop],
        customer: Customer,
        money: int | float,
        fuel_price: int | float
) -> tuple[dict[str, int | float], Shop | None, int | float]:
    costs_for_possible_shops = {}
    lowest_total_cost_shop = None
    money_after_purchase = 0
    current_cheapest_cost = float("inf")

    for shop in shops:
        distance_to_shop = customer.distance_to_shop(shop)

        fuel_cost = customer.car.calculate_round_trip_fuel_cost(
            distance_to_shop, fuel_price
        )

        shopping_cost = customer.calculate_shopping_cost(shop)

        shopping_and_trip_cost = customer.calculate_shopping_trip(
            fuel_cost, shopping_cost
        )

        costs_for_possible_shops[shop.name] = shopping_and_trip_cost

        if shopping_and_trip_cost < current_cheapest_cost:
            current_cheapest_cost = shopping_and_trip_cost
            money_after_purchase = money - current_cheapest_cost

            if money >= current_cheapest_cost:
                lowest_total_cost_shop = shop

    return (
        costs_for_possible_shops,
        lowest_total_cost_shop,
        money_after_purchase
    )
