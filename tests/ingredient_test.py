import allure
import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type, name, price", [
            (INGREDIENT_TYPE_SAUCE, "Salsa", 100),
            (INGREDIENT_TYPE_SAUCE, "Chili", 120)
        ]
    )
    @allure.title("Проверка создания ингредиента")
    def test_create_ingredient(self, ingredient_type, name, price):
        ingredient: Ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_price() == price
        assert ingredient.get_name() == name
