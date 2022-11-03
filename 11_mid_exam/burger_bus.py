count_of_cities = int(input())
total_profit = 0
for current_city in range(1, count_of_cities + 1):
    name = input()
    earned_money = float(input())
    expenses = float(input())
    if current_city % 3 == 0 and current_city % 5 != 0:
        expenses *= 1.5
    if current_city % 5 == 0:
        earned_money *= 0.9
    current_city_profit = earned_money - expenses
    total_profit += current_city_profit
    print(f'In {name} Burger Bus earned {current_city_profit:.2f} leva.')
print(f'Burger Bus total profit: {total_profit:.2f} leva.')


