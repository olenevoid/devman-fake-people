from file_operations import render_template
from faker import Faker
import random
from os import path, makedirs


charsheet_path = 'charsheet.svg'

charsheet_folder_name = 'charsheets'

skills_list = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
]

runic_skills = []

runic_letters = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


def get_random_person() -> dict:
    fake = Faker("ru_RU")
    last_name, first_name, _ = fake.name().split(' ')
    job = fake.job()
    town = fake.city()
    return {'first_name': first_name, 'last_name': last_name,
            'job': job, 'town': town}


def get_random_stats(min: int = 3, max: int = 18) -> dict:
    stats = {'strength': 0, 'agility': 0, 'endurance': 0,
             'intelligence': 0, 'luck': 0}
    for key, _ in stats.items():
        stats[key] = random.randint(min, max)
    return stats


def get_random_skills() -> dict:
    skills = {'skill_1': '', 'skill_2': '', 'skill_3': ''}
    skills_sample = random.sample(runic_skills, 3)
    for key, _ in skills.items():
        skills[key] = skills_sample.pop()
    return skills


def get_runic_text(text: str) -> str:
    for char in list(text):
        if char in runic_letters:
            text = text.replace(char, runic_letters[char])
    return text


def main():
    if not path.exists(charsheet_folder_name):
        makedirs(charsheet_folder_name)

    for skill in skills_list:
        runic_skills.append(get_runic_text(skill))

    for _ in range(0, 10, 1):
        character = {**get_random_person(),
                     **get_random_stats(),
                     **get_random_skills()}
        filename = f'{character["last_name"]}_{character["first_name"]}.svg'
        file_path = path.join(charsheet_folder_name, filename)
        render_template(charsheet_path,
                        file_path,
                        character)


if __name__ == '__main__':
    main()
