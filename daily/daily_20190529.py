class stuck:
    def __init__(self, val:int=None):
        self.vals = []
        if val:
            self.vals.append(val)
    def push(self, val:int) -> int:
        if val:
            self.vals.append(val)
        return len(self.vals)
    def pop(self) -> int:
        if len(self.vals):
            val = self.vals.pop()
            return val
        return None
    def max(self) -> int:
        return max(self.vals)

s = stuck(5)
s.push(1)
s.push(2)
print(s.max())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())



