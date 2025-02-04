from abc import ABC, abstractmethod

import requests

from src.vacancy import Vacancy


class ApiVacancy(ABC):
    """Родительский класс взаимодействия с агрегаторами вакансий по API"""

    @abstractmethod
    def _connect_to_api(self):
        """Метод подключение к API"""
        # Если сделать этот метод приватным, то его нельзя будет наследовать от абстрактного метода
        # В обсуждении к курсовой Станислав Никуличев разрешил его сделать защищенным
        pass

    @abstractmethod
    def get_vacancies(self, request_text):
        """Метод получения данных (вакансий)"""
        pass


class HeadHunterAPI(ApiVacancy):
    """Класс для работы с API HeadHunter (api.hh.ru)"""

    def __init__(self):
        """Инициализация класса HeadHunterAPI"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def _connect_to_api(self) -> dict:
        """Подключение к API hh.ru"""
        # Если сделать этот метод приватным, то его нельзя будет наследовать от абстрактного метода
        # В обсуждении к курсовой Станислав Никуличев разрешил его сделать защищенным
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка запроса к серверу: {response.status_code}")
            return {"items": []}

    def get_vacancies(self, request_text: str, number: int = 100) -> list[Vacancy]:
        """Получение данных (вакансий) с hh.ru в формате списка классов Vacancy"""
        self.__vacancies = []
        self.__params["text"] = request_text
        self.__params["per_page"] = number

        # Забирает данные в формате списка словарей из ключа items
        __vacancies_tmp = self._connect_to_api().get("items")

        # Преобразуем данные из списка словарей JSON в список классов Vacancy
        for item in __vacancies_tmp:
            self.__vacancies.append(
                Vacancy(
                    item.get("id"),
                    item.get("name"),
                    item.get("area").get("name"),
                    item.get("salary"),
                    item.get("alternate_url"),
                    f"{item.get("snippet").get("requirement")}\n{item.get("snippet").get("responsibility")}",
                )
            )

        __vacancies_tmp = []  # Освобождаем память

        return self.__vacancies


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    print(hh_api.get_vacancies("Сторож", 1))
