class MinStack:
    def __init__(self):
        self.stack = []
    # @param x, an integer

    def push(self, x):
        if len(self.stack):
            self.stack.append((x, min(x, self.getMin())))
        else:
            self.stack.append((x, x))

    # @return nothing
    def pop(self):
        if len(self.stack):
            self.stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1][0] if len(self.stack) else -1

    # @return an integer
    def getMin(self):
        return self.stack[-1][1] if len(self.stack) else -1


s = MinStack()

print(s.top())
