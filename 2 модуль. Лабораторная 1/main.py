# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest

class Bookshelf:
    def __int__(self, number_of_books: int, maximum_books: int, ):
        """
        Cоздание и подготовка к работе объекта "Книжная полка"
        :param number_of_books: Количество книг на полке
        :param maximum_books: Сколько книг помещается на полке
        Примеры:
        >>> bookshelf = Bookshelf(2, 15) # Инициализация экземпляра класса
        """
        if not isinstance(number_of_books, int):
            raise TypeError("Количество книг на полке должно быть типа int")
        if number_of_books < 0:
            raise ValueError("Количество книг на полке не может быть отрицательным числом")
        self.maximum_books = maximum_books

        if number_of_books > maximum_books:
            raise ValueError("Количество книг на полке не может быть больше максимального количества книг на полке")

    def add_books(self, add_books: int):
        """
        Добавление книг на полку
        :return: Итоговое количество книг
        :param add_books: Количество добавленных книг
        Примеры:
        >>> bookshelf = Bookshelf(2, 15)
        >>> bookshelf.add_books(1)
        """
        if not isinstance(add_books, int):
            raise TypeError("Добавляемое количество книг должно быть типа int")
        if add_books < 0:
            raise ValueError("Добавляемое количество книг не может быть отрицательным числом")

    def remove_books(self, remove_books, int):
        """
        Снятие книг с полки
        :return: Итоговое количество книг
        :param remove_books: Количество убранных книг
        Примеры:
        >>> bookshelf = Bookshelf(2, 15)
        >>> bookshelf.remove_books(1)
        """
        if not isinstance(remove_books, int):
            raise TypeError("Количество убранных книг должно быть типа int")
        if remove_books < 0:
            raise ValueError("Количество убранных книг не может быть отрицательным числом")

class Bottle:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта Бутылка
        :param capacity_volume: Объем бутылки
        :param occupied_volume: Объем занимаемой жидкости
        Примеры:
        >>> bottle = Bottle(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем должен быть положительным числом")
        self.capacity_volume = capacity_volume  # объем бутылки
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume  # занятый объем бутылки

    def is_full_bottle(self) -> bool:
        """
        Функция которая проверяет является ли бутылка полной
        :return: Является ли бутылка полной
        Примеры:
        >>> bottle = Bottle(500, 0)
        >>> bottle.is_full_bottle()
        """
    def add_water_to_bottle(self, water: float) -> None:
        """
        Добавление воды в бутылку.
        :param water: Объем добавляемой жидкости
        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в бутылке, то вызываем ошибку
        Примеры:
        >>> bottle = Bottle(500, 0)
        >>> bottle.add_water_to_bottle(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")

class Weather:
    def __init__(self, selected_days: int, sunny_days: int, cloudy_days: int):
        """
        Создание и подготовка к работе объекта "Погода"
        :param selected_days: Количество дней
        :param sunny_days: Количество солнечных дней
        :param cloudy_days: Количество пасмурных дней
        Примеры:
        >>> weather = Weather(20, 15, 5)
        """
        if not isinstance(selected_days, int):
            raise TypeError("Количество дней должно быть типа int")
        if selected_days < 0:
            raise ValueError("Количество дней не может быть отрицательным числом")
        self.selected_days = selected_days

        if not isinstance(sunny_days, int):
            raise TypeError("Количество солнечных дней должно быть типа int")
        if sunny_days < 0:
            raise ValueError("Количество солнечных дней не может быть отрицательным числом")
        self.sunny_days = sunny_days

        if not isinstance(cloudy_days, int):
            raise TypeError("Количество пасмурных дней должно быть типа int")
        if cloudy_days < 0:
            raise ValueError("Количество пасмурных дней не может быть отрицательным числом")
        self.cloudy_days = cloudy_days

        if sunny_days + cloudy_days > selected_days:
            raise ValueError("Количество дней не может быть меньше суммарного количества солнечных и пасмурных дней")

    def is_weather_good(self) -> None:
        """
        Функция которая проверяет хорошая ли погода в выбранные дни
        :return: Является ли погода хорошей
        Примеры:
        >>> weather = Weather(20, 15, 5)
        >>> weather.is_weather_good()
        """
    def is_rain_possible(self) -> None:
        """
        Функция которая проверяет возможен ли дождь в выбранные дни
        :return: Возможен ли дождь
        Примеры:
        >>> weather = Weather(20, 15, 5)
        >>> weather.is_rain_possible()
        """

if __name__ == "__main__":
    doctest.testmod()



