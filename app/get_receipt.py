import datetime


def get_receipt(customer: dict, shop):
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    products = customer["product_cart"]
    items = shop["items"]

    print(f"Date: {date}\n"
          f"Thanks, {customer['name']}, for you purchase!\n"
          f"You have bought: \n"
          f"{products['milk']} milks for {items['milk']} dollars\n"
          f"{products['bread']} breads for {items['bread']} dollars\n"
          f"{products['butter']} butters for {items['butter']} dollars\n"
          f"Total cost is {shop['total_cost']} dollars\n"
          f"See you again!\n\n"
          f"{customer['name']} rides home\n"
          f"{customer['name']} now has {shop['money_left']} dollars\n")
