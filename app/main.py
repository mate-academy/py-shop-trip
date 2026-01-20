from app.customer import Customer, config
from app.shop import Shop


def shop_trip() -> None:

    customers = [Customer(**customer) for customer in config["customers"]]
    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = None
        best_price = float("inf")

        for shop in shops:
            trip_cost = customer.trip_cost(shop)
            total_cost = sum(shop.products.get(product,
                                               float("inf")) * quantity
                             for product, quantity in
                             customer.product_cart.items())
            total_trip_cost = trip_cost + total_cost

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_trip_cost}")

            if total_trip_cost < best_price and customer.can_afford(shop):
                best_shop = shop
                best_price = total_trip_cost

        if best_shop:
            customer.buy_products(best_shop)
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
