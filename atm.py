#display main menu
balance = 1000
def main_menu():
    option = None
    while option != 4:
        print(" 1. Check Balance\n", "2. Deposit Money\n", "3. Withdraw Money\n", "4. Quit")
        option = int(input(""))
        if option == 2 or option == 3:
            exchange_menu(option)
def exchange_menu(option): # 1 dynamic function for both deposit and withdraw
    print(" choose an option:", option)
    options = ["Check Balance", "Deposit", "Withdraw", "Quit"]
    amount = int(input(" Enter amount to ", options[option+1], ": ")) # -1 to turn it into index for our array
    exchange(option, amount)

def exchange(option, amount):
    if option == 2:
        balance += amount
    if option == 3 and (balance - amount) >= 0:
        balance -= amount
        print("Withdrawl successful. New balance:", balance)

main_menu()
