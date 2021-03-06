#
# from typing import List
#
# def comb_sort(numbers: List[int]):
#     len_numbers = len(numbers)
#     gap = len_numbers
#     swapped = True
# # swappedで最後の週のsortの判定
#     while gap != 1 or swapped:
#         gap = int(gap/1.3)
#         if gap < 1:
#             gap = 1
#         swapped = False
#         for i in range(0, len_numbers - gap):
#             if numbers[i] > numbers[i + gap]:
#                 numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
#                 swapped = True
#     return numbers
#
# if __name__ == '__main__':
#     import random
#     nums = [random.randint(0, 1000) for i in range(10)]
#     print(comb_sort(nums))
from typing import List

def comb_sort(numbers: List[int]):
    length_numbers = len(numbers)
    gap = length_numbers
    swapped = True
    while gap != 1 or swapped:
        swapped = False
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        for i in range(0, length_numbers - gap):
            if numbers[i] > numbers[i+gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                swapped = True
    return numbers


 if __name__ == '__main__':
     import random
     nums = [random.randint(0, 1000) for i in range(10)]
     print(nums)
     print(comb_sort(nums))