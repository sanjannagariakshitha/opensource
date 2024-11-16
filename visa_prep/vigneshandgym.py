gym_cost, trainer_cost, monthly_bgt = map(int,input().split())
if gym_cost > monthly_bgt:
    print(0)
elif gym_cost + trainer_cost <= monthly_bgt:
    print(2)
else:
    print(1)
