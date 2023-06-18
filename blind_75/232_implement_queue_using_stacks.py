from collections import deque


# push: linear; pop, peek, and empty all constant
class MyQueue:

    def __init__(self):
        self.s_front = deque()
        self.s_back = deque()
        # can only support stack[-1], stack.append, stack.pop, stack.isempty (len(stack))

    def push(self, x: int) -> None:

        while self.s_front:
            self.s_back.append(self.s_front.pop())
        
        self.s_front.append(x)

        while self.s_back:
            self.s_front.append(self.s_back.pop())


    def pop(self) -> int:
        return self.s_front.pop()

    def peek(self) -> int:
        return self.s_front[-1]

    def empty(self) -> bool:
        return not self.s_front


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()