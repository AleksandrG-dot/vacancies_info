from unittest.mock import patch

from src.api_vacancies import HeadHunterAPI


# Тестирование класса получения вакансий HeadHunterAPI()
@patch("src.api_vacancies.requests.get")
def test_get_vacancies(moc_get, response_hh):
    hh_api = HeadHunterAPI()
    moc_get.return_value.status_code = 200
    moc_get.return_value.json.return_value = response_hh

    response = hh_api.get_vacancies("волшебник", 3)
    assert len(response) == 3
    assert (
        str(response[0])
        == "ID: 115804650, Вакансия: Специалист по подбору пары (Мачмейкер), Город: Тамбов, Зарплата: 30000-60000 "
        + "RUR, url: https://hh.ru/vacancy/115804650"
    )
    assert (
        str(response[1])
        == "ID: 110639788, Вакансия: Педагог по актерскому мастерству, Город: Москва, Зарплата: 0-0 , "
        + "url: https://hh.ru/vacancy/110639788"
    )
    assert (
        str(response[2])
        == "ID: 112305768, Вакансия: Волшебник продаж, Город: Москва, Зарплата: 300000-0 RUR,"
        + " url: https://hh.ru/vacancy/112305768"
    )

    moc_get.assert_called_once_with(
        "https://api.hh.ru/vacancies",
        headers={"User-Agent": "HH-User-Agent"},
        params={"text": "волшебник", "page": 0, "per_page": 3},
    )
