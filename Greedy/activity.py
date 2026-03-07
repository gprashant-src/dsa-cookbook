intervals = [(1,3),(2,4),(3,5),(0,7),(5,9)]

intervals.sort(key=lambda x:(x[1]))

start, finish = intervals[0]
count = 1
for i in range(1, len(intervals)):
    st, fi = intervals[i]
    if st >= finish:
        # start = st
        finish = fi
        count += 1

print(count)