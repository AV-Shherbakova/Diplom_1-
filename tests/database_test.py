import allure

from praktikum.database import Database


class TestDatabase:

    @allure.title("Проверка инициализации базы данных")
    def test_init_database(self):
        db: Database = Database()
        assert len(db.available_buns()) == 3
        assert len(db.available_ingredients()) == 6
