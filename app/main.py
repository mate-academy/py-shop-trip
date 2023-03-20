import customer


def shop_trip() -> None:

    for client in customer.customer_list:
        print(f"{client.name} has {client.money} dollars.")

        shop, expenses = client.select_shop()

        if client.money < expenses:
            print(f"{client.name} doesn't have enough money "
                  f"to make purchase in any shop")
        else:
            print(f"{client.name} rides to {shop.name}\n")
            client.go_to_shop(shop)
        print()
