class Solution:
    def find_closest_elements(self, arr: list[int], k: int, x: int) -> list[int]:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                break
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if abs(arr[mid - 1] - x) <= abs(arr[mid] - x):
                mid -= 1
            elif mid < len(arr) - 1:
                if abs(arr[mid + 1] - x) < abs(arr[mid] - x):
                    mid += 1
        if mid <= 0:
            return arr[:k]
        elif mid >= len(arr) - 1:
            return arr[len(arr)-k:]
        left_pivot = mid - k + 1
        right_pivot = mid
        if left_pivot < 0:
            left_pivot = 0
            right_pivot = mid + abs(mid - k + 1)
        result_sum_dif = sum([abs(x - elem) for elem in arr[left_pivot:right_pivot+1]])
        result_left_pivot = left_pivot
        result_right_pivot = right_pivot
        while left_pivot <= mid and right_pivot <= len(arr) - 1:
            cur_sum_dif = sum([abs(x - elem) for elem in arr[left_pivot:right_pivot+1]])
            if cur_sum_dif < result_sum_dif:
                result_left_pivot = left_pivot
                result_right_pivot = right_pivot
                result_sum_dif = cur_sum_dif
            left_pivot += 1
            right_pivot += 1
        return arr[result_left_pivot: result_right_pivot + 1]


test_arr_1 = [1, 2, 3, 4, 5]
test_k_1 = 4
test_x_1 = 3
print(Solution().find_closest_elements(test_arr_1, test_k_1, test_x_1))
# assert result == [1, 2, 3, 4]
# print(Solution().find_closest_elements(test_arr_1, test_k_1, test_x_1))
test_arr_1 = [1, 4, 4, 4, 6, 7, 8]
test_k_1 = 5
test_x_1 = 5
print(Solution().find_closest_elements(test_arr_1, test_k_1, test_x_1))
test_arr_2 = [1, 1, 2, 3, 4, 5]
test_k_2 = 4
test_x_2 = - 1
# print(Solution().find_closest_elements(test_arr_2, test_k_2, test_x_2))
test_arr_3 = [1, 1, 1, 10, 10, 10]
test_k_3 = 1
test_x_3 = 9
# print(Solution().find_closest_elements(test_arr_3, test_k_3, test_x_3))
test_arr_4 = [0, 1, 1, 1, 2, 3, 6, 7, 8, 9]
test_k_4 = 5
test_x_4 = 9
print(Solution().find_closest_elements(test_arr_4, test_k_4, test_x_4))
test_arr_4 = [0, 1, 3, 3, 4, 4, 6, 7, 8, 9]
test_k_4 = 4
test_x_4 = 3
# print(Solution().find_closest_elements(test_arr_4, test_k_4, test_x_4))
# test_arr_5 = [1]
# test_k_5 = 1
# test_x_5 = 0
# print(Solution().find_closest_elements(test_arr_5, test_k_5, test_x_5))
# test_arr_6 = [-2,-1,1,2,3,4,5]
# test_k_6 = 7
# test_x_6 = 3
# print(Solution().find_closest_elements(test_arr_6, test_k_6, test_x_6))
test_arr_1 = [0, 2, 2, 3, 4, 6, 7, 8, 9, 9]
test_k_1 = 4
test_x_1 = 5
print(Solution().find_closest_elements(test_arr_1, test_k_1, test_x_1))
test_arr_1 = [1, 1, 2, 2, 2, 2, 2, 3, 3]
test_k_1 = 3
test_x_1 = 3
print(Solution().find_closest_elements(test_arr_1, test_k_1, test_x_1))
test_arr_1 = [1, 5, 10, 12, 13]
test_k_1 = 1
test_x_1 = 9
print(Solution().find_closest_elements(test_arr_1, test_k_1, test_x_1))
test_arr_1 = [3,5,8,10]
test_k_1 = 2
test_x_1 = 15
print(Solution().find_closest_elements(test_arr_1, test_k_1, test_x_1))