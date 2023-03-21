from app.customer import customer_list


def shop_trip() -> None:

    for client in customer_list:
        print(f"{client.name} has {client.money} dollars")

        shop_, expenses = client.select_shop()

        if client.money < expenses:
            print(f"{client.name} doesn't have enough money "
                  f"to make purchase in any shop")
        else:
            print(f"{client.name} rides to {shop_.name}\n")
            client.go_to_shop(shop_)
        print()


shop_trip()
