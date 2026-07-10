class MinStack:

    def __init__(self):
        self.stack = []
        self.min = [2**31 - 1,]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(min(self.min[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
