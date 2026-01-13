from app.utils import read_json_file, unpacking_file_data


def shop_trip() -> None:
    file_data: dict = read_json_file("config.json")
    clear_data = unpacking_file_data(file_data)

    for customer in clear_data["customers"]:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in clear_data["shops"]:
            cost = customer.get_trip_cost_to_shop(
                shop,
                clear_data["FUEL_PRICE"])

            cost = round(cost, 2)
            print(f"{customer.name}'s trip to the"
                  f" {shop.name} costs {round(cost, 2)}")

        if customer.cost_to_shop > customer.money:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to"
                  f" {customer.cheaper_shop.name}\n")

            home_coord = customer.location.copy()
            customer.print_check()
            print(f"{customer.name} rides home")
            customer.location = home_coord

            customer.money -= customer.cost_to_shop
            print(f"{customer.name} now has"
                  f" {round(customer.money, 2)} dollars\n")
