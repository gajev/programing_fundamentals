food_per_month = float(input()) * 1000
hay_per_month = float(input()) * 1000
cover_per_month = float(input()) * 1000
pig_weight = float(input()) * 1000
everything_is_fine = True

for day in range (1, 31):
    food_per_month -= 300
    if day % 2 == 0:
        hay_per_month -= food_per_month * 0.05
    if day % 3 == 0:
        cover_per_month -= pig_weight / 3
    if food_per_month <= 0 or hay_per_month <= 0 or cover_per_month <= 0:
        everything_is_fine = False
        print("Merry must go to the pet store!")
        break
if everything_is_fine:
    print(f'Everything is fine! Puppy is happy! Food: {food_per_month / 1000:.2f}, Hay: {hay_per_month / 1000:.2f}, Cover: {cover_per_month / 1000:.2f}.')

