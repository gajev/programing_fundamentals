centuries = int(input())
year = centuries * 100
days = int(year * 365.2422)
hours = int(days) * 24
minutes = int(hours) * 60

print(f'{centuries} centuries = {year} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes')