class Solution:
    def isValid(self, s: str) -> bool:
        # input: string s containing chars (,),[,],{,}
        # output: true if string is valid, false if not
        # constraints:
            # 1 <= s.length <= 10^4
            # s consists of parentheses only '()[]{}'.
        # edge cases:
            # one character?
            # don't need to consider empty string

        mappings = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        tracker = []

        if len(s) % 2:
            return False

        for i in s:
            if i in mappings:
                tracker.append(i)
            else:
                if not tracker or mappings[tracker[-1]] != i:
                    return False
                tracker.pop()
        
        if len(tracker):
            return False
        
        return True