from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_create_burger(self):
        burger: Burger = Burger()
        bun: Bun = Bun("dsafsdf", 100)
        burger.set_buns(bun)
        ingredient: Ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "HOT salsa", 100)
        burger.add_ingredient(ingredient)
        assert burger is not None
        assert burger.get_price() == 300

    def test_remove_ingredient(self):
        burger: Burger = Burger()
        ingredient: Ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "HOT salsa", 100)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger: Burger = Burger()
        ingredient0: Ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "HOT salsa", 100)
        burger.add_ingredient(ingredient0)
        ingredient1: Ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 300)
        burger.add_ingredient(ingredient1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient0
        assert burger.ingredients[1] == ingredient1
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient1

    def test_get_receipt(self):
        burger: Burger = Burger()
        burger.set_buns(Bun("dsafsdf", 100))
        sauce: Ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "HOT salsa", 100)
        burger.add_ingredient(sauce)
        bun = '(==== dsafsdf ====)'
        ingredient = '= sauce HOT salsa ='
        price = 'Price: 300'
        result = bun + '\n' + ingredient + '\n' + bun + '\n\n' + price
        assert burger.get_receipt() == result
