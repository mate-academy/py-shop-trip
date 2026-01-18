def going_to_shop(customer: any, shops: any) -> None:
    print(f"\n{customer.name} has {customer.money} dollars")
    for key, value in customer.total_trip_cost.items():
        print(f"{customer.name}'s trip to the {key} "
              f"costs {round(float(value), 2)}")
    if customer.cheapest_cost < customer.money:
        print(f"{customer.name} rides to {customer.cheapest_shop}")
        for shop in shops:
            if shop.name == customer.cheapest_shop:
                customer.location = shop.location
    else:
        print(f"{customer.name} doesn't have enough money "
              f"to make a purchase in any shop")
