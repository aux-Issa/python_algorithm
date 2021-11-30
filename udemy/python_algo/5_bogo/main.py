import random
from typing import List

#
# def in_order(numbers: List[int]) -> bool:
#     print('hello')
#     return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
#     # for i in range(len(numbers)-1):
#     #     if numbers[i] > numbers[i+1]:
#     #         return False
#     # return True
#
#
# def bogo_sort(numbers: List[int]) -> List[int]:
#     while not in_order(numbers):
#         random.shuffle(numbers)
#     return numbers
#
#
# if __name__ == '__main__':
#     nums = [random.randint(0, 1000) for _ in range(10)]
#     print(bogo_sort(nums))

def in_order(numbers: List[int]) -> bool:
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False
    return True

def bogo_sort(numbers: List[int]) -> List[int]:
    # whileの条件式がtrueになるまでシャッフルし続ける
    while not in_order(numbers):
        random.shuffle(numbers)
        print(numbers)
    return numbers

if __name__ == '__main__':
    print(bogo_sort([3,5,4,2,9,6,7,4,2]))

