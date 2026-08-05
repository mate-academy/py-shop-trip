from app.data_loader import load_data


def shop_trip() -> None:
    data = load_data()
    fuel_price = data["fuel_price"]
    customers = data["customers"]
    shops = data["shops"]

    for client in customers:
        total_spent_of_trip = []
        print(f"{client.name} has {client.money} dollars")
        for shop in shops:
            distance = client.distance_trip(client.location, shop.location)
            total_cost = client.total_cost_of_products(shop.products) + (client.car.total_cost_of_fuel(distance, fuel_price) * 2)
            total_spent_of_trip.append(total_cost)
            print(f"{client.name}'s trip to the {shop.name} costs {round(total_cost, 2)}")

        min_cost = min(total_spent_of_trip)
        key = total_spent_of_trip.index(min_cost)

        if client.money >= min_cost:
            print(f"{client.name} rides to {shops[key].name}\n")
            client.location = shops[key].location
            client.print_receipt(shops[key])
            client.money -= min_cost
            print(f"{client.name} rides home")
            print(f"{client.name} now has {round(client.money, 2)} dollars\n")
        else:
            print(f"{client.name} doesn't have enough money to make a purchase in any shop")
