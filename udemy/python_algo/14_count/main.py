# from typing import List
#
#
# def counting_sort(numbers: List[int]) -> List[int]:
#     max_num = max(numbers)
#     counts = [0] * (max_num + 1)
#     result = [0] * len(numbers)
#
#     for num in numbers:
#         counts[num] += 1
#
#     for i in range(1, len(counts)):
#         counts[i] += counts[i-1]
#
#     i = len(numbers) - 1
#     while i >= 0:
#         index = numbers[i]
#         result[counts[index]-1] = numbers[i]
#         counts[index] -= 1
#         i -= 1
#
#     return result
from typing import List

def counting_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    # numbers内の特定の数字の登場をカウントする配列
    counts = [0]*(max_num + 1)
    # sort後の結果を示す配列
    results = [0]*len(numbers)
    # numbersの各要素をカウントし，counterに格納
    for num in numbers:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    i = len(numbers) - 1
    while i >= 0:
        index = numbers[i]
        results[counts[index]-1] = numbers[i]
        counts[index] -= 1
        i -= 1
    return results

# if __name__ == '__main__':
#     import random
#     nums = [random.randint(0, 1000) for _ in range(10)]
#     print(counting_sort(nums))
