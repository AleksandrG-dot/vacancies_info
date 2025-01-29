from src.api_vacancies import HeadHunterAPI
from src.utils import get_top_n_vacancies, vacancies_by_keyword
from src.working_with_files import WorkingFileVacanciesJSON


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    # Создание экземпляра класса для работы с API hh.ru
    hh_api = HeadHunterAPI()

    # Создание экземпляра класса для работы с файлом
    work_file = WorkingFileVacanciesJSON("data/vacancies.json")

    while True:
        print("-" * 120)
        print(
            """1. Поиск вакансии на hh.ru
2. Вывести топ N вакансий по зарплате
3. Поиск вакансий по ключевому слову
4. Удалить вакансию по ID ( * - удалить все )
5. Завершить работу"""
        )

        user_choice = input("Введите номер пункта: ")

        if user_choice == "1":
            search_query = input("Введите поисковый запрос: ")
            vacancies = hh_api.get_vacancies(search_query, 5)
            count = work_file.add_to(vacancies)
            print(
                f"Найдено {len(vacancies)} вакансий. В файл добавлено {count} вакансий."
                f" Дубликатов: {len(vacancies) - count}"
            )
        elif user_choice == "2":
            user_choice = int(input("Введите количество вакансий N: "))
            top_n = get_top_n_vacancies(work_file.get_data, user_choice)
            for vac in top_n:
                print(vac)
        elif user_choice == "3":
            user_choice = input("Введите слово для поиска в описании вакансии: ")
            filter_vacancy = vacancies_by_keyword(work_file.get_data, user_choice)
            print(f"По запросу '{user_choice}' найдено {len(filter_vacancy)} вакансий:")
            for vac in filter_vacancy:
                print(vac)
        elif user_choice == "4":
            user_choice = input("Введите ID вакансии для удаления (* - удалить все): ")
            result = work_file.del_data(user_choice)
            print("Данные удалены успешно" if result else "!Данные НЕ удалены!")
        elif user_choice == "5":
            print("Выход из программы")
            break
        else:
            print("!ОШИБКА ввода!\n")


if __name__ == "__main__":
    user_interaction()
