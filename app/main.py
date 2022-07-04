from app.customer import Customer
from app.shop import Shop


def person():
    lst_of_names = []
    for persona in Customer.create_customer("config.json"):
        lst_of_names.append(persona.name)
    return lst_of_names


def shop_trip():
    customer = input("Please, enter your name: ")
    if customer not in person():
        print("Sorry, we have not information")
    persons = Customer.create_customer("config.json")
    for persona in persons:
        if customer == persona.name:
            persona.has_money()
            costs = []
            shops = Shop.create_shop("config.json")
            for shop in shops:
                costs.append(persona.cost(shop))
                print(f"{persona.name}'s trip to the {shop.name} costs {persona.cost(shop)}")
            index = costs.index(min(costs))
            if persona.money < persona.cost(shops[index]):
                print(f"{persona.name} doesn't have enough money to make purchase in any shop")
                return
            cheap_shop = shops[index]
            home_location = persona.location
            persona.to_shop(cheap_shop)
            print(cheap_shop.print_bill(persona))
            persona.to_home()
            persona.location = home_location
            print(persona.remain_money(cheap_shop))


if __name__ == '__main__':
    shop_trip()