from src.vacancy import Vacancy


def get_top_n_vacancies(data: list[Vacancy], n: int) -> list[Vacancy]:
    """Функция выводит топ N вакансий по зарплате с ключом from"""
    if n > len(data):
        n = len(data)
    sorted_tmp = sorted(data, key=lambda Vacancy: Vacancy.salary.get("from"), reverse=True)
    result = sorted_tmp[:n]
    return result


def vacancies_by_keyword(data: list[Vacancy], keyword: str) -> list[Vacancy]:
    """Функция фильтрует список вакансий по слову keyword в описании и
    возвращает отфильтрованный список"""
    # !можно реализовать через filter()
    search_list = []
    keyword_low = keyword.lower()
    for vac in data:
        if keyword_low in str(vac).lower() + vac.description.lower():
            search_list.append(vac)
    return search_list
