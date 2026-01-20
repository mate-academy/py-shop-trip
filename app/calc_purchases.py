def calc_purchases(product_cart: dict, products: dict):
    sum_of_products = 0
    for product in product_cart.keys():
        product_cost = product_cart[product] * products[product]
        sum_of_products += product_cost
    return sum_of_products


def shop_products(shops: list, name_of_shop) -> dict:
    for shop in shops:
        if shop["name"] == name_of_shop:
            return shop["products"]


def print_bought_products(product_cart: dict, products: dict):
    print("You have bought: ")
    sum_of_products = 0
    for product in product_cart.keys():
        product_cost = product_cart[product] * products[product]
        print(
            f"{product_cart[product]} {product}s for {product_cost} dollars")
        sum_of_products += product_cost
    print(f"Total cost is {sum_of_products} dollars")
    print("See you again!\n")
