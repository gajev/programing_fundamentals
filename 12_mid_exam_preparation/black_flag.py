pirate_days = int(input())
plunder_a_day = int(input())
expected_plunder = float(input())
collected_plunder = 0

for current_day in range(1, pirate_days + 1):
    collected_plunder += plunder_a_day
    if current_day % 3 == 0:
        collected_plunder += plunder_a_day * 0.5
    if current_day % 5 == 0:
        collected_plunder = collected_plunder * 0.7
percentage = collected_plunder / expected_plunder * 100
if collected_plunder >= expected_plunder:
    print(f"Ahoy! {collected_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")