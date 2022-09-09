def product_calculation(count_milk: int,
                        count_bread: int,
                        count_butter: int,
                        shop):
    total_amount = {
        "milk": count_milk * shop["products"]["milk"],
        "bread": count_bread * shop["products"]["bread"],
        "butter": count_butter * shop["products"]["butter"]
    }
    milk = total_amount["milk"]
    bread = total_amount["bread"]
    butter = total_amount["butter"]
    return milk + bread + butter


def product_calculation_print(count_milk: int,
                              count_bread: int,
                              count_butter: int,
                              shop):
    total_amount = {
        "milk": count_milk * shop["products"]["milk"],
        "bread": count_bread * shop["products"]["bread"],
        "butter": count_butter * shop["products"]["butter"]
    }

    print(f'{count_milk} milks for {total_amount["milk"]} dollars')
    print(f'{count_bread} milks for {total_amount["bread"]} dollars')
    print(f'{count_butter} milks for {total_amount["butter"]} dollars')

    milk = total_amount["milk"]
    bread = total_amount["bread"]
    butter = total_amount["butter"]
    total_cost = milk + bread + butter
    print(f'Total cost is {total_cost} dollars')
