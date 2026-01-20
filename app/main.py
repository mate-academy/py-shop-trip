import json
from math import sqrt
import datetime
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    # Создание объектов класса Customer
    customers = []
    for data_customers in data["customers"]:
        customer = Customer(
            name=data_customers["name"],
            product_cart=data_customers["product_cart"],
            location=data_customers["location"],
            money=data_customers["money"],
            car=data_customers["car"]
        )
        customers.append(customer)

    # Создание объектов класса Shop
    shops = []
    for data_shop in data["shops"]:
        shop = Shop(
            name=data_shop["name"],
            location=data_shop["location"],
            products=data_shop["products"]
        )
        shops.append(shop)
    shop_lenght = (len(shops))
    _lenght = 0

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        small_price = {}
        _lenght += 1
        for shop in shops:
            # Расчет стоимости топлива на дорогу туда и обратно
            path = sqrt(
                ((shop.location[0] - customer.location[0]) ** 2)
                + ((shop.location[1] - customer.location[1]) ** 2)
            )
            fuel_cost = data["FUEL_PRICE"] * (
                2 * (path * (customer.car["fuel_consumption"] / 100))
            )
            fuel_cost = round(fuel_cost, 2)

            # Расчет стоимости продуктов в магазине
            milk_price = (
                customer.product_cart["milk"] * shop.products["milk"]
            )
            bread_price = (
                customer.product_cart["bread"] * shop.products["bread"]
            )
            butter_price = (
                customer.product_cart["butter"] * shop.products["butter"]
            )
            food_price = milk_price + bread_price + butter_price

            # Сумма всех расходов
            price = fuel_cost + food_price
            print(
                f"{customer.name}'s trip to "
                f"the {shop.name} costs {price}")
            small_price[shop.name] = price

        # Проверка, есть ли деньги на покупку
        if customer.money >= min(small_price.values()):
            cheapest_shop = min(small_price, key=small_price.get)
            print(f"{customer.name} rides to {cheapest_shop}")

            choss_shop = next(
                shop for shop in shops if shop.name == cheapest_shop
            )

            # Расчет стоимости товаров в выбранном магазине
            milk_price = (
                customer.product_cart["milk"] * choss_shop.products["milk"]
            )
            bread_price = (
                customer.product_cart["bread"] * choss_shop.products["bread"]
            )
            butter_price = (
                customer.product_cart["butter"] * choss_shop.products["butter"]
            )
            food_price = milk_price + bread_price + butter_price

            total_trip_cost = small_price[cheapest_shop]

            # Обновление суммы оставшихся денег у клиента
            customer.money = round(customer.money - total_trip_cost, 2)

            print()
            now_date = datetime.datetime.now()
            format_date = now_date.strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {format_date}")
            print(f"Thanks, {customer.name}, for your purchase!")

            # Вывод товаров и стоимости
            print("You have bought:")
            print(
                f"{customer.product_cart['milk']} "
                f"milks for {milk_price} dollars"
            )
            print(
                f"{customer.product_cart['bread']} "
                f"breads for {bread_price:.0f} dollars"
            )
            print(
                f"{customer.product_cart['butter']} "
                f"butters for {butter_price} dollars"
            )
            print(f"Total cost is {food_price} dollars")

            print("See you again!")
            print()
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars")
        else:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
        if _lenght == shop_lenght:
            pass
        else:
            print()
