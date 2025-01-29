# Тест класса Vacancy (cтандартный случай)
def test_vacancy_one(first_vacancy):
    assert first_vacancy.id == "116455408"
    assert first_vacancy.name == "Python-разработчик"
    assert first_vacancy.city == "Москва"
    assert first_vacancy.salary == {"from": 80000, "to": 105000, "currency": "RUR"}
    assert first_vacancy.url == "https://hh.ru/vacancy/116455408"
    assert (
        first_vacancy.description
        == "От 1 года коммерческой разработки. Умение структурно мыслить, разбивать проект. Создание мониторингов"
    )


# Тест класса Vacancy (один из ключей salary равен None)
def test_vacancy_two(second_vacancy):
    assert second_vacancy.id == "116380094"
    assert second_vacancy.name == "Сторож (вахтер)"
    assert second_vacancy.city == "Ярославль"
    assert second_vacancy.salary == {"from": 25000, "to": 0, "currency": "RUR"}
    assert second_vacancy.url == "https://hh.ru/vacancy/116380094"
    assert (
        second_vacancy.description
        == "Без предъявления требований к квалификации.\n1. Контроль выноса материальных ценностей из..."
    )


# Тест класса Vacancy (весь salary равен None)
def test_vacancy_three(third_vacancy):
    assert third_vacancy.salary == {"from": 0, "to": 0, "currency": ""}


# Тестирование метода Vacancy.dict - получения словаря из Vacancy
def test_vacancy_dict(third_vacancy):
    assert third_vacancy.dict() == {
        "id": "116451181",
        "name": "Junior Java-разработчик",
        "city": "Москва",
        "salary": {"from": 0, "to": 0, "currency": ""},
        "url": "https://hh.ru/vacancy/116451181",
        "description": "Умение быстро разбираться в коде Java (Spring). Хорошее знание SQL.",
    }


# Тестирование строкового представления класса Vacancy (маг. метод __str__)
def test_vacancy_str(first_vacancy):
    assert (
        str(first_vacancy) == "ID: 116455408, Вакансия: Python-разработчик, Город: Москва,"
        " Зарплата: 80000-105000 RUR, url: https://hh.ru/vacancy/116455408"
    )


# Тестирование метода сравнения вакансий по зарплате на равенство
def test_equality(first_vacancy, second_vacancy, third_vacancy):
    third_vacancy.salary = {"from": 80000, "to": 0, "currency": "RUR"}
    assert not first_vacancy == second_vacancy
    assert first_vacancy == third_vacancy


# Тестирование метода сравнения вакансий по зарплате на меньше или равно
def test_less(first_vacancy, second_vacancy, third_vacancy):
    third_vacancy.salary = {"from": 80000, "to": 0, "currency": "RUR"}
    assert not first_vacancy <= second_vacancy
    assert first_vacancy <= third_vacancy


# Тестирование метода сравнения вакансий по зарплате на больше или равно
def test_greater(first_vacancy, second_vacancy, third_vacancy):
    third_vacancy.salary = {"from": 80000, "to": 0, "currency": "RUR"}
    assert first_vacancy >= second_vacancy
    assert first_vacancy >= third_vacancy
