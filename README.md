# Shop trip

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

You want to create an application that helps customers to choose the cheapest
trip for the products.

There is `config.json` file that contains:
- `FUEL_PRICE` - Price for 1 liter of fuel in dollars.
- `customers` - list of dictionaries with information about each customer.
- `shops` - list of dictionaries with information about each shop in the city. 

You have information about 

Customers:
- name
- products he wants to buy
- location
- money
- car
  - brand
  - volume of fuel consumption for 100 kilometers.

Shops:
- name
- location
- products that shop provides

Write `shop_trip` function that doesn't take any argument,
where customers calculate how 
much will cost trip for the products in every shop and pick
the cheapest one and ride there if they have enough money.
When the customer arrives at the shop his location should equal to
shop location. After customer buys products, shop prints purchase
receipt using current time. After the shop he arrives home and
counts the remaining money.

The cost of the trip consists of three parts: the fuel cost to get 
to the shop, cost of all products to buy, the fuel cost to get home.

For example, let's say now is 04/01/2021 12:33:41:
```javascript
 // config.py:

{
    "FUEL_PRICE": 2.4,   
    "customers": [
        {
            "name": "Bob",
            "product_cart": {
                "milk": 4,
                "bread": 2,
                "butter": 5
            },
            "location": [12, -2],
            "money": 55,
            "car": {
                "brand": "Suzuki",
                "fuel_consumption": 9.9
            }
        },
        {
            "name": "Monica",
            "product_cart": {
                "milk": 3,
                "bread": 3,
                "butter": 1
            },
            "location": [11, -2],
            "money": 12,
            "car": {
                "brand": "Audi",
                "fuel_consumption": 7.6
            }
        }
    ],
    "shops": [
        {
            "name": "Outskirts Shop",
            "location": [10, -5],
            "products": {
                "milk": 3,
                "bread": 1,
                "butter": 2.5
            }
        },
        {
            "name": "Shop '24/7'",
            "location": [4, 3],
            "products": {
                "milk": 2,
                "bread": 1.5,
                "butter": 3.2
            }
        },
    ]
}
```
```python
# main.py:
shop_trip()

# Bob has 55 dollars
# Bob's trip to the Outskirts Shop costs 28.21
# Bob's trip to the Shop '24/7' costs 31.48
# Bob rides to Outskirts Shop
# 
# Date: 04/01/2021 12:33:41
# Thanks, Bob, for your purchase!
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
# Monica has 12 dollars
# Monica's trip to the Outskirts Shop costs 15.65
# Monica's trip to the Shop '24/7' costs 16.84
# Monica doesn't have enough money to make a purchase in any shop
```
You design application architecture by yourself, but there are some rules:
* The `main.py` module must contain only `shop_trip` function
* You must create and use at least 2 additional modules
* Your project use at least 2 classes

<details open>
  <summary>
    Hint: modules structure example if you have problems with architecture.
  </summary>
  py-shop-trip/<br>
  |-- car.py<br>
  |-- customer.py<br>
  |-- main.py<br>
  └-- shop.py<br>
</details>


Distance between customer and shop is a distance between their locations in km. 
Round printed value to two decimal places.


### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
