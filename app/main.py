import json
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)
        for customer in data["customers"]:
            cust = Customer(
                name=customer["name"],
                products=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=customer["car"],
            )
            print(f"{cust.name} has {cust.money} dollars")
            closest = {}
            shop_names = {}
            cust_prod = []
            prod_price = []
            sh_prod_names = []
            prod_count = []
            sum_all = []
            for shop in data["shops"]:
                sh = Shop(
                    name=shop["name"],
                    location=shop["location"],
                    products=shop["products"]
                )
                fuel = cust.car["fuel_consumption"]
                prod_total = [
                    a * b for a, b in zip
                    (sh.prod_price(), cust.prod_count())
                ]
                prod_total = sum(prod_total)
                fuel_total = round(
                    cust.fuel_shop(fuel, cust.dist_shop(sh.location)), 2
                )
                expenses = prod_total + fuel_total
                closest[sh.name] = expenses
                shop_names[sh.name] = sh.products
                print(
                    f"{cust.name}'s trip to the "
                    f"{sh.name} costs {expenses}"
                )
            if cust.money > expenses:
                print(f"{cust.name} rides to "
                      f"{min(closest, key=closest.get)}")
            else:
                print(
                    f"{cust.name} doesn't have enough "
                    f"money to make purchase in any shop"
                )
                break
            closest_sh = min(closest, key=closest.get)
            print()
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {cust.name}, for you purchase!")
            print("You have bought: ")
            for cl, prod in shop_names.items():
                if cl == closest_sh:
                    for price in prod.values():
                        prod_price.append(price)
            for prod in cust.products.values():
                cust_prod.append(prod)
            for pr_name, pr_count in cust.products.items():
                sh_prod_names.append(pr_name)
                prod_count.append(str(pr_count) + " " + str(pr_name))
            tot_every_product_price = [
                a * b for a, b in zip(prod_price, cust_prod)
            ]
            all_bought_prod = {prod_count[i]: tot_every_product_price[i]
                               for i in range(len(prod_count))}
            for prod, total in all_bought_prod.items():
                sum_all.append(total)
                print(f"{prod}s for {total} dollars")
            print(f"Total cost is {sum(sum_all)} dollars")
            print("See you again!")
            print()
            print(f"{cust.name} rides home")
            print(
                f"{cust.name} now has "
                f"{cust.money - min(closest.values())} dollars"
            )
            print()
