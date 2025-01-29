from src.utils import get_top_n_vacancies, vacancies_by_keyword


# Тестирование функции получения ТОП-N вакансий get_top_n_vacancies
def test_get_top_n_vacancies(vacancies_list):
    assert get_top_n_vacancies(vacancies_list, 2) == [vacancies_list[0], vacancies_list[1]]


# Тестирование функции получения ТОП-N вакансий get_top_n_vacancies (пустой список)
def test_get_top_n_vacancies_empty():
    assert get_top_n_vacancies([], 5) == []


# Тестирование функции поиска слова по описанию vacancies_by_keyword
def test_vacancies_by_keyword(vacancies_list):
    assert vacancies_by_keyword(vacancies_list, "инженер-Конструктор") == [
        vacancies_list[0],
        vacancies_list[1],
        vacancies_list[4],
    ]
    assert vacancies_by_keyword(vacancies_list, "AUTOCAD") == [vacancies_list[0], vacancies_list[2]]


# Тестирование функции поиска слова по описанию vacancies_by_keyword (нет такого слова в описании)
def test_vacancies_by_keyword_not_found(vacancies_list):
    assert vacancies_by_keyword(vacancies_list, "Python") == []


# Тестирование функции поиска слова по описанию vacancies_by_keyword (вход - пустой список)
def test_vacancies_by_keyword_empty():
    assert vacancies_by_keyword([], "Python") == []
