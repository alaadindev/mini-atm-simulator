#display main menu
balance = 1000
def main_menu():
    global balance
    option = None
    while option != 4:
        print(f"\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Quit\n")
        option = int(input(""))
        if option == 1:
            print(f"your balance is: {balance}")
        if option == 2 or option == 3:
            exchange_menu(option)
    print("GoodBye")

def exchange_menu(option): # 1 dynamic function for both deposit and withdraw
    print(f"\nchoose an option: {option}")
    options = ["Check Balance", "Deposit", "Withdraw", "Quit"]
    amount = int(input(f"Enter amount to {options[option-1]}: ")) # -1 to turn it into index for our array
    exchange(option, amount)

def exchange(option, amount):
    global balance # turn out u can't access global var in python unless u used global keyword
    if option == 2:
        balance += amount
        print(f"Widthrawl successful. New Balance: {balance}")
    if option == 3:
        if (balance - amount) < 0:
            print(f"Insuffcient funds!")
        else:
            balance -= amount
            print(f"Withdrawl successful. New balance: {balance}\n")

main_menu()
