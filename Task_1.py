import doctest

class Ship:
    def __init__(self, name: str, length: float, capacity: int):
        """
        Создание и подготовка к работе объекта "Корабль"

        :param name: Название корабля
        :param length: Длина корабля
        :param capacity: Вместимость корабля

        Примеры:
        >>> ship = Ship("Titanic", 269.1, 3547)
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость должна быть положительным целым числом")

        self.name = name
        self.length = length
        self.capacity = capacity

    def sail(self, destination: str) -> None:
        """
        Отправка корабля в пункт назначения.

        :param destination: Пункт назначения

        Примеры:
        >>> ship = Ship("Titanic", 269.1, 3547)
        >>> ship.sail("New York")
        """
        ...

    def dock(self) -> None:
        """
        Швартовка корабля в порту.

        Примеры:
        >>> ship = Ship("Titanic", 269.1, 3547)
        >>> ship.dock()
        """
        ...

class Ball:
    def __init__(self, type_: str, diameter: float):
        """
        Создание и подготовка к работе объекта "Мяч"

        :param type_: Тип мяча (например, футбольный, баскетбольный)
        :param diameter: Диаметр мяча

        Примеры:
        >>> ball = Ball("football", 22.0)
        """
        if not isinstance(type_, str):
            raise TypeError("Тип мяча должен быть строкой")
        if not isinstance(diameter, (int, float)) or diameter <= 0:
            raise ValueError("Диаметр должен быть положительным числом")

        self.type_ = type_
        self.diameter = diameter

    def bounce(self) -> None:
        """
        Отскок мяча от поверхности.

        Примеры:
        >>> ball = Ball("football", 22.0)
        >>> ball.bounce()
        """
        ...

    def deflate(self) -> None:
        """
        Сдувание мяча.

        Примеры:
        >>> ball = Ball("football", 22.0)
        >>> ball.deflate()
        """
        ...

class Painting:
    def __init__(self, title: str, artist: str, year: int):
        """
        Создание и подготовка к работе объекта "Картина"

        :param title: Название картины
        :param artist: Имя художника
        :param year: Год создания картины

        Примеры:
        >>> painting = Painting("Mona Lisa", "Leonardo da Vinci", 1503)
        """
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(artist, str):
            raise TypeError("Имя художника должно быть строкой")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год должен быть положительным целым числом")

        self.title = title
        self.artist = artist
        self.year = year

    def display(self) -> None:
        """
        Отображение картины в галерее.

        Примеры:
        >>> painting = Painting("Mona Lisa", "Leonardo da Vinci", 1503)
        >>> painting.display()
        """
        ...

    def restore(self) -> None:
        """
        Реставрация картины.

        Примеры:
        >>> painting = Painting("Mona Lisa", "Leonardo da Vinci", 1503)
        >>> painting.restore()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
