import datetime


class Shop:
    def __init__(self, name, location, products):
        self.name = name
        self.location = location
        self.products = products

    def sale_of_goods(self, customer):
        print("Date:", datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought:")
        total_cost = 0
        for buyable, amount in customer.product_cart.items():
            for sellable, price in self.products.items():
                if buyable == sellable:
                    total_cost += (amount * price)
                    print(f"{amount} {buyable}s for {amount * price} dollars")
        print(f"Total cost is {round(total_cost, 2)} dollars")

        # print(customer.product_cart)
        # print(self.products)
        print("See you again!")
        # You have bought:
        # 4 milks for 12 dollars
        # 2 breads for 2 dollars
        # 5 butters for 12.5 dollars
        # Total cost is 26.5 dollars
        # See you again!
        #
        # Bob rides home
        # Bob now has 26.79 dollars
        #
        pass

    def __repr__(self):
        return (f"{self.name}")


if __name__ == '__main__':
    x = Shop(name="", location="", products="")
