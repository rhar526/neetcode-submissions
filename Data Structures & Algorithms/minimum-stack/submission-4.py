class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.mins) == 0 or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> None:

        if self.mins[-1] == self.stack[-1]:
            self.mins.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        
