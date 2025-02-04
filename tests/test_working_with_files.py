import os.path

from src.working_with_files import WorkingFileVacanciesJSON

file = "tests/vacancy_test.json"


# Тестирование на попытку чтения данных если файл не существует
def test_read_not_file():
    # Если файл существует, удаляем его.
    if os.path.isfile(file):
        os.remove(file)
    work_file = WorkingFileVacanciesJSON(file)
    assert not work_file.read_from()  # Так чтение не удалось, то вернерт False
    assert work_file.get_data == []  # Должен вернуть пустой список


# Тестирование метода добавления данных в файл
def test_add_file(vacancies_list, first_vacancy):
    work_file = WorkingFileVacanciesJSON(file)
    assert work_file.add_to(vacancies_list) == 5  # добавление 5 новых вакансий
    assert work_file.add_to([first_vacancy]) == 1  # добавление 1 новой вакансии
    assert len(work_file.get_data) == 6  # вакансий должно быть 6
    assert work_file.get_data[5].id == "116455408"  # id последней добавленной вакансии
    assert os.path.isfile(file)  # файл с данными должен быть создан


# Тестирование добавления уже существующих в файле вакансий
def test_add_vacancies_present(vacancies_list):
    work_file = WorkingFileVacanciesJSON(file)
    assert work_file.add_to(vacancies_list) == 0  # добавленных данных должно быть 0
    assert len(work_file.get_data) == 6  # вакансий должно быть 6


# Тестирование чтения данных с 6 вакансиями
def test_read_file():
    work_file = WorkingFileVacanciesJSON(file)
    assert work_file.read_from()
    assert len(work_file.get_data) == 6  # Должен вернуть пустой список


# Тестирование удаления данных по id. Удаление предпоследнего элемента с ID "116390705"
def test_delete():
    work_file = WorkingFileVacanciesJSON(file)
    assert work_file.del_data("116390705")  # удаление прошло успешно
    assert len(work_file.get_data) == 5  # вакансий должно быть
    assert work_file.get_data[4].id == "116455408"  # id последней добавленной вакансии


# Тестирование удаления данных по id. Удаление не существующего элемента с ID "116390705"
def test_delete_no_exist():
    work_file = WorkingFileVacanciesJSON(file)
    assert not work_file.del_data("116390705")  # удаление не произошло
    assert len(work_file.get_data) == 5  # вакансий должно быть 5


# Тестирование удаления данных по id. Удаление всех данных (с *)
def test_delete_all():
    work_file = WorkingFileVacanciesJSON(file)
    assert work_file.del_data("*")  # удаление прошло успешно
    assert len(work_file.get_data) == 0  # вакансий должно быть 0
