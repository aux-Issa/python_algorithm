# from typing import List
# import random
#
# # 12/3 I  couldn't solve
# def bubble_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(len_numbers):
#         for j in range(len_numbers - 1 - i):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#
#     return numbers
#
#
# if __name__ == '__main__':
#     nums = [random.randint(0, 1000) for i in range(10)]
#     print(bubble_sort(nums))

from typing import List

def cocktail_sort(numbers: List) -> List[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
            if not swapped:
                break

        swapped = False
        end = end - 1

        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        start = start + 1

    return numbers

if __name__ = "__main__":
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(cocktail_sort(nums))