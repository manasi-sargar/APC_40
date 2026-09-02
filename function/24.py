balance = 0
history = []
def deposit(amount):
    global balance
    balance += amount
    history.append("Deposited " + str(amount))
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        history.append("Withdrawn " + str(amount))
    else:
        print("Insufficient balance")
def enquiry():
    print("Balance =", balance)
def transactions():
    for h in history:
        print(h)
deposit(5000)
withdraw(1000)
enquiry()
transactions()