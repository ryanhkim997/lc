class MyCircularQueue:

    def __init__(self, k: int):
        self.front = None
        self.back = None
        self.space = k

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.front = self.back = ListNode(value)
            self.space -= 1
            return True
        elif not self.isFull():
            self.back.next = ListNode(value)
            self.back = self.back.next
            self.space -= 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = self.front.next
            self.space += 1
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.back.val

    def isEmpty(self) -> bool:
        if not self.front:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.space == 0:
            return True
        return False
    
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()