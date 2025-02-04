import json
import os.path
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class WorkingWithVacancyDBabc(ABC):
    """Родительский класс для работы с файлами"""

    @abstractmethod
    def add_to(self, data):
        """Метод добавления данных (вакансий) в файл"""
        pass

    @abstractmethod
    def read_from(self):
        """Метод получения данных (вакансий) из файла"""
        pass

    @abstractmethod
    def del_data(self, id):
        """Метод удаления данных (вакансий) из файла"""
        pass


class WorkingFileVacanciesJSON(WorkingWithVacancyDBabc):
    """Класс для работы с JSON-файлами вакансий"""

    def __init__(self, file=r"data/vacancies.json"):
        self.__file = file  # Путь к файлу
        self.__data = []  # Данные: список вакансий класса Vacancy

    @property
    def get_data(self) -> list[Vacancy]:
        """Метод получения всех хранящихся в файле данных в формате списка экземпляров класс Vacancy"""
        if not self.__data:
            self.read_from()
        return self.__data

    def __save_to(self) -> None:
        """Метод выполняет сохранение данных self.__data в JSON-файл в виде списка словарей."""

        # Преобразование self.__data из списка Vacancy в список словарей
        list_vac = []
        for item in self.__data:
            list_vac.append(item.dict())

        # Сохранение списка словарей в JSON-файл
        with open(self.__file, "w", encoding="utf-8") as f:
            json.dump(list_vac, f, ensure_ascii=False)

    def read_from(self) -> bool:
        """Метод выполняет чтение данный из JSON-файла в self.__data в формате списка экземпляров класса Vacancy.
        В случае удачи вернет True, иначе False"""
        self.__data = []
        if not os.path.isfile(self.__file):
            return False
        with open(self.__file, encoding="utf-8") as f:
            vacancies_tmp = json.load(f)

        # Преобразование списка словарей JSON в список классов Vacancy self.__data
        for item in vacancies_tmp:
            self.__data.append(Vacancy(**item))
        return True

    def add_to(self, added_data: list[Vacancy]) -> int:
        """Метод добавляет данные в self.__data исключая повторения, затем сохраняет
        данные в JSON-файле. Возвращает количество добавленных вакансий."""
        if not self.__data:
            self.read_from()

        coincidences = 0  # счетчик дубликатов
        counter = 0  # счетчик добавленных вакансий
        for new_vac in added_data:
            presence_flag = False
            for old_vac in self.__data:
                if new_vac.id == old_vac.id:
                    presence_flag = True
                    break
            if presence_flag:
                coincidences += 1
            else:
                counter += 1
                self.__data.append(new_vac)

        # Сохраняем полученные данные в файл JSON
        self.__save_to()

        return counter

    def del_data(self, id: str) -> bool:
        """Метод удаляет данные из JSON-файла по id. * - удалить все. id должен быть типа str.
        Возвращает True если удачно, иначе False"""
        if id == "*":
            self.__data = []
            self.__save_to()
            return True

        if not self.__data:
            self.read_from()

        # Поиск индекса вакансии по id
        i_del = -1  # индекс элемента с id для удаления
        for i, vac in enumerate(self.__data):
            if vac.id == id:
                i_del = i
                break

        # Удаление вакансии по индексу i_del, если он найден
        if i_del != -1:
            del self.__data[i_del]
            self.__save_to()
            return True

        return False


if __name__ == "__main__":
    work_file = WorkingFileVacanciesJSON("../data/vacancies.json")
    print("Данные прочитаны: ", work_file.read_from())
    print("Полученные вакансии: ", work_file.get_data)
    print("Удаление по ID=777: ", work_file.del_data("777"))
