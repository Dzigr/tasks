from typing import Dict, Any, List
import json
import pytest
import os


def find_differences(
        json_old: Dict[str, Any],
        json_new: Dict[str, Any],
        diff_keys: List[str]
) -> Dict[str, Any]:
    result = {}
    sorted_keys = sorted(set.union(set(json_old), set(json_new)))
    for key in sorted_keys:
        if json_old.get(key) != json_new.get(key) and key in diff_keys:
            result[key] = json_new.get(key)
        elif all(
                [isinstance(json_old.get(key), dict),
                 isinstance(json_new.get(key), dict)],
        ):
            nested_diff = find_differences(
                json_old.get(key),
                json_new.get(key),
                diff_keys,
            )
            if nested_diff:
                result.update(nested_diff)

    return result


@pytest.fixture
def json_load():
    file_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'test_data.json')
    with open(file_path, "r") as f:
        return json.load(f)


def test_find_differences_same_json(json_load):
    new_data = json_load.get('new')
    diff_keys = ['services', 'staff', 'datetime']
    expected_result = {}
    assert find_differences(new_data, new_data, diff_keys) == expected_result


def test_find_differences_different_json(json_load):
    new_data = json_load.get('new')
    old_data = json_load.get('old')
    diff_keys = ['services', 'staff', 'datetime']
    expected_result = {
        'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500}],
        'datetime': '2022-01-25T13:00:00+03:00',
    }
    assert find_differences(old_data, new_data, diff_keys) == expected_result
