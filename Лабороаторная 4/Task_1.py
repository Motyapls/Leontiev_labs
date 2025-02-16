class Animal:
    """Базовый класс для животных."""
    def __init__(self, name: str, age: int):
        """
        Инициализация животного.
        :param name: Имя животного
        :param age: Возраст животного
        """
        self._name = name  # Имя не должно изменяться напрямую
        self.age = age

    @property
    def name(self) -> str:
        """Геттер для имени животного."""
        return self._name

    def make_sound(self) -> str:
        """Метод, который должен быть переопределен в дочерних классах."""
        return "Животное издает звук"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.name}, {self.age} лет"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age})"


class Dog(Animal):
    """Класс, представляющий собаку."""
    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализация собаки.
        :param name: Имя собаки
        :param age: Возраст собаки
        :param breed: Порода собаки
        """
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> str:
        """
        Перегрузка метода make_sound. Собака лает.
        """
        return "Гав-гав!"

    def __str__(self) -> str:
        return f"Собака: {self.name}, {self.age} лет, порода {self.breed}"

    def __repr__(self) -> str:
        return f"Dog(name={self.name!r}, age={self.age}, breed={self.breed!r})"


if __name__ == "__main__":
    animal = Animal("Неизвестное", 5)
    dog = Dog("Бобик", 3, "Овчарка")

    print(animal)  # Выводит информацию о животном
    print(dog)     # Выводит информацию о собаке
    print(animal.make_sound())  # Вызывает метод базового класса
    print(dog.make_sound())     # Вызывает переопределенный метод
