import random
import time


class Solution:
    def missing_number(self, nums: list[int]):
        n = 1
        while n < len(nums):
            for i in range(len(nums) - n):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            n += 1
        for num in range(nums[-1]):
            if num not in nums:
                return num
        return nums[-1]+1



test_1 = [0, 1]
start_time = time.time()
print(Solution().missing_number(test_1))
print(time.time() - start_time)
