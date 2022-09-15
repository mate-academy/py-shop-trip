def shopping_cart_count(store_products: dict, customer_list: dict):
    price = 0
    for key, value in customer_list.items():
        price += value * store_products[key]
    return price


def shopping_cart(store_products: dict, customer_list: dict):
    print("You have bought: ")
    for key, value in customer_list.items():
        price = value * store_products[key]
        print(f"{value} {key}s for {price} dollars")
