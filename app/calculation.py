import datetime


def calc(shop_info: list, buyers_info: list) -> str:
    string = ""
    for buyers in buyers_info:
        price_products = {}
        if len(string) > 0:
            string += "\n\n"
        string += f"{buyers.name} has {buyers.money} dollars\n"

        for shop in shop_info:
            distance_shop = ((shop.location[0] - buyers.location[0])**2
                             + (shop.location[1] - buyers.location[1])**2)**0.5
            costs = (sum(buyers.product_cart[key] * shop.product[key]
                         for key in buyers.product_cart)
                     + distance_shop * buyers.car.fuel_price_per_km * 2)
            price_products[costs] = shop
            string += (f"{buyers.name}'s trip to the"
                       f" {shop.name} costs {round(costs, 2)}\n")

        cheaper_trip = min(price_products)
        if cheaper_trip < buyers.money:

            price_product = 0
            time = datetime.datetime.now()
            string += (f"{buyers.name} rides to "
                       f"{price_products[cheaper_trip].name}\n"
                       f"\nDate: {time.strftime('%d/%m/%Y %H:%M:%S')}"
                       f"\nThanks, {buyers.name}, for your purchase!"
                       f"\nYou have bought:\n")
            home = buyers.location
            buyers.location = price_products[cheaper_trip].location
            for key, value in buyers.product_cart.items():
                price_product += (value
                                  * price_products[cheaper_trip].product[key])
                shop = price_products[cheaper_trip]
                string += (f"{value} {key}s for"
                           f" {value * shop.product[key]:g} dollars\n")

            string += (f"Total cost is {round(price_product, 2)}"
                       f" dollars\nSee you again!\n\n{buyers.name}"
                       f" rides home\n{buyers.name} now has"
                       f" {round(buyers.money - cheaper_trip, 2)} dollars")
            buyers.location = home

        else:
            string += (f"{buyers.name} doesn't have enough"
                       f" money to make a purchase in any shop")
    return string
