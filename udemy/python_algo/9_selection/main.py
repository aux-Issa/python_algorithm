from typing import List

def selection_sort(numbers: List[int]):
    length_num = len(numbers)
    for i in range(length_num):
        temp_min_index = i
        for j in range(i+1, length_num):
            if numbers[temp_min_index] > numbers[j]:
                temp_min_index = j
        numbers[i], numbers[temp_min_index] = numbers[temp_min_index], numbers[i]
    return numbers

if __name__ == '__main__':
    import random
    numbers = [random.randint(0, 1000) for i in range(10)]
    print(numbers)
    print(selection_sort(numbers))

