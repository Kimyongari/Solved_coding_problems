import math
N = input()
set = [0 for _ in range(11)]
for i in N:
    set[int(i)] += 1
set[10] = math.ceil(((set[6] + set[9]) / 2))
set[6] = 0
set[9] = 0
print(max(set))