percent = int(input())
if percent == 100:
    print("100% Complete!")
    print("[%%%%%%%%%%]")
else:
    times_percent_symbol = (percent // 10) * "%"
    times_dots = (10 - (percent // 10)) * "."
    print(f'{percent}% [{times_percent_symbol}{times_dots}]')
    print("Still loading...")

