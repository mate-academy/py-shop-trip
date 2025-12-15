import datetime
from app.shop import Shop


def test_receipt_output(capsys):
    shop = Shop(
        name="Test Shop",
        location=[0.0, 0.0],
        products={"Apple": 3.00, "Bread": 2.00, "Milk": 6.00}
    )

    cart = {"Apple": 2, "Bread": 1, "Milk": 2}
    timestamp = datetime.datetime(2023, 1, 1, 12, 0, 0)

    total = shop.print_receipt("Bob", cart, timestamp=timestamp)
    captured = capsys.readouterr()

    assert total == 20.0
    assert "2023-01-01 12:00:00" in captured.out
    assert "2 apples for 6 dollars" in captured.out
    assert "1 breads for 2 dollars" in captured.out
    assert "2 milks for 12 dollars" in captured.out
    assert "Total cost is 20.0 dollars" in captured.out
