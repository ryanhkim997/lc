class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # output: length as an int of longest substr (contiguous)
        # input: s as a string
        # constraints:
            # 0 <= s.length <= 5 * 104
            # s consists of English letters, digits, symbols and spaces.
        # edge cases:
            # empty string
            # spaces

        if len(s) <= 1:
            return len(s)
        
        left = 0
        right = 0
        char_map = {}
        max_length = 0

        while right < len(s) and left < len(s):
            right_char = s[right]
            if right_char in char_map:
                left = max(left, char_map[right_char] + 1)
            
            char_map[right_char] = right
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length