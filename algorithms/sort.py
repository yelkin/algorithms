from typing import List

from copy import copy


def bubble_sort(data: List) -> List:
    data = copy(data)

    for _ in range(len(data)):
        for i in range(1, len(data)):
            if data[i-1] > data[i]:
                data[i-1], data[i] = data[i], data[i-1]

    return data


def quick_sort(data: List) -> List:
    data = copy(data)

    if len(data) < 2:
        return data

    middle = data[0]
    left = []
    right = []

    for i in data[1:]:
        if i < middle:
            left.append(i)
        else:
            right.append(i)
    left.append(middle)

    return quick_sort(left) + quick_sort(right)