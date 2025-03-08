class Solution:
    def is_valid_password(self, password: str) -> bool:
        password_char_list = list(password)
        non_english_symbols = False
        has_uppercase_letter = False
        has_special_symbols = False
        password_length = False
        has_numeric_symbol = False
        is_not_palindrome = False
        lowercase_symbols = list()
        for symbol in password_char_list:
            if symbol.isalpha() and not symbol.isascii():
                non_english_symbols = True
            if symbol.isalpha() and symbol.isupper() and symbol.isascii():
                has_uppercase_letter = True
            if symbol in ("_", "#", "%"):
                has_special_symbols = True
            if symbol.isnumeric():
                has_numeric_symbol = True
            password_length += 1
            lowercase_symbols.append(symbol.lower())
        if lowercase_symbols != lowercase_symbols[::-1]:
            is_not_palindrome = True
        valid_password_length = False
        if password_length >= 8:
            valid_password_length = True
        if (not non_english_symbols and has_uppercase_letter and has_special_symbols and
                has_numeric_symbol and valid_password_length and is_not_palindrome):
            return True
        return False


test_1 = "Abc1_def#"
test_2 = "Привет1_#"
test_3 = "apapa"
test_4 = "abcdefg1_"
test_5 = "Rewqa1_1aqwer"
print(Solution().is_valid_password(test_1))
print(Solution().is_valid_password(test_2))
print(Solution().is_valid_password(test_3))
print(Solution().is_valid_password(test_4))
print(Solution().is_valid_password(test_5))


