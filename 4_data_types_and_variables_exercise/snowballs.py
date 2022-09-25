number_of_snowballs = int(input())
top_ball = 0
highest_weight = 0
highest_time = 0
highest_quality = 0

for snowball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > top_ball:
        top_ball = int(value)
        highest_weight = weight
        highest_time = time
        highest_quality = quality



print(f"{highest_weight} : {highest_time} = {top_ball} ({highest_quality})")