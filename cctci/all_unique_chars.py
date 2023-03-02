# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# easiest way is to store entries in hash map, check if char exists and return false if it's hit;
    # space: O(n)
    # time: O(n)

class Char:
    def all_unique_chars(self, s: str) -> bool:
        hash = {}
        for char in s:
            if hash[char]:
                return False
            hash[char] = True
        return True

# loop through string
    # 

    def all_unique_chars_less_space(self, s: str) -> bool:
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    return False
        return True