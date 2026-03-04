from app.main import shop_trip
from typing import Any


def test_shop_trip_runs(capsys: Any) -> None:
    shop_trip()
    captured = capsys.readouterr()
    assert "rides to" in captured.out
