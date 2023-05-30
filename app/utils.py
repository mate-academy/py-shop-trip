import math
from decimal import Decimal, ROUND_DOWN
from datetime import datetime
from app.customer import Customer
from app.shop import Shop


def remove_trailing_zeros(num):
    str_num = str(num)
    if '.' in str_num:
        str_num = str_num.rstrip('0').rstrip('.')
    if str_num.isdigit():
        return int(str_num)
    else:
        return float(str_num)


def fuel_cost(customer: Customer, shop: Shop, fuel_price) -> Decimal:
    fuel_consumption = Decimal(customer.car["fuel_consumption"])
    cost_of_fuel = Decimal(0)
    customer_location = customer.location
    shop_location = shop.location
    distance_to_shop = Decimal(
        math.sqrt((shop_location[0] - customer_location[0]) ** 2 + (shop_location[1] - customer_location[1]) ** 2))
    cost_of_fuel += Decimal(2) * distance_to_shop * (fuel_consumption / Decimal(100)) * Decimal(fuel_price)

    cost_of_fuel = cost_of_fuel.quantize(Decimal('0.00'),
                                         rounding=ROUND_DOWN)
    return cost_of_fuel


def cheapest_shop(customer: Customer, shops: list[Shop], fuel_price):
    total_cost = float('inf')
    selected_shop = None

    for shop in shops:
        cost = the_cost_of_shopping(customer, shop, fuel_price)
        print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
        if cost < total_cost:
            total_cost = cost
            selected_shop = shop

    if total_cost > customer.money:
        print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
        return None
    else:
        customer.location = selected_shop.location
        print(f"{customer.name} rides to {selected_shop.name}")
        return selected_shop


def the_cost_of_shopping(customer: Customer, shop: Shop, fuel_price) -> Decimal:
    cost = Decimal(0)

    for product, quantity in customer.product_cart.items():
        price = Decimal(shop.products[product])
        subtotal = price * quantity
        cost += subtotal

    cost += fuel_cost(customer, shop, fuel_price)

    cost = cost.quantize(Decimal('0.00'),
                         rounding=ROUND_DOWN)
    return cost


def calculate_total_cost(customer: Customer, shop: Shop):
    total_cost = Decimal(0)
    output = f"\nDate: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}\nThanks," \
             f" {customer.name}, for your purchase!\nYou have bought:\n"

    for product, quantity in customer.product_cart.items():
        if product in shop.products:
            price = Decimal(shop.products[product])
            cost = price * Decimal(quantity)
            total_cost += cost
            output += f"{quantity} {product}s for {remove_trailing_zeros(cost)} dollars\n"

    total_cost = total_cost.quantize(Decimal('.01'), rounding=ROUND_DOWN)
    output += f"Total cost is {remove_trailing_zeros(total_cost)} dollars\nSee you again!"
    print(output)


def cash_balance(customer: Customer, shop: Shop, fuel_price) -> None:
    cost_of_shopping = the_cost_of_shopping(customer, shop, fuel_price)
    cost_of_fuel = fuel_cost(customer, shop, fuel_price)
    customer_balance = Decimal(customer.money) - Decimal(cost_of_shopping) - Decimal(cost_of_fuel)
    customer_balance = customer_balance.quantize(Decimal('.01'), rounding=ROUND_DOWN)
    print(f"\n{customer.name} rides home\n{customer.name} now has {remove_trailing_zeros(customer_balance)} dollars\n")
