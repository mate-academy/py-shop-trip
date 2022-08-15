import json

import datetime

import os


def shop_trip():
    # with open("config.json", "r") as f:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]

    cust_lst = [data["customers"][i]["name"]
                for i in range(len(data["customers"]))]
    shops_lst = [data["shops"][i]["name"]
                 for i in range(len(data["shops"]))]

    def costs(customer, shop):
        c_loc = ""
        s_loc = ""
        fuel_cons = ""
        prod_cart = ""
        prods = ""
        for i in range(len(data["customers"])):
            if data["customers"][i]["name"] == customer:
                c_loc = data["customers"][i]["location"]
                fuel_cons = data["customers"][i]["car"]["fuel_consumption"]
                prod_cart = list(data["customers"][i]["product_cart"].values())
        for i in range(len(data["shops"])):
            if data["shops"][i]["name"] == shop:
                s_loc = data["shops"][i]["location"]
                prods = list(data["shops"][i]["products"].values())

        dist = ((c_loc[0] - s_loc[0]) ** 2 + (c_loc[1] - s_loc[1]) ** 2) ** 0.5
        fuel_cost = round(fuel_cons / 100 * dist * fuel_price * 2, 2)
        pr_cost = sum(prod_cart[i] * prods[i] for i in range(len(prods)))
        total_cost = fuel_cost + pr_cost

        return total_cost, customer, shop, pr_cost

    res_list = []

    for i in range(len(data["customers"])):
        res_list.append([])
        money = data['customers'][i]['money']
        with open(f"{cust_lst[i]}.txt", "w") as f:
            f.write(f"{cust_lst[i]} has {money} dollars\n")
        for j in range(len(data["shops"])):
            res = costs(cust_lst[i], shops_lst[j])
            res_list[i].extend([[res[2], res[0], res[3]]])
            with open(f"{cust_lst[i]}.txt", "a") as f:
                f.write(f"{res[1]}'s trip to the {res[2]} costs {res[0]}\n")

    chipest_shop = []
    for elnt in res_list:
        for i in range(len(elnt)):
            if elnt[i][1] == min(elnt[i][1] for i in range(len(elnt))):
                chipest_shop.append(elnt[i])

    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    for i in range(len(cust_lst)):
        if chipest_shop[i][1] <= data["customers"][i]["money"]:
            prod_bought = list(data["customers"][i]["product_cart"].items())
            prod_prises = ""
            for j in range(len(data["shops"])):
                if data["shops"][j]["name"] == chipest_shop[i][0]:
                    prod_prises = list(data["shops"][j]["products"].values())

            ct_gds_1st = prod_bought[0][1]
            gds_1st = prod_bought[0][0]
            gds_1st_cost = ct_gds_1st * prod_prises[0]

            ct_gds_2nd = prod_bought[1][1]
            gds_2nd = prod_bought[1][0]
            gds_2nd_cost = ct_gds_2nd * prod_prises[1]

            ct_gds_3rd = prod_bought[2][1]
            gds_3rd = prod_bought[2][0]
            gds_3rd_cost = ct_gds_3rd * prod_prises[2]

            rest_money = data["customers"][i]["money"] - chipest_shop[i][1]

            with open(f"{cust_lst[i]}.txt", "a") as f:
                f.write(f"{cust_lst[i]} rides to {chipest_shop[i][0]}\n\n"
                        f"Date: {current_time}\n"
                        f"Thanks, {cust_lst[i]}, for you purchase!\n"
                        f"You have bought: \n"
                        f"{ct_gds_1st} {gds_1st}s for {gds_1st_cost} dollars\n"
                        f"{ct_gds_2nd} {gds_2nd}s for {gds_2nd_cost} dollars\n"
                        f"{ct_gds_3rd} {gds_3rd}s for {gds_3rd_cost} dollars\n"
                        f"Total cost is {chipest_shop[i][2]} dollars\n"
                        f"See you again!\n\n"
                        f"{cust_lst[i]} rides home\n"
                        f"{cust_lst[i]} now has {rest_money} dollars\n\n")
        else:
            sad_text = "doesn't have enough money to make purchase in any shop"
            with open(f"{cust_lst[i]}.txt", "a") as f:
                f.write(f"{cust_lst[i]} {sad_text}")

        with open(f"{cust_lst[i]}.txt", "r") as f:
            content = f.read()

        os.remove(f"{cust_lst[i]}.txt")

        with open("content.txt", "a") as f:
            f.write(content)

    with open("content.txt", "r") as f:
        print(f.read())

    os.remove("content.txt")


print(shop_trip())
