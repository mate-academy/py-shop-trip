from app.logic import prepare_for_shop_trip


def shop_trip() -> None:
    customers, shops = prepare_for_shop_trip()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        if selected_shop := customer.choose_shop_out_of(shops):
            customer.drive_to(selected_shop)
            customer.buy_products()
            customer.return_home()
            customer.check_wallet()
        else:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
