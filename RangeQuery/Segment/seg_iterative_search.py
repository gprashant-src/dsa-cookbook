class SegTree:
    def __init__(self, arr, op, I):
        self.op = op
        self.I = I

        self.n = len(arr)

        self.size = 1
        while self.size < self.n:
            self.size <<= 1

        self.tree = [I] * (2 * self.size)

        for i, x in enumerate(arr):
            self.tree[self.size + i] = x

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = op(
                self.tree[2 * i],
                self.tree[2 * i + 1]
            )

    def update(self, pos, val):
        pos += self.size
        self.tree[pos] = val

        pos >>= 1

        while pos:
            self.tree[pos] = self.op(
                self.tree[2 * pos],
                self.tree[2 * pos + 1]
            )
            pos >>= 1

    def query(self, left, right):
        left += self.size
        right += self.size + 1

        ans_l = self.I
        ans_r = self.I

        while left < right:
            if left & 1:
                ans_l = self.op(ans_l, self.tree[left])
                left += 1

            if right & 1:
                right -= 1
                ans_r = self.op(self.tree[right], ans_r)

            left >>= 1
            right >>= 1

        return self.op(ans_l, ans_r)
    
    def find(self, x):
        if self.tree[1] < x:
            return -1

        idx = 1

        while idx < self.size:
            if self.tree[2*idx] >= x:
                idx = 2*idx
            else:
                idx = 2*idx + 1

        return idx - self.size