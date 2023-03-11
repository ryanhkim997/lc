class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # output: boolean if ransomeNote can be made using letters from magazine
        # input: two strings, ransomeNote and magazine
        # constraints: 
            # 1 <= ransomNote.length, magazine.length <= 105
            # ransomNote and magazine consist of lowercase English letters.
            # Each letter in magazine can only be used once in ransomNote.
        # edge cases:
            # strings are always at least length 1
            # ransomNote len is greater than magazine len

        # we want ransomNote len to be less than magazine, checking to see if all ransomNote chars can be made with magazine chars

        if len(ransomNote) > len(magazine): return False

        tracker = {}

        for i in ransomNote:
            tracker[i] = tracker.get(i, 0) + 1
        
        for i in magazine:
            if i in tracker:
                tracker[i] -= 1
                if tracker[i] == 0:
                    del tracker[i]
        
        if len(tracker) != 0:
            return False
        
        return True