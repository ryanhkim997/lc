class MinStack:

    def __init__(self):
        self.stack = []
        self.min_tracker = []
        self.min_val = float("inf")

    def push(self, val: int) -> None:
        if val <= self.min_val:
            self.min_val = val
        self.min_tracker.append(self.min_val)
        self.stack.append(val)

    def pop(self) -> None:
        self.min_tracker.pop()
        self.stack.pop()
        self.min_val = self.min_tracker[-1] if self.min_tracker else float("inf")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val

# first time through notes:
    # had the right idea, but didn't implement min_tracker to add current min value for every new pushed val