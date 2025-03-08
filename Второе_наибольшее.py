class Solution:
    def get_second_largest(self, nums: list[int]) -> int:
        if len(set(nums)) == 1:
            return -1
        swapped = True
        unique_nums = list(set(nums))
        while swapped:
            swapped = False
            last_index = len(unique_nums) - 1
            for cur_index in range(last_index):
                if unique_nums[cur_index] > unique_nums[cur_index + 1]:
                    unique_nums[cur_index], unique_nums[cur_index + 1] = unique_nums[cur_index + 1], unique_nums[cur_index]
                    swapped = True
        return unique_nums[-2]


test_1 = [12, 35, 1, 10, 34, 1]
test_2 = [10, 5, 10]
test_3 = [10, 10, 10]
print(Solution().get_second_largest(test_1))
print(Solution().get_second_largest(test_2))
print(Solution().get_second_largest(test_3))
