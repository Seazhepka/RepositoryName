class Vehicle:
    """
    Базовый класс для всех транспортных средств.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.
        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.
        :return: Строка с информацией о марке, модели и годе выпуска.
        """
        return f"{self.year} {self.brand} {self.model}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление транспортного средства.
        :return: Официальная строка для создания объекта.
        """
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self.year})"

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства.
        :return: Сообщение о запуске двигателя.
        """
        return f"The engine of {self.brand} {self.model} has started."


class Car(Vehicle):
    """
    Класс для легковых автомобилей, наследует от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация легкового автомобиля.
        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param doors: Количество дверей.
        """
        super().__init__(brand, model, year)
        self.__doors = doors

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.
        :return: Строка с информацией о марке, модели, годе выпуска и количестве дверей.
        """
        return f"{super().__str__()} with {self.__doors} doors"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление легкового автомобиля.
        :return: Официальная строка для создания объекта.
        """
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, doors={self.__doors})"

    def start_engine(self) -> str:
        """
        Запускает двигатель легкового автомобиля с дополнительным сообщением.
        Переопределение метода для предоставления специфичной информации о легковом автомобиле.
        :return: Сообщение о запуске двигателя с указанием количества дверей.
        """
        return f"The engine of {self.brand} {self.model} has started. It has {self.__doors} doors."


if __name__ == "__main__":
    my_car = Car("BMW", "X6", 2024, 4)
    print(my_car)
    print(repr(my_car))
    print(my_car.start_engine())
