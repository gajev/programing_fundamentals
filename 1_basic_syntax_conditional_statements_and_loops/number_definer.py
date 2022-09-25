number = float(input())

if number >= 0:
    if number == 0:
        print("zero")
    elif 0 < number < 1:
        print("small positive")
    elif 1000000 > number >= 1:
        print("positive")
    else:
        print("large positive")

else:
    if 0 > number > -1:
        print("small negative")
    elif -1000000 < number <= -1:
        print("negative")
    else:
        print("large negative")