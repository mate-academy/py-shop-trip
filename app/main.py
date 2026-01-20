from app.content import get_data_for_trip


def shop_trip() -> None:
    fuel_price, customers, shops = get_data_for_trip()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        the_cheapest_shop = min(
            (customer.calculate_shop_trip(shop, fuel_price) for shop in shops),
            key=lambda shop: shop.get("shop_trip_price")
        )
        if the_cheapest_shop.get("shop_trip_price") > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        shop = the_cheapest_shop.get("shop")
        customer.ride_to_the_shop(shop, fuel_price)
        shop.make_purchases(customer)
        customer.ride_to_the_home()
