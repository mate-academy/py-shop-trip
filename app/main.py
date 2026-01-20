from app.read_from_json_file import read_json_file


def shop_trip() -> None:
    customers, shops, fuel_price = read_json_file()
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_trip, best_shop_name = customer.calculate_trip(fuel_price, shops)

        if best_trip <= customer.money:
            print(f"{customer.name} rides to {best_shop_name}\n")

            for store in shops:
                if store.name == best_shop_name:
                    store.shop_print_receipt(customer)

            customer.goes_home_from(best_trip)

        else:
            if customer == customers[-1]:
                print(f"{customer.name} doesn't have"
                      f" enough money to make purchase in any shop")
            else:
                print(f"{customer.name} doesn't have"
                      f" enough money to make purchase in any shop\n")


if __name__ == "__main__":
    shop_trip()
