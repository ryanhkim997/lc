from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output: list of lists, inner lists are anagrams of each other
        # input: list of strs
        # constraints:
            # 1 <= strs.length <= 104
            # 0 <= strs[i].length <= 100
            # strs[i] consists of lowercase English letters.
        # edge cases:
            # all strs are the same length

        if len(strs) == 1: return [[strs[0]]]
        
        output, output_i = [], -1
        ana_tracker = {}

        # iterate through list
        for st in strs:
            # sort string at index and store in var; should be rewritten every time
            sorted_st = "".join(sorted(st))
            # if sorted string does not exist in dict
            if sorted_st not in ana_tracker:
                # add to dict with index number + 1
                output_i += 1
                output.append([st])
                ana_tracker[sorted_st] = output_i
            # else
            else:
                # append original string to output[output_i]
                output[ana_tracker[sorted_st]].append(st)

        return output