class Solution:
    def is_palindrome(self, s: str) -> bool:
        result_string = "".join([elem.lower() for elem in s if elem.isalpha() is True or elem.isdigit()])
        return result_string == result_string[::-1]


test_1 = "A man, a plan, a canal: Panama"
test_2 = "0P"
print(Solution().is_palindrome(test_2))
# print(type(" "))