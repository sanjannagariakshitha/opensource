V, C = input().split()
if V==C:
    print("NULL")
elif(V=="R" and C=="S") or (V=="P" and C=="R") or (V=="S" and C=="P"):
    print("Vignesh")
else:
    print("Charan")
