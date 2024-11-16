bill_amount = int(input())
flat_discount=100
percentage_discount = bill_amount*0.1
max_discount=max(percentage_discount, flat_discount)
final_amount=bill_amount-max_discount
print(int(final_amount))
