n=int(input())
arr=list(map(int, input().split()))
is_sorted=True
for i in range(1,n):
    if arr[i]<arr[i-1]:
        is_sorted=False
        break
print("true" if is_sorted else "false")
