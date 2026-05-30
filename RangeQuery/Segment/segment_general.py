class Segment:
    def __init__(self, arr, op, I):
        self.I = I
        self.op = op
        self.n = len(arr)
        self.tree = [I] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, t_idx, low, high):
        if low == high:
            self.tree[t_idx] = arr[low]
            return
        
        mid = low + (high - low) // 2
        l, r = 2 * t_idx, 2 * t_idx + 1

        self.build(arr, l, low, mid)
        self.build(arr, r, mid + 1, high)

        self.tree[t_idx] = self.op(self.tree[l], self.tree[r])
    
    def _update(self, t_idx, low, high, arr_idx, val):
        if low == high:
            self.tree[t_idx] = val
            return
        
        mid = low + (high - low) // 2
        l, r = 2 * t_idx, 2 * t_idx + 1

        if arr_idx <= mid:
            self._update(l, low, mid, arr_idx, val)
        else:
            self._update(r, mid + 1, high, arr_idx, val)

        self.tree[t_idx] = self.op(self.tree[l], self.tree[r])
    
    def _query(self, t_idx, low, high, left, right):
        if left <= low and high <= right: return self.tree[t_idx]

        if high < left or right < low: return self.I

        mid = low + (high - low) // 2
        l, r = 2 * t_idx, 2 * t_idx + 1

        a = self._query(l, low, mid, left, right)
        b = self._query(r, mid + 1, high, left, right)

        return self.op(a, b)
    
    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)
    
    def update(self, index, value):
        self._update(1, 0, self.n - 1, index, value)
    

arr = [5, 8, 2, 11, 6, 1, 9, 7]
sg = Segment(arr, op=min, I=float("inf"))

print(sg.query(1, 4))
sg.update(2, 4)
print(sg.query(1, 4))