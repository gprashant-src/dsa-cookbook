class Segment:
    def __init__(self, arr, default=0):
        self.default = default
        self.n = len(arr)
        self.tree = [default] * (4 * self.n)
        self.lazy = [default] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, t_idx, low, high):
        if low == high:
            self.tree[t_idx] = arr[low]
            return
        
        mid = low + (high - low) // 2
        l, r = 2 * t_idx, 2 * t_idx + 1

        self.build(arr, l, low, mid)
        self.build(arr, r, mid + 1, high)

        self.tree[t_idx] = self.tree[l] + self.tree[r]

    def push(self, t_idx, low, high):
        if self.lazy[t_idx] == 0:return

        if low != high:
            val = self.lazy[t_idx]
            mid = low + (high - low) // 2

            l, r = 2 * t_idx, 2 * t_idx + 1

            self.tree[l] += val * (mid - low + 1)
            self.tree[r] += val * (high - mid)

            self.lazy[l] += val
            self.lazy[r] += val

        self.lazy[t_idx] = 0

    
    def _update(self, t_idx, low, high, left, right, val):
        if high < left or right < low: return

        if left <= low and high <= right:
            self.tree[t_idx] += val * (high - low + 1)
            self.lazy[t_idx] += val
            return
        
        self.push(t_idx, low, high)
        
        mid = low + (high - low) // 2
        l, r = 2 * t_idx, 2 * t_idx + 1

        self._update(l, low, mid, left, right, val)
        self._update(r, mid + 1, high, left, right, val)

        self.tree[t_idx] = self.tree[l] + self.tree[r]



    
    def _query(self, t_idx, low, high, left, right):
        if high < left or right < low: return self.default

        self.push(t_idx, low, high)

        if left <= low and high <= right: return self.tree[t_idx]

        mid = low + (high - low) // 2
        l, r = 2 * t_idx, 2 * t_idx + 1

        a = self._query(l, low, mid, left, right)
        b = self._query(r, mid + 1, high, left, right)

        return a + b
    

# -----------------------------------
    
    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)
    
    def update(self, index=None, left=None, right=None, val=None):
        if index is not None:
            self._update(1, 0, self.n - 1, index, index, val)
        else:
            self._update(1, 0, self.n - 1, left, right, val)
    

arr = [5, 8, 2, 11, 6, 1, 9, 7]
sg = Segment(arr)

print(sg.query(1, 4))
sg.update(index=2, val=2)
print(sg.query(1, 4))



# ------- ITERATIVE VERSION (POINT QUERY) -----------


class Segment:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build(arr)

    def build(self, arr):
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        
    
    def update(self, left, right, value):
        a, b = left + self.n, right + 1 + self.n

        while a < b:
            if a & 1:
                self.tree[a] += value
                a += 1
            if b & 1:
                b -= 1
                self.tree[b] += value
            
            a >>= 1
            b >>= 1
    
    def query(self, index):
        t_idx = index + self.n
        res = 0

        while t_idx > 0:
            res += self.tree[t_idx]
            t_idx >>= 1
        
        return res