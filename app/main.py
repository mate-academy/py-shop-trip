from app.customer import Customer
from app.shop import Shop


def shop_trip():
    persons = Customer.create_customer("app/config.json")
    for persona in persons:
        persona.has_money()
        costs = []
        shops = Shop.create_shop("app/config.json")
        for shop in shops:
            costs.append(persona.cost(shop))
            print(f"{persona.name}'s trip to the "
                  f"{shop.name} costs {persona.cost(shop)}")
        index = costs.index(min(costs))
        if persona.money <\
                persona.cost(shops[index]):
            print(f"{persona.name} "
                  f"doesn't have enough money to make purchase in any shop")
            return
        cheap_shop = shops[index]
        home_location = persona.location
        persona.to_shop(cheap_shop)
        print('')
        cheap_shop.print_bill(persona)
        print('')
        persona.to_home()
        persona.location = home_location
        print(persona.remain_money(cheap_shop))
        print('')
