import datetime

from app.customer import Customer
from app.shop import Shop


def get_distance(shop: Shop, customer: Customer) -> float:
    shop = shop.location
    customer = customer.location
    dist = abs(
        (
            (shop[0] - customer[0]) ** 2
            + (shop[1] - customer[1]) ** 2) ** 0.5)
    return dist


def purchases(
        total: int,
        receipt: None,
        customer: Customer,
        shop: Shop) -> tuple:
    receipt = {} if receipt is None else receipt
    for product, quantity in customer.product_cart.items():
        price = shop.products[product] * quantity
        receipt[product] = quantity, price
        total += price
    return total, receipt


def get_receipt(
        receipt: None,
        customer: Customer,
        total: int | float = None) -> str:
    receipt = {} if receipt is None else receipt
    total = 0 if total is None else total
    time_now = datetime.datetime.now()
    time_now = time_now.strftime("%d/%m/%Y %H:%M:%S")
    res_list = ["Date: " + time_now]
    # Ugly indentations - because of flake8.
    res_list.append(
        f"Thanks, {customer.name}, for your purchase!\nYou have bought"
        ":"
    )
    for item in receipt:
        quantity = receipt[item][0]
        price = receipt[item][1]
        price = float(price)
        if price.is_integer():
            price = int(price)
        res_list.append(f"{quantity} {item}s for {price} dollars")
    res_list.append(f"Total cost is {total} dollars")
    res_list.append("See you again!")
    resulting_receipt = "\n".join(res_list)
    return resulting_receipt


if __name__ == "__main__":
    pass
