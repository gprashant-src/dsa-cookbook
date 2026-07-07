class Fenwick:
    def __init__(self, arr):
        self.n = len(arr)
        self.bit = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            self.bit[i] += arr[i - 1]
            idx = i + (i & -i)
            if idx <= self.n:
                self.bit[idx] += self.bit[i]

    def update(self, index, val):
        index += 1
        while index <= self.n:
            self.bit[index] += val
            index += (index & -index)

    def _query(self, index):
        index += 1
        S = 0
        while index > 0:
            S += self.bit[index]
            index -= (index & -index)
        return S
    
    def query(self, left, right):
        if left > right or left < 0 or right >= self.n: return 0
        if left == 0: return self._query(right)
        return self._query(right) - self._query(left - 1)
    
arr = [3, 2, -1, 6, 5, 4]
fw = Fenwick(arr)

print(fw.query(1, 4))



"""Binary Lifting
def find(k):
    idx = 0

    P = 1 << (ft.n.bit_length() - 1)
    while P:
        nxt = idx + P
        if nxt <= ft.n and ft.bit[nxt] < k:
            k -= ft.bit[nxt]
            idx = nxt
        P >>= 1
    
    return idx
"""