class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        # output: substring in which every char in t is in S
        # input: s (len m), t (len n) both strings
        # constraints:
            # m == s.length
            # n == t.length
            # 1 <= m, n <= 105
            # s and t consist of uppercase and lowercase English letters.
        # edge cases:
            # answer will be unique (only need to look for one)

        t_dict = {}
        s_dict = {}
        left = 0
        output = ""

        if len(t) > len(s): return ""
        
        # iterate through t string
        for i in range(len(t)):
            # add all chars to t_dict, with keys as chars and vals as occurrences
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
            # add all chars in s string to s_dict; same as above but add len(t) chars of s string
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        
        # if s_dict == t_dict
        if s_dict == t_dict:
            # set output to slice(len(t))
            output = s[0:len(t)]
        
        # iterate through s string, with right pointer starting at len(t) - 1
        for right in range(len(t), len(s)):
            # make copy of t_dict
            t_dict_copy = t_dict.copy()
            # add s char at right to s_dict or increment by 1
            s_dict[s[right]] = s_dict.get(s[right], 0) + 1
            # iterate through s_dict
            for char in s_dict:
                # subtract the val at each char in s_dict from t_dict.copy() val
                if s_dict[char] in t_dict_copy:
                    t_dict_copy[s_dict[char]] -= 1

            # if all(val == 0 for val in t_dict) and length of slice(left:right + 1) is less than len(output)
            if all(val == 0 for val in t_dict) and len(output) > len(s[left:right + 1]):
                # set output to slice(left : right + 1)
                output = len(s[left:right + 1])
            
            # if output is not empty
            if output:
                # increment left
                left += 1
        
        return output


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        # output: substring in which every char in t is in S
        # input: s (len m), t (len n) both strings
        # constraints:
            # m == s.length
            # n == t.length
            # 1 <= m, n <= 105
            # s and t consist of uppercase and lowercase English letters.
        # edge cases:
            # answer will be unique (only need to look for one)

        t_dict = {}
        s_dict = {}
        left = 0
        output = ""
        is_substr = True

        if len(t) > len(s): return ""
        
        # iterate through t string
        for i in range(len(t)):
            # add all chars to t_dict, with keys as chars and vals as occurrences
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
            # add all chars in s string to s_dict; same as above but add len(t) chars of s string
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1

        # if s_dict == t_dict
        if s_dict == t_dict:
            # set output to slice(len(t))
            output = s[0:len(t)]
        
        # iterate through s string, with right pointer starting at len(t) - 1
        for right in range(len(t), len(s)):
            is_substr = True
            # make copy of t_dict
            # t_dict_copy = t_dict.copy()
            # add s char at right to s_dict or increment by 1
            s_dict[s[right]] = s_dict.get(s[right], 0) + 1
            # iterate through s_dict
            for char in t_dict:
                # subtract the val at each char in s_dict from t_dict.copy() val
                if char in s_dict and s_dict[char] < t_dict[char]: 
                    # t_dict_copy[char] -= 1
                    is_substr = False
                    break

            # if all(val == 0 for val in t_dict) and length of slice(left:right + 1) is less than len(output)
            if is_substr:
                # set output to slice(left : right + 1)
                output = s[left:right + 1] 
                # if len(s[left:right + 1]) < len(output) else output
            
            # if output is not empty
            if output:
                s_dict[s[left]] -= 1
                # increment left

                left += 1
        
        return output


class Solution3:
    def minWindow(self, s: str, t: str) -> str:
        # output: substring in which every char in t is in S
        # input: s (len m), t (len n) both strings
        # constraints:
            # m == s.length
            # n == t.length
            # 1 <= m, n <= 10^5
            # s and t consist of uppercase and lowercase English letters.
        # edge cases:
            # answer will be unique (only need to look for one)
        
        if len(t) == 0: return ""

        count_dict, window = {}, {}

        for i in t:
            count_dict[i] = count_dict.get(i, 0) + 1

        output, output_len = [-1,-1], float("infinity")
        left = 0
        have, need = 0, len(count_dict)

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in count_dict and window[s[right]] == count_dict[s[right]]:
                have += 1
            
            while have == need:
                if right - left + 1 < output_len:
                    output = [left, right]
                    output_len = right - left + 1
                
                window[s[left]] -= 1

                if s[left] in count_dict and window[s[left]] < count_dict[s[left]]:
                    have -= 1
                
                left += 1

        return s[output[0]:output[1] + 1] if output_len != float("infinity") else ""


