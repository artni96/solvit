class Solution:
    @staticmethod
    def compress(chars: list[str]) -> int:
        if len(chars):
            tail = 0
            previous_elem = chars[0]
            elem_counter = 1
            for i in range(1, len(chars)):
                if chars[i] == previous_elem:

                    if elem_counter == 1:
                        tail += 1
                    elem_counter += 1
                    if elem_counter > 9:
                        for _ in range(len(str(elem_counter))):
                            chars[tail + _] = str(str(elem_counter)[_])
                    else:
                        chars[tail] = str(elem_counter)
                else:
                    tail += len(str(elem_counter))
                    chars[tail] = chars[i]
                    elem_counter = 1
                    previous_elem = chars[i]
            print(chars[:tail + len(str(elem_counter))])
            return len(chars[:tail + len(str(elem_counter))])
        return len(chars)



test_1 = ["a", "a", "a", "b", "b", "c", "c", "c"]
test_2 = ["a" for i in range(12)]
test_3 = ["a", "b", "c"]
test_4 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
test_5 = ["a","a","a","a","a","b"]
test_6 = []
test_7 = ["a" for i in range(21)]
test_8 = ["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]
print(Solution().compress(test_1))
print(Solution().compress(test_2))
print(Solution().compress(test_3))
print(Solution().compress(test_4))
print(Solution().compress(test_5))
print(Solution().compress(test_6))
print(Solution().compress(test_7))
print(Solution().compress(test_8))
