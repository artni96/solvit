def binary_search(nums: list, target: int):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_v2(nums: list, target: int):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1


test_nums = [i for i in range(3, 13)]
print(binary_search(test_nums, 14))
print(binary_search_v2(test_nums, 13))


def bubble_sort(nums: list):
    swapped = True
    tail = len(nums) - 1
    while swapped:
        swapped = False
        for i in range(tail):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        tail -= 1
    return nums


unsorted_list = [3, 2, 4, 6, 5, 9, 8, 7]
print(bubble_sort(unsorted_list))

x = 12
x %= 100
print(10%10)