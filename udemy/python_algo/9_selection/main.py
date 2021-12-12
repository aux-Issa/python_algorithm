# from typing import List
#
#
# def selection_sort(numbers: List[int]) -> List[int]:
#     for i in range(len(numbers)):
#         min_idx = i
#         for j in range(i+1, len(numbers)):
#             if numbers[min_idx] > numbers[j]:
#                 min_idx = j
#
#         numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
#     return numbers
#
#
# if __name__ == '__main__':
#     import random
#     nums = [random.randint(0, 1000) for _ in range(10)]
#     print(selection_sort(nums))

from typing import List

def selection_sort(numbers: List[int]):
    length_num = len(numbers)
    for i in range(length_num):
        min_index = i
        for j in range(i+1, length_num):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

if __name__ == '__main__':
    import random
    numbers = [random.randint(0, 1000) for _ in range(10)]
    print(numbers)
    print(selection_sort(numbers))
