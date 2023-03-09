class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # input:
            # s, the str to search for anagrams
            # p, the str to use to create anagrams
        # output:
            # array of all start indices of p's anagrams in s
        # constraints:
            # 1 <= s.length, p.length <= 3 * 104
            # s and p consist of lowercase English letters.
        # edge cases:
            # never given empty string
            # lowercase english letters

        # could sort p string first, then sort s - len(p) substrings for len(s) - len(p) -> plog(p) + slog(s) * (s - p)
        output = []
        p_dict = {}
        s_dict = {}
        left = 0

        if len(p) > len(s):
            return output


        for i in range(len(p)): # O(p) time
            p_dict[p[i]] = p_dict.get(p[i], 0) + 1 # constant time for dict insertion
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1

        if s_dict == p_dict: output.append(0)
        
        for right in range(len(p), len(s)): # O(s - p) time
            
            s_dict[s[right]] = s_dict.get(s[right], 0) + 1
            s_dict[s[left]] -= 1

            if s_dict[s[left]] == 0:
                del s_dict[s[left]]
            
            left += 1

            if s_dict == p_dict:
                output.append(left)
            


        return output

                


