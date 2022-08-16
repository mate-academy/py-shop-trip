import os
import datetime
from app.customers import custs
from app.shops import shops


def shop_trip():

    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    all_shoppings = [[] for _ in range(len(custs))]

    for shop in shops:
        for i, cust in enumerate(custs):
            all_shoppings[i].extend([cust.shopping(shop)])

    chippest_shoppings = []

    for i, elmt in enumerate(all_shoppings):
        with open(f"{elmt[i][0]}.txt", "w") as f:
            f.write(f"{elmt[i][0]} has {elmt[i][1]} dollars\n")
        for el in elmt:
            with open(f"{el[0]}.txt", "a") as f:
                f.write(f"{el[0]}'s trip to the {el[2]} costs {el[-1]}\n")
            if el[-1] == min(item[-1] for item in elmt):
                chippest_shoppings.append(el)

    for elt in chippest_shoppings:
        if elt[7] <= elt[1]:
            with open(f"{elt[0]}.txt", "a") as f:
                f.write(f"{elt[0]} rides to {elt[2]}\n\n"
                        f"Date: {current_time}\n"
                        f"Thanks, {elt[0]}, for you purchase!\n"
                        f"You have bought: \n"
                        f"{elt[3][0]} {elt[4][0]}s for {elt[5][0]} dollars\n"
                        f"{elt[3][1]} {elt[4][1]}s for {elt[5][1]} dollars\n"
                        f"{elt[3][2]} {elt[4][2]}s for {elt[5][2]} dollars\n"
                        f"Total cost is {elt[6]} dollars\n"
                        f"See you again!\n\n"
                        f"{elt[0]} rides home\n"
                        f"{elt[0]} now has {elt[1] - elt[7]} dollars\n\n")
        else:
            sad_text = "doesn't have enough money to make purchase in any shop"
            with open(f"{elt[0]}.txt", "a") as f:
                f.write(f"{elt[0]} {sad_text}")

        with open(f"{elt[0]}.txt", "r") as f:
            content = f.read()

        os.remove(f"{elt[0]}.txt")

        with open("content.txt", "a") as f:
            f.write(content)

    with open("content.txt", "r") as f:
        print(f.read())

    os.remove("content.txt")


shop_trip()
