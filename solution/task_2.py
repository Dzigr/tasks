from collections import Counter
from typing import List, Tuple


def group_versions(data: List[Tuple[str, int]]) -> List[List]:
    counts = Counter(tuple(pair) for pair in data)
    grouped_versions = [[*pair, count] for pair, count in counts.items()]

    return grouped_versions


def test_group_versions_empty_data():
    data = []
    expected_result = []
    assert group_versions(data) == expected_result


def test_group_versions_single_element():
    data = [('665587', 2)]
    expected_result = [['665587', 2, 1]]
    assert group_versions(data) == expected_result


def test_group_versions_multiple_elements():
    data = [
        ('665587', 2),
        ('669532', 1),
        ('669532', 1),
        ('665587', 2),
        ('665587', 2)
    ]
    expected_result = [
        ['665587', 2, 3],
        ['669532', 1, 2]
    ]
    assert group_versions(data) == expected_result
