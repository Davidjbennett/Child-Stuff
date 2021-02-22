import copy

class Stack:
    def __init__(self):
        self.data = []
    def push(self, x):
        self.data.append(x)
    def pop(self):
        assert len(self.data) > 0
        return self.data.pop()
    def top(self):
        assert len(self.data) > 0
        return self.data[len(self.data) - 1]
    def size(self):
        return len(self.data)

s1 = Stack()
for i in range(5):
    s1.push(i)
print(f"{s1.size()=} {s1.top()=}")

s2 = copy.deepcopy(s1)

