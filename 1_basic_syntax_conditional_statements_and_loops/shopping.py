budget = int(input())

spent_money = 0
command = input()

while command != "End":
    prices = int(command)
    spent_money += prices
    if spent_money > budget:
        print("You went in overdraft!")
        break
    command = input()

else:
    print("You bought everything needed.")
