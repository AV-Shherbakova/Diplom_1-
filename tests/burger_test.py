from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

SAUCE_NAME = "HOT salsa"

BUN_NAME = "Вкусная булка"


class TestBurger:

    def test_create_burger(self):
        burger: Burger = Burger()
        bun: Bun = Bun(BUN_NAME, 100)
        burger.set_buns(bun)
        ingredient: Ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_NAME, 100)
        burger.add_ingredient(ingredient)
        assert burger is not None
        assert burger.get_price() == 300

    def test_remove_ingredient(self):
        burger: Burger = Burger()
        ingredient_mock: Mock = Mock()
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger: Burger = Burger()
        ingredient_mock0: Mock = Mock()
        ingredient_mock1: Mock = Mock()
        burger.add_ingredient(ingredient_mock0)
        burger.add_ingredient(ingredient_mock1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient_mock0
        assert burger.ingredients[1] == ingredient_mock1
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_mock1
        assert burger.ingredients[1] == ingredient_mock0

    def test_get_receipt(self):
        burger: Burger = Burger()
        burger.set_buns(Bun(BUN_NAME, 100))
        sauce: Ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_NAME, 100)
        burger.add_ingredient(sauce)
        bun = f'(==== {BUN_NAME} ====)'
        ingredient = f'= {INGREDIENT_TYPE_SAUCE.lower()} {SAUCE_NAME} ='
        price = 'Price: 300'
        result = bun + '\n' + ingredient + '\n' + bun + '\n\n' + price
        assert burger.get_receipt() == result
