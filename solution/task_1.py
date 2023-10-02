from typing import List


def verify_data(template: str, keys: List[str]) -> str:
    if template.count("{") != template.count("}"):
        return "Ошибка: непарное количество открывающих и закрывающих скобок"
    for key in keys:
        if "{" + key + "}" not in template:
            return f"Ошибка: ключ {key} отсутствует в тексте"

    return template


def test_verify_data_missing_key():
    template = '''{name}, ваша запись изменена:
    ⌚️ {day_month} в {start_time}
    👩 {Master}
    Услуги:
    {services}
    управление записью {record_link}'''
    keys = ['name', 'day_month', 'start_time', 'master', 'services']
    expected_error = "Ошибка: ключ master отсутствует в тексте"
    assert verify_data(template, keys) == expected_error


def test_verify_data_mismatched_brackets():
    template = '''{name}, ваша запись изменена:
    ⌚️ {day_month} в {start_time}
    👩 {master}
    Услуги:
    {services
    управление записью {record_link}'''
    keys = ['name', 'day_month', 'day_of_week', 'start_time', 'master', 'services']
    expected_error = "Ошибка: непарное количество открывающих и закрывающих скобок"
    assert verify_data(template, keys) == expected_error
