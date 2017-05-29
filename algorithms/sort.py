from typing import List

from copy import copy


def bubble_sort(data: List):
    data = copy(data)

    for _ in range(len(data)):
        for i in range(1, len(data)):
            if data[i-1] > data[i]:
                data[i-1], data[i] = data[i], data[i-1]

    return data