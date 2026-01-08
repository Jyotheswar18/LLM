balance = int(input())
withdraw = int(input())

if withdraw % 100 != 0:
    print("Amount must be multiple of 100")
elif withdraw > balance:
    print("Insufficient balance")
else:
    balance -= withdraw
    print("Updated Balance:", balance)
