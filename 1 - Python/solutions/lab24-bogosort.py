# lab 24: bogosort, not using built-in functions

import random
import time


# generate a random list of n values each between 1 and 99
def random_list(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(1, 99))
    return nums


# re-arrange a list by swapping pairs of elements
def shuffle(nums):
    for i in range(len(nums)):
        j = random.randint(0, len(nums)-1)  # pick a random index

        # the non-pythonic way of swapping
        # t = nums[i]
        # nums[i] = nums[j]
        # nums[j] = t

        # the pythonic way of swapping
        nums[i], nums[j] = nums[j], nums[i]


# check if a list is sorted, look at individual pairs
def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def get_time():
    return int(round(time.time() * 1000))

def bogosort(nums):
    count = 0
    start_time = get_time()
    while not is_sorted(nums):  # loop until the list is sorted
        shuffle(nums)
        print(''.join([str(num) for num in nums]))
        count += 1
    end_time = get_time()
    time_taken = end_time - start_time
    print(f'total time taken: {time_taken/1000} seconds')
    print(f'time per step:    {time_taken/1000/count} second')
    print(f'steps:            {count}')


nums = random_list(10)
print(nums)
bogosort(nums)
print(nums)