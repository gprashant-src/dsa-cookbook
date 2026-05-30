class Segment:
    def __init__(self, arr, op, I):
        self.I = I
        self.op = op
        self.n = len(arr)
        self.tree = [I] * (2 * self.n)
        self.build(arr)

    def build(self, arr):
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 *i + 1])

    
    def update(self, index, value):
        t_idx = index + self.n
        self.tree[t_idx] = value

        while t_idx > 1:
            t_idx >>= 1
            l, r = 2 * t_idx, 2 * t_idx + 1
            self.tree[t_idx] = self.op(self.tree[l], self.tree[r])
    
    def query(self, left, right):
        a, b = left + self.n, right + 1 + self.n

        ans_l, ans_r = self.I, self.I

        while a < b:
            if a & 1:
                ans_l = self.op(ans_l, self.tree[a])
                a += 1
            if b & 1:
                b -= 1
                ans_r = self.op(ans_r, self.tree[b])
            
            a >>= 1
            b >>= 1
        
        return self.op(ans_l, ans_r)

    

arr = [5, 8, 2, 11, 6, 1, 9, 7]
sg = Segment(arr, op=min, I=float("inf"))

print(sg.query(1, 4))
sg.update(2, 4)
print(sg.query(1, 4))