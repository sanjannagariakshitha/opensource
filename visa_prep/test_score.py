N, X, Y = map(int, input().split())
if Y%X == 0 and Y//X <= N:
    print("YES")
else:
    print("NO")
