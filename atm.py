balance = 1000
#adding colors for terminal output just for extra flair
#these are ANSI escape code --> 0: reset, 1: red, 3: green, 3: blue, 4: yellow 
#using array can be messy but we can use its index later to auto swap color depending on the option
#on second thought am use both var and array
reset = '\033[0m'; red = '\033[31m'; green = '\033[32m'; blue = '\033[34m'; yellow = '\033[33m'
colors = [reset, red, green, blue, yellow]
     
#display main menu
def main_menu():
    global balance, reset, red, blue, green, yellow, colors
    option = None
    while option != 4:
        print(f"\n1.{yellow} Check Balance\n{green}2. Deposit Money\n{blue}3. Withdraw Money\n{red}4. Quit\n{reset}")
        option = int(input(""))
        if option == 1:
            print(f"\n{yellow}your balance is: {reset}{balance}")
        if option == 2 or option == 3:
            exchange_menu(option)
    print("GoodBye")

#menu for withdraw/deposit to enter our amount
def exchange_menu(option): # 1 dynamic function for both deposit and withdraw
    global balance, reset, red, blue, green, yellow, colors
    print(f"\n{yellow}choose an option: {colors[option]}{option}")
    options = ["Check Balance", "Deposit", "Withdraw", "Quit"]
    amount = int(input(f"{yellow}Enter amount to {options[option-1]}: {colors[option]}")) # auto swap colors using option
    exchange(option, amount)

#withdraw/deposit into our balance
def exchange(option, amount):
    # turn out u can't access global var in python unless u used global keyword
    global balance, reset, red, blue, green, yellow, colors
    
    if option == 2:
        balance += amount
        print(f"{blue}Widthrawl successful. New Balance: {yellow}{balance}\n")
    if option == 3:
        if (balance - amount) < 0:
            print(f"{red}Insuffcient funds!\n")
        else:
            balance -= amount
            print(f"{green}Withdrawl successful. New balance: {yellow}{balance}\n")



main_menu()
