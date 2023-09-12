from app.customer import Customer
from app.shop import Shop


def check_shop_total_price(
        customer_products_cart: dict,
        products_in_shop: dict
) -> dict:
    shop_prices = {}

    for product_name, product_count in customer_products_cart.items():
        if product_name in products_in_shop.keys():
            product_price = products_in_shop[product_name]
            shop_prices[product_name] = product_count * product_price
    return {
        "shop_prices": shop_prices,
        "total_price": sum(shop_prices.values())
    }


def check_low_price_shop_for_customer(shops: list, customer: Customer) -> dict:
    lowest_price_shop = None
    lowest_shop_total_price = float("inf")

    for shop in shops:

        shop_products_price = check_shop_total_price(
            customer.product_cart,
            shop.products
        )
        shop_products_total_price = shop_products_price["total_price"]
        trip_cost = customer.calculate_trip_cost(shop.location) * 2
        total_price = shop_products_total_price + trip_cost
        if total_price < lowest_shop_total_price:
            lowest_price_shop = shop
            lowest_shop_total_price = total_price
    return {lowest_price_shop: lowest_shop_total_price}


def check_low_price_shops_for_customers(customers: list, shops: list) -> dict:
    prices_for_customers = {}

    for customer in customers:
        prices_for_customers[customer] = check_low_price_shop_for_customer(
            shops, customer
        )
    return prices_for_customers


def trip_and_total_shop_purchases_price_for_customer(
        customer: Customer, shop: Shop
) -> float:
    shop_product_prices = shop.get_product_prices(customer.product_cart)
    total_purchases_price = shop_product_prices["total_purchases_price"]
    trip_price = customer.calculate_trip_cost(shop.location) * 2
    total_price = total_purchases_price + trip_price
    return total_price


def print_trip_prices_for_customer(customer: Customer, shops: list) -> None:
    print(f"{customer.name} has {round(customer.money, 2)} dollars")
    for shop in shops:
        total_price = trip_and_total_shop_purchases_price_for_customer(
            customer, shop
        )
        print(f"{customer.name}'s trip to the {shop.name} "
              f"costs {round(total_price, 2)}")


def go_shopping(customers: list, shops: list) -> None:
    low_price_shop_for_customers = check_low_price_shops_for_customers(
        customers, shops
    )

    for customer, shop_info in low_price_shop_for_customers.items():
        for cheapest_shop, cheapest_price in shop_info.items():
            if customer.money >= cheapest_price:
                print_trip_prices_for_customer(customer, shops)
                customer.go_to_shop(cheapest_shop.name, cheapest_shop.location)
                cheapest_shop.sell_products(
                    customer.name, customer.product_cart
                )
                customer.make_purchases(cheapest_price)
                customer.go_home()
            else:
                print_trip_prices_for_customer(customer, shops)
                print(f"{customer.name} doesn't have enough money "
                      f"to make a purchase in any shop")
