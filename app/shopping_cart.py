def shopping_cart_count(store_products: dict, customer_list: dict):
    price = 0
    for product, quantity in customer_list.items():
        price += quantity * store_products[product]
    return price


def shopping_cart(store_products: dict, customer_list: dict):
    print("You have bought: ")
    for product, quantity in customer_list.items():
        price = quantity * store_products[product]
        print(f"{quantity} {product}s for {price} dollars")
