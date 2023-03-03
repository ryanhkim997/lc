class Solution:
    def isPalindrome(self, s: str) -> bool:
        # output: boolean if palindrome
        # input: s (str)
        # constraints:
            # 1 <= s.length <= 2 * 105
            # s consists only of printable ASCII characters.
        # edge cases:
            # string is never empty, but can be filled with non-alphanumeric chars
        
        st = str.lower("".join(filter(str.isalnum, s)))

        if len(st) <= 1:
            return True
        
        i = 0
        j = len(st) - 1

        while i <= j:
            if st[i] != st[j]:
                return False

            i += 1
            j -= 1

        return True