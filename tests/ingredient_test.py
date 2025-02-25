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
    @allure.title("Проверка создания ингредиента (тип)")
    def test_create_ingredient_type(self, ingredient_type, name, price):
        ingredient: Ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize(
        "ingredient_type, name, price", [
            (INGREDIENT_TYPE_SAUCE, "Salsa", 100),
            (INGREDIENT_TYPE_SAUCE, "Chili", 120)
        ]
    )
    @allure.title("Проверка создания ингредиента (цена)")
    def test_create_ingredient_price(self, ingredient_type, name, price):
        ingredient: Ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price


    @pytest.mark.parametrize(
        "ingredient_type, name, price", [
            (INGREDIENT_TYPE_SAUCE, "Salsa", 100),
            (INGREDIENT_TYPE_SAUCE, "Chili", 120)
        ]
    )
    @allure.title("Проверка создания ингредиента (название)")
    def test_create_ingredient_name(self, ingredient_type, name, price):
        ingredient: Ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name
