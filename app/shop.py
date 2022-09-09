from datetime import datetime
from app.product_calculation import product_calculation_print
from app.movement import trip_to_the_store
from app.movement import trip_to_the_home


def purchase(count_milk: int,
             count_bread: int,
             count_butter: int,
             customer,
             shop):
    """
    Trip to the store (change of coordinates)
    """
    trip_to_the_store(customer, shop)

    """
    Receipt printing
    """
    date = datetime(2021, 1, 4, 12, 33, 41).strftime("%d/%m/%Y %H:%M:%S")
    print(f'Date: {date}')
    print(f'Thanks, {customer["name"]}, for you purchase!')
    print("You have bought:")
    product_calculation_print(count_milk, count_bread, count_butter, shop)
    print("See you again!\n")

    """
    Trip home
    """
    print(f'{customer["name"]} rides home')

    """
    Change of user coordinates and delete temp_file (location_home.json)
    """
    trip_to_the_home(customer)
