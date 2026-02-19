from __future__ import annotations

from typing import Dict, List, Optional, Tuple

from .car import Car
from .customer import Customer
from .shop import Shop
from .utils import load_config, money_fmt, money_trim, to_location


def shop_trip() -> None:
    """Run shop trip simulation."""
    config = load_config("config.json")
    fuel_price: float = float(config["FUEL_PRICE"])

    shops = _build_shops(config["shops"])
    customers = _build_customers(config["customers"])

    for customer in customers:
        _print_customer_header(customer)

        costs = _print_trip_costs(
            customer=customer,
            shops=shops,
            fuel_price=fuel_price,
        )

        best_shop = _best_shop_from_costs(shops, costs)

        if best_shop is None or not costs:
            _print_not_enough_money(customer.name)
            continue

        best_cost = costs[best_shop.name]

        if customer.money < best_cost:
            _print_not_enough_money(customer.name)
            continue

        print(f"{customer.name} rides to {best_shop.name}")

        customer.perform_purchase_trip(best_shop, best_cost)

        print(f"{customer.name} rides home")
        print(
            f"{customer.name} now has "
            f"{money_fmt(customer.money)} dollars\n"
        )


def _build_shops(raw_shops: List[dict]) -> Tuple[Shop, ...]:
    """Create Shop objects from raw config data."""
    shop_list: List[Shop] = []

    for raw_shop in raw_shops:
        products_map = {
            str(key): float(value)
            for key, value in raw_shop["products"].items()
        }

        shop_list.append(
            Shop(
                name=str(raw_shop["name"]),
                location=to_location(raw_shop["location"]),
                products=products_map,
            )
        )

    return tuple(shop_list)


def _build_customers(raw_customers: List[dict]) -> List[Customer]:
    """Create Customer objects from raw config data."""
    customers: List[Customer] = []

    for raw_customer in raw_customers:
        car_data = raw_customer["car"]

        car = Car(
            brand=str(car_data["brand"]),
            fuel_consumption=float(car_data["fuel_consumption"]),
        )

        cart_map = {
            str(key): int(value)
            for key, value in raw_customer["product_cart"].items()
        }

        customers.append(
            Customer(
                name=str(raw_customer["name"]),
                product_cart=cart_map,
                location=to_location(raw_customer["location"]),
                money=float(raw_customer["money"]),
                car=car,
            )
        )

    return customers


def _print_customer_header(customer: Customer) -> None:
    """Print first line for a customer."""
    print(
        f"{customer.name} has "
        f"{money_trim(customer.money)} dollars"
    )


def _print_trip_costs(
    customer: Customer,
    shops: Tuple[Shop, ...],
    fuel_price: float,
) -> Dict[str, float]:
    """Print trip cost for each valid shop and return shop->cost mapping."""
    costs: Dict[str, float] = {}

    for shop in shops:
        trip_cost = customer.trip_cost_to_shop(shop, fuel_price)
        if trip_cost is None:
            continue

        costs[shop.name] = trip_cost

        print(
            f"{customer.name}'s trip to the {shop.name} costs "
            f"{money_fmt(trip_cost)}"
        )

    return costs


def _best_shop_from_costs(
    shops: Tuple[Shop, ...],
    costs: Dict[str, float],
) -> Optional[Shop]:
    """Return the Shop with the minimal cost from a precomputed dict."""
    if not costs:
        return None

    best_name, _best_cost = min(
        costs.items(),
        key=lambda item: item[1],
    )

    for shop in shops:
        if shop.name == best_name:
            return shop

    return None


def _print_not_enough_money(customer_name: str) -> None:
    """Print standardized message for insufficient money."""
    print(
        f"{customer_name} doesn't have enough money to make a purchase "
        "in any shop"
    )
