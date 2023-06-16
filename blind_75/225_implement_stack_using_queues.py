from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        len_q = len(self.q)
        for i in range(len_q):
            popped = self.q.popleft()
            if i != len_q - 1:
                self.push(popped)
            else:
                return popped

    def top(self) -> int:
        for i in range(len(self.q)):
            if i == len(self.q) - 1:
                return self.q[i]

    def empty(self) -> bool:
        if len(self.q):
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()