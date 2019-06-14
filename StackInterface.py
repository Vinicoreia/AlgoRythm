
class Stack:
    def __init__(self):
        self._stack = []
    def push(self, value):
        self._stack.append(value)
    def pop(self):
        return self._stack.pop()
    def popN(self, n):
        k = []
        print(self._stack)
        for i in range(n):
            k.append(self._stack.pop())
        return k
