X, Y, Z = map(int,(input().split()))
total_time = X*Y
available_time = Z*24*60
if total_time <= available_time:
    print("YES")
else:
    print("NO")
