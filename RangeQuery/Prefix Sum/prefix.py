arr = [1, 4, 3, 2, 6, 10, 8]

class prefix1d:
    def __init__(self, arr):
        self.n = len(arr)
        self.P = [0] * (self.n + 1)

        for i in range(self.n):
            self.P[i + 1] = self.P[i] + arr[i]
    
    def query(self, left, right):
        return self.P[right + 1] - self.P[left]


l, r = 2, 5

P = prefix1d(arr)
# print(P)
print("Range sum=",P.query(l, r))