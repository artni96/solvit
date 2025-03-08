class Solution:
    def reverse_string(self, s: list[str]) -> None:
        end_point = len(s) - 1
        cur_range = range((len(s) - 1) // 2 + 1)
        for elem in cur_range:
            s[end_point], s[elem] = s[elem], s[end_point]
            end_point -= 1
        return s


test_1 = ["h","e","l","l","o"]
print(Solution().reverse_string(test_1))
