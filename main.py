import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET =1 

ROWS =3
COLS =3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_values = {
    "A":5,
    "B":9,
    "C":3,
    "D":2
}

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amoutn must be greater than 0")
        else:
            print("Enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet (1- " +str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if  1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Enter a number")
    return lines

def getbet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Enter a number")
    return amount

def slotmachinespin(rows, cols,symbols):
    all_symbols = []
    for symbol, symbolcount in symbol_count.items():
        for _ in range(symbolcount):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
            
def printslotmachine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row] , end =" | ")
            else:
                print(column[row], end="")
        print()

def checkwinnnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbols = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbols != symbol_to_check:
                break
        else:
            winnings+= values[symbols]*bet
            winning_lines.append(lines+1)
    return winnings, winning_lines    

def spin(balance):
    lines = get_number_of_lines()
    
    while True:
        bet = getbet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is {balance}")
        else:
            break
   
    # Spin the slot machine
    slot = slotmachinespin(ROWS, COLS, symbol_count)
    printslotmachine(slot)

    # Check winnings
    winnings, winning_lines = checkwinnnings(slot, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    if winning_lines:
        print("You won on lines:", *winning_lines)
    else:
        print("No winning lines this round.")

    return winnings - total_bet


def game():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = getbet()
        total_bet = bet* lines
        if total_bet > balance:
            print("You dont have enough balance to bet " + str(balance))
        else:
            break

    print(f"You are betting {bet} on {lines}. Total bet is equal to: ${bet*lines}")

    slot = slotmachinespin(ROWS,COLS,symbol_count)
    printslotmachine(slot)

    winnings, winning_lines = checkwinnnings(slot, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    print("You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print("current balance is", balance)
        answer = input("Press enter to play q to quit")
        if answer =='q':
            break
        balance += spin(balance)
    print("You're left with ", balance)

main()