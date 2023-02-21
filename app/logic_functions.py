from app.car import Car
from app.shop import Shop
from app.customer import Customer


def trip_calculator(shop: Shop, customer: Customer, fuel_price: float) -> dict:
    distance = Car.distance_calculator(
        shop.location, customer.location
    )

    costs_per_km = fuel_price * customer.car.fuel_consumption / 100

    purchased_products = Shop.make_purchased_products_list(
        customer_products=customer.product_cart,
        value=shop.products
    )

    products_total_price = (
        Shop.products_total_price_calculator(
            customer_products=customer.product_cart,
            value=shop.products
        )
    )

    full_costs_of_trip = round(
        distance * costs_per_km * 2 + products_total_price, 2
    )

    print(f"{customer.name}"
          f"'s trip to the {shop.name}"
          f" costs {full_costs_of_trip}"
          )

    return (
        {"full_costs_of_trip": full_costs_of_trip,
         "shop": shop,
         "purchased_products": purchased_products,
         "products_total_price": products_total_price
         }
    )


def start_trip(
        customers: dict[Customer],
        shops: dict[Shop],
        fuel_price: float
) -> None:
    costs_and_shops = []
    for customer_key in customers:
        print(f"{customers.get(customer_key).name} has "
              f"{customers.get(customer_key).money} dollars")

        for shop_key in shops:
            costs_and_shops.append(trip_calculator(
                shops[shop_key],
                customers.get(customer_key),
                fuel_price
            ))

        min_cost = min(
            item.get("full_costs_of_trip") for item in costs_and_shops
        )

        if Shop.price_vs_wallet_checker(
                min_cost,
                customers[customer_key].money,
                customers[customer_key].name
        ):
            continue

        cheapest_trip = [
            cheapest for cheapest in costs_and_shops if cheapest.get(
                "full_costs_of_trip"
            ) == min_cost][0]

        Customer.print_customer_trip(
            customers[customer_key],
            cheapest_trip,
            min_cost
        )
