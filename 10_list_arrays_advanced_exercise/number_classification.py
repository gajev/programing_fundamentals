numbers = input().split(",")
numbers = [int(i) for i in numbers]
positive = [positive_number for positive_number in numbers if positive_number >= 0]
positive = (', '.join(map(str, positive)))
negative = [negative_number for negative_number in numbers if negative_number < 0]
negative = (', '.join(map(str, negative)))
even = [even_number for even_number in numbers if even_number % 2 == 0]
even = (', '.join(map(str, even)))
odd = [odd_number for odd_number in numbers if odd_number % 2 != 0]
odd = (', '.join(map(str, odd)))
print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")