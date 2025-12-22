import datetime


def calc(shop_info: list, buyer_infos: list) -> str:
    if not shop_info:
        return "there are no shops"
    string = ""
    for buyer in buyer_infos:
        price_products = {}
        if string:
            string += "\n\n"
        string += f"{buyer.name} has {buyer.money} dollars\n"

        for shop in shop_info:
            distance_shop = ((shop.location[0] - buyer.location[0])**2
                             + (shop.location[1] - buyer.location[1])**2)**0.5
            costs = (sum(buyer.product_cart[key] * shop.product[key]
                         for key in buyer.product_cart)
                     + distance_shop * buyer.car.fuel_price_per_km * 2)
            price_products[costs] = shop
            string += (f"{buyer.name}'s trip to the"
                       f" {shop.name} costs {costs:.2f}\n")
        cheaper_trip = min(price_products)
        if cheaper_trip < buyer.money:

            price_product = 0
            time = datetime.datetime.now()
            string += (f"{buyer.name} rides to "
                       f"{price_products[cheaper_trip].name}\n"
                       f"\nDate: {time.strftime('%d/%m/%Y %H:%M:%S')}"
                       f"\nThanks, {buyer.name}, for your purchase!"
                       f"\nYou have bought:\n")
            home = buyer.location
            buyer.location = price_products[cheaper_trip].location
            for key, value in buyer.product_cart.items():
                shop = price_products[cheaper_trip]
                price = value * shop.product[key]
                price_product += price
                string += (f"{value} {key}s for"
                           f" {price:.2f} dollars\n")

            string += (f"Total cost is {price_product:.2f}"
                       f" dollars\nSee you again!\n\n{buyer.name}"
                       f" rides home\n{buyer.name} now has"
                       f" {buyer.money - cheaper_trip:.2f} dollars")
            buyer.location = home

        else:
            string += (f"{buyer.name} doesn't have enough"
                       f" money to make a purchase in any shop")
    return string
