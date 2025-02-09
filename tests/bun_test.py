import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        "name, price", [
            ("Простая булка", 100),
            ("Кунжутная булка", 120)
        ]
    )
    def test_bun(self, name, price):
        bun: Bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
