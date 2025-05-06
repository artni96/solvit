class Solution:
    def find_closest_elements(self, arr: list[int], k: int, x: int) -> list[int]:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                if mid == 0:
                    return arr[:k]
                elif mid == len(arr) - 1:
                    return arr[len(arr) - k:]
                else:
                    if mid - (k // 2) <= 0:
                        inner_left = 0
                    elif mid + (k // 2) >= len(arr):
                        inner_left = len(arr) - k
                    else:
                        inner_left = mid - k
                    result = {
                        "left_dif": abs(arr[inner_left] - arr[mid]),
                        "right_dif": abs(arr[inner_left + k] - arr[mid]),
                        "left": inner_left,
                    }
                    while inner_left <= mid and inner_left + k <= len(arr) - 1:
                        if (abs(arr[inner_left] - arr[mid]) <= result["left_dif"]
                                and abs(arr[inner_left + k] - arr[mid]) <= result["right_dif"]):
                            # print(f"{arr[inner_left:inner_left+k]}, mid={arr[mid]}")
                            result["left_dif"], result["right_dif"], result["left"] = (
                                abs(arr[inner_left] - arr[mid]), abs(arr[inner_left + k] - arr[mid]), inner_left
                            )
                        inner_left += 1
                    return arr[result["left"]:result["left"]+k]
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if len(arr) > 1:
                if abs(arr[mid - 1] - x) < abs(arr[mid] - x):
                    mid -= 1
                elif abs(arr[mid] - x) < abs(arr[mid + 1] - x):
                    mid += 1
            if mid <= 0:
                return arr[:k]
            elif mid >= len(arr):
                return arr[len(arr) - k:]
            else:
                if mid - (k // 2) <= 0:
                    inner_left = 0
                elif mid + (k // 2) >= len(arr):
                    inner_left = len(arr) - k
                else:
                    inner_left = mid - k
                result = {
                    "left_dif": abs(arr[inner_left] - arr[mid]),
                    "right_dif": abs(arr[inner_left + k] - arr[mid]),
                    "left": inner_left,
                }
                while inner_left <= mid and inner_left + k <= len(arr) - 1:
                    if (abs(arr[inner_left] - arr[mid]) <= result["left_dif"]
                            and abs(arr[inner_left + k] - arr[mid]) <= result[
                                "right_dif"]):
                        result["left_dif"], result["right_dif"], result["left"] = (
                            abs(arr[inner_left] - arr[mid]),
                            abs(arr[inner_left + k] - arr[mid]), inner_left
                        )
                    inner_left += 1
                return arr[result["left"]:result["left"] + k]


test_arr_1 = [1, 2, 3, 4, 5]
test_k_1 = 4
test_x_1 = 3
print(Solution().find_closest_elements(test_arr_1, test_k_1, test_x_1))
test_arr_2 = [1, 1, 2, 3, 4, 5]
test_k_2 = 4
test_x_2 = - 1
print(Solution().find_closest_elements(test_arr_2, test_k_2, test_x_2))
test_arr_3 = [1, 1, 1, 10, 10, 10]
test_k_3 = 1
test_x_3 = 9
print(Solution().find_closest_elements(test_arr_3, test_k_3, test_x_3))
test_arr_4 = [0, 1, 1, 1, 2, 3, 6, 7, 8, 9]
test_k_4 = 4
test_x_4 = 1
print(Solution().find_closest_elements(test_arr_4, test_k_4, test_x_4))
test_arr_4 = [0, 1, 3, 3, 4, 4, 6, 7, 8, 9]
test_k_4 = 4
test_x_4 = 3
print(Solution().find_closest_elements(test_arr_4, test_k_4, test_x_4))
test_arr_5 = [1]
test_k_5 = 1
test_x_5 = 0
print(Solution().find_closest_elements(test_arr_5, test_k_5, test_x_5))
test_arr_6 = [-2,-1,1,2,3,4,5]
test_k_6 = 7
test_x_6 = 3
print(Solution().find_closest_elements(test_arr_6, test_k_6, test_x_6))