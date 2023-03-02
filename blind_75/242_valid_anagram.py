class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # output:
            # true if t and s are anagrams
        # input: s (str), t (str)
        # constraints:
            # 1 <= s.length, t.length <= 5 * 104
            # s and t consist of lowercase English letters.
        # edge cases:
            # all lowercase, no empty str
        
        # could sort both strings and compare -> O(nlog(n) + mlog(m)) time, O(n + m) space
        # could store in hash table and compare -> O(n + m) time, O(1) space
        # prime factor decomposition -> O(n + m) time, O(1) space

        if len(s) != len(t):
            return False

        tracker = {}

        for i in s:
            if i in tracker:
                tracker[i] += 1
            else:
                tracker[i] = 1
        
        for i in t:
            if i not in tracker or tracker[i] == 0:
                return False
            else:
                tracker[i] -= 1
        
        return True