class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


test_1 = [1, 2, 3, 1]
test_3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]