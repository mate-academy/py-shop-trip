
def sum_of_shopping(customer: dict, shop: dict, print_: bool = False) -> float:
    sum_ = 0
    for product, number in customer["product_cart"].items():
        cost = shop["products"][product] * number
        sum_ += cost
        if print_:
            print(f"{number} {product}s for {cost} dollars")
    if print_:
        print(f"Total cost is {sum_} dollars\n"
              f"See you again!\n")
    return sum_
