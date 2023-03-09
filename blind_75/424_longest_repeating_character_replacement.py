class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # output:
            # longest substr length containing same letter after performing k changes AT MOST
        # input:
            # string s, int k, where s is string to mutate and k is changing to uppercase char
        # constraints:
            # 1 <= s.length <= 105
            # s consists of only uppercase English letters.
            # 0 <= k <= s.length
        # edge cases:
            # no empty strings
            # k may be length of str; in this case return substr eq length of string

        # initialize window (left & right)

        left = 0
        char_tracker = {}
        max_len = 0

        for right in range(len(s)):
            right_char = s[right]
            window_len = right - left + 1
            char_tracker[right_char] = char_tracker.get(right_char, 0) + 1

            # if something:
            if window_len - max(char_tracker.values()) <= k:
                # compare max_len to something
                max_len = max(max_len, window_len)
            else:
                # decrement s[left] from char_tracker
                char_tracker[s[left]] -= 1
                # increment left
                left += 1
            
        return max_len

