balance = 1000
#adding colors for terminal output just for extra flair
#these are ANSI escape code --> 0: reset, 1: red, 3: green, 3: blue, 4: yellow 
#using array can be messy but we can use its index later to auto swap color depending on the option
colors = ['\033[0m', '\033[31m', '\033[32m', '\033[34m', '\033[33m']
     
#display main menu
def main_menu():
    global balance
    global colors
    option = None
    while option != 4:
        print(f"\n1.{colors[4]} Check Balance\n{colors[2]}2. Deposit Money\n{colors[3]}3. Withdraw Money\n{colors[1]}4. Quit\n{colors[0]}")
        option = int(input(""))
        if option == 1:
            print(f"\n{colors[4]}your balance is: {colors[0]}{balance}")
        if option == 2 or option == 3:
            exchange_menu(option)
    print("GoodBye")

#menu for withdraw/deposit to enter our amount
def exchange_menu(option): # 1 dynamic function for both deposit and withdraw
    print(f"\n{colors[4]}choose an option: {colors[3]}{option}")
    options = ["Check Balance", "Deposit", "Withdraw", "Quit"]
    amount = int(input(f"{colors[4]}Enter amount to {options[option-1]}: {colors[option]}")) # auto swap colors using option
    exchange(option, amount)

#withdraw/deposit into our balance
def exchange(option, amount):
    global balance # turn out u can't access global var in python unless u used global keyword
    if option == 2:
        balance += amount
        print(f"{colors[3]}Widthrawl successful. New Balance: {colors[4]}{balance}\n")
    if option == 3:
        if (balance - amount) < 0:
            print(f"{colors[1]}Insuffcient funds!\n")
        else:
            balance -= amount
            print(f"{colors[3]}Withdrawl successful. New balance: {colors[4]}{balance}\n")



main_menu()
