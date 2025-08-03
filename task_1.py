from typing import List, Tuple

def find_min_max(arr: List[int]) -> Tuple[int, int]:
    if len(arr) == 1:
        return arr[0], arr[0]

    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])
    return min(left_min, right_min), max(left_max, right_max)
