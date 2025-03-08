class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        max_length = 0
        s_length = len(s)
        tail_i = 0
        head_i = tail_i + 1
        while head_i <= s_length:
            current_section = s[tail_i:head_i]
            if len(set(s[tail_i:head_i + 1])) == len(s[tail_i:head_i+1]):
                head_i += 1
            elif len(set(s[tail_i+1:head_i])) == len(s[tail_i+1:head_i]):
                tail_i += 1
            if len(current_section) > max_length:
                max_length = len(current_section)
        return max_length

test_1 = "abcabcbb"
test_2 = "bbbbb"
test_3 = "pwwkew"
test_4 = "aab"
test_5 = "dvdf"
test_6 = ""
test_7 = " "
print(Solution().length_of_longest_substring(test_1))
print(Solution().length_of_longest_substring(test_2))
print(Solution().length_of_longest_substring(test_3))
print(Solution().length_of_longest_substring(test_4))
print(Solution().length_of_longest_substring(test_5))
print(Solution().length_of_longest_substring(test_6))
print(Solution().length_of_longest_substring(test_7))



