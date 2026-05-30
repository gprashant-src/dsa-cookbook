class FenwickDiff:
    def __init__(self, arr):
        self.n = len(arr)
        self.bit = [0] * (self.n + 2)

        prev = 0
        for i in range(1, self.n + 1):
            curr = arr[i - 1]
            diff = curr  - prev
            self.bit[i] += diff
            idx = i + (i & -i)
            if idx <= self.n + 1:
                self.bit[idx] += self.bit[i]
            prev = curr


    def _update(self, index, val):
        index += 1
        while index <= self.n + 1:
            self.bit[index] += val
            index += (index & -index)

    def update(self, left, right, val):
        if left > right or left < 0 or right >= self.n: return 0

        self._update(left, val)
        self._update(right + 1, -val)

    def query(self, index):
        if index < 0 or index >= self.n: return 0

        index += 1
        S = 0
        while index > 0:
            S += self.bit[index]
            index -= (index & -index)
        return S
    
arr = [3, 2, -1, 6, 5, 4]
fw = FenwickDiff(arr)
print(fw.query(4))
fw.update(1, 4, 10)

print(fw.query(4))