class Solution:
    def get_length_of_last_word(self, s: str) -> int:
        last_word = ""
        non_alpha_symbol = False
        for char in s:
            if char.isalpha():
                if non_alpha_symbol:
                    last_word = ""
                    non_alpha_symbol = False
                last_word += char
            else:
                non_alpha_symbol = True
        return len(last_word)


test_1 = "Hello World"
test_2 = "  fly me  to  the moon  "
test_3 = "luffy is still joyboy"
print(Solution().get_length_of_last_word(test_1))
print(Solution().get_length_of_last_word(test_2))
print(Solution().get_length_of_last_word(test_3))
