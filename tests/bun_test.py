import allure
import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        "name, price", [
            ("Простая булка", 100),
            ("Кунжутная булка", 120)
        ]
    )
    @allure.title("Проверка метода получения названия булки")
    def test_bun_name(self, name, price):
        bun: Bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price", [
            ("Простая булка", 100),
            ("Кунжутная булка", 120)
        ]
    )
    @allure.title("Проверка метода получения цены булки")
    def test_bun_price(self, name, price):
        bun: Bun = Bun(name, price)
        assert bun.get_price() == price
