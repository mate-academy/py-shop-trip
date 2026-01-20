from app.tools import load_data


def shop_trip() -> None:
    (customers, shops) = load_data("app/config.json")

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        customer.choose_shop(shops)
        if customer.best_shop is not None:
            customer.best_shop["link"].purhase(customer.name,
                                               customer.product_cart)
            customer.money -= customer.best_shop["cost"]
            print(f"{customer.name} rides home\n{customer.name} "
                  f"now has {customer.money} dollars\n")


if __name__ == "__main__":
    shop_trip()
