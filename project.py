
balance=0
def check_balance():
    print("Total Balance:",balance)

def deposit(amt):
    global balance
    balance=balance+amt
    print(amt,"Rs.deposited!")

def withdraw(amt):
    global balance
    if(balance>amt):
        balance=balance-amt
        print(amt,"Rs.withdrawn!")
    else:
        print("Insufficient Balance")

while True:
    ch=int(input("\n\n1.Deposit\t2.Withdraw\n3.Check Balance\n4.Exit"))
    if ch==1:
        print('code for deposit')
        d_amt=int(input("Enter amt to deposit:"))
        deposit(d_amt)

    elif ch==2:
       print('code for withdraw')
       w_amt=int(input("Enter amt to withdraw:"))
       withdraw(w_amt)

    elif ch==3:
        print('code for check balance:')
        check_balance()

    elif ch==4:
        print("code for exit")
        break

    else:
        print("invalid choice")











        



















