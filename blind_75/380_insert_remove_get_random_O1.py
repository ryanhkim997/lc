from random import random

class RandomizedSet:

    def __init__(self):
        self.idx_dict = {}
        self.val_arr = []

    def insert(self, val: int) -> bool:
        if val in self.idx_dict:
            return False
        self.val_arr.append(val)
        self.idx_dict[val] = len(self.val_arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_dict:
            return False
        last_val = self.val_arr[-1]
        val_idx = self.idx_dict[val]

        self.val_arr[val_idx] = last_val
        self.idx_dict[last_val] = val_idx
        del self.idx_dict[val]
        self.val_arr.pop()
        return True
            

    def getRandom(self) -> int:
        return random.choice(self.val_arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# constraints:
    # -231 <= val <= 231 - 1
    # At most 2 * 105 calls will be made to insert, remove, and getRandom.
    # There will be at least one element in the data structure when getRandom is called.
    # all vals are ints