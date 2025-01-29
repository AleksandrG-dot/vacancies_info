class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("id", "name", "city", "salary", "url", "description")

    def __init__(self, id: str, name: str, city: str, salary: dict, url: str, description: str):
        """Инициализатор для класса"""
        salary = self.__validate_salary(salary)
        self.id = id
        self.name = name
        self.city = city
        self.salary = salary  # словарь с ключами from, to, currency
        self.url = url
        self.description = description

    @staticmethod
    def __validate_salary(salary: dict) -> dict:
        """Метод валидирует данные по зарплате."""

        def num_valid(num) -> int:
            """Валидирует число. Переводит поступающий тип данных в integer. Если None, то вернет 0"""
            if num is None:
                return 0
            else:
                return int(num)

        if salary is None:
            return {"from": 0, "to": 0, "currency": ""}

        return {
            "from": num_valid(salary.get("from")),
            "to": num_valid(salary.get("to")),
            "currency": salary.get("currency"),
        }

    def dict(self) -> dict:
        """Метод преобразует Vacancy в словарь JSON"""
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "salary": self.salary,
            "url": self.url,
            "description": self.description,
        }

    def __str__(self) -> str:
        """Магический метод для строкового отображения объекта"""
        return (f"ID: {self.id}, Вакансия: {self.name}, Город: {self.city}, "
                f"Зарплата: {self.salary['from']}-{self.salary['to']} {self.salary['currency']}, url: {self.url}")

    def __eq__(self, other) -> bool:
        """Магический метод сравнения вакансий по зарплате на равенство"""
        if type(self) is not type(other):
            raise TypeError("Нельзя сравнивать объекты разных классов")
        return self.salary.get("from") == other.salary.get("from")

    def __le__(self, other) -> bool:
        """Магический метод сравнения вакансий по зарплате (меньше или равно)"""
        if type(self) is not type(other):
            raise TypeError("Нельзя сравнивать объекты разных классов")
        return self.salary.get("from") <= other.salary.get("from")

    def __ge__(self, other) -> bool:
        """Магический метод сравнения вакансий по зарплате (больше или равно)"""
        if type(self) is not type(other):
            raise TypeError("Нельзя сравнивать объекты разных классов")
        return self.salary.get("from") >= other.salary.get("from")
