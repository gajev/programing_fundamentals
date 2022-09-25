lost_battles = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
counter_broken_shieds = 0

for current_battle in range (1, lost_battles + 1):
    if current_battle % 2 == 0:
        expenses += helmet_price
    if current_battle % 3 == 0:
        expenses += sword_price
        if current_battle % 2 ==0:
            expenses += shield_price
            counter_broken_shieds += 1
            if counter_broken_shieds % 2 == 0:
                expenses += armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")



