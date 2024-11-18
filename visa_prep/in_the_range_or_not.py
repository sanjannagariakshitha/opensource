T = int(input())
results = []
min_freq = 67
max_freq = 45000
for _ in range(T):
    X = int(input())
    if min_freq <= X <= max_freq:
        results.append("YES")
    else:
        results.append("NO")
for result in results:
    print(result)
