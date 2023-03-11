class Solution:
    def longestPalindrome(self, s: str) -> str:
        # output: longest palindromic substring in s
        # input: string s
        # constraints:
            # 1 <= s.length <= 1000
            # s consist of only digits and English letters.
        # edge cases:
            # s len is never 0
            # digits and english letters (doesn't really matter since we'd be checking equality across all chars)
            # can have multiple valid answers
            # need to return string itself
        
        if len(s) == 1: return s
        
        output = ""
        output_len = 0

        for i in range(len(s)):
            
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > output_len:
                    output = s[left:right + 1]
                    output_len = right - left + 1
                
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > output_len:
                    output = s[left:right + 1]
                    output_len = right - left + 1
                
                left -= 1
                right += 1
        
        return output