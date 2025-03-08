class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        for ex_i in range(len(nums)):
            first_elem = nums[ex_i]
            for in_i in range(ex_i + 1, len(nums)):
                second_elem = nums[in_i]
                if first_elem + second_elem == target:
                    return [ex_i, in_i]




test_1 = Solution().two_sum(nums=[2,7,11,15], target=9)
test_2 = Solution().two_sum(nums=[3,2,4], target=6)
test_3 = Solution().two_sum(nums=[3,3], target=6)
print(test_1)
print(test_2)
print(test_3)
