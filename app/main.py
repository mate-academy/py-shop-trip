import os
import datetime
from app.customers import customers
from app.shops import shops


def shop_trip():

    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    all_shoppings = [[] for _ in range(len(customers))]

    for shop in shops:
        for i, customer in enumerate(customers):
            all_shoppings[i].extend([customer.shopping(shop)])

    chippest_shoppings = []

    for i, customer_shop in enumerate(all_shoppings):
        with open(f"{customer_shop[i][0]}.txt", "w") as f:
            f.write(f"{customer_shop[i][0]} has "
                    f"{customer_shop[i][1]} dollars\n")
        for shopping in customer_shop:
            with open(f"{shopping[0]}.txt", "a") as f:
                f.write(f"{shopping[0]}'s trip "
                        f"to the {shopping[2]} costs {shopping[7]}\n")
            if shopping[7] == min(shopping[7] for shopping in customer_shop):
                chippest_shoppings.append(shopping)

    for shopping in chippest_shoppings:
        if shopping[7] <= shopping[1]:
            with open(f"{shopping[0]}.txt", "a") as f:
                f.write(f"{shopping[0]} rides to {shopping[2]}\n\n"
                        f"Date: {current_time}\n"
                        f"Thanks, {shopping[0]}, for you purchase!\n"
                        f"You have bought: \n"
                        f"{shopping[3][0]} {shopping[4][0]}s for "
                        f"{shopping[5][0]} dollars\n"
                        f"{shopping[3][1]} {shopping[4][1]}s for "
                        f"{shopping[5][1]} dollars\n"
                        f"{shopping[3][2]} {shopping[4][2]}s for "
                        f"{shopping[5][2]} dollars\n"
                        f"Total cost is {shopping[6]} dollars\n"
                        f"See you again!\n\n"
                        f"{shopping[0]} rides home\n"
                        f"{shopping[0]} now has {shopping[1] - shopping[7]} "
                        f"dollars\n\n")
        else:
            sad_text = "doesn't have enough money to make purchase in any shop"
            with open(f"{shopping[0]}.txt", "a") as f:
                f.write(f"{shopping[0]} {sad_text}")

        with open(f"{shopping[0]}.txt", "r") as f:
            content = f.read()

        os.remove(f"{shopping[0]}.txt")

        with open("content.txt", "a") as f:
            f.write(content)

    with open("content.txt", "r") as f:
        print(f.read())

    os.remove("content.txt")


shop_trip()
