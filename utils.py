import json


def load_json():
    """Загружает данные из json файла"""
    with open("candidates.json", encoding='utf-8') as f:
        return json.load(f)


def get_all():
    """Показывает всех кандидатов"""
    return load_json()


def get_by_pk(pk):
    """Возвращает кандидата по pk"""
    for candidate in load_json():
        if candidate['pk'] == pk:
            return candidate
    return "Not Found"


def get_by_skill(skill):
    """Возвращает кандидата по навыку"""
    result = []
    for candidate in load_json():
        skills = candidate['skills'].split(", ")
        if skill in skills:
            result.append(candidate)
    return result




