import datetime


from app.customer import Customer
from app.shop import Shop
from app.data_processing import fuel_price


def get_fuel_cost(
        customer: Customer,
        second_point: list[int]
) -> float:
    distance = ((customer.location[0] - second_point[0]) ** 2
                + (customer.location[1] - second_point[1]) ** 2) ** 0.5
    customer.location = second_point
    fuel_cost = (fuel_price * distance
                 * customer.car.fuel_consumption / 100)

    return round(fuel_cost, 2)


def get_product_cost(
        customer: Customer,
        shop: Shop
) -> float:
    total_products_cost = 0
    products = customer.product_cart

    for product, number in products.items():
        products_cost = number * shop.product_cart[product]
        total_products_cost += products_cost

    return round(total_products_cost, 2)


def get_receipt(
        customer: Customer,
        shop: Shop
) -> None:
    print(f"Date: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n"
           f"Thanks, {customer.name}, for your purchase!\n"
           f"You have bought:")

    for product, number in customer.product_cart.items():
        products_cost = number * shop.product_cart[product]
        if products_cost % 1 == 0:
            products_cost = int(products_cost)
        print(f"{number} {product}s for {products_cost} dollars")

    total_product_cost = get_product_cost(customer, shop)
    print(f"Total cost is {total_product_cost} dollars\n"
          f"See you again!\n\n"
          f"{customer.name} rides home")
