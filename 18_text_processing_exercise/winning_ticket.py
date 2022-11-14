collection_of_tickets = [x.strip() for x in input().split(", ")]
for current_ticket in collection_of_tickets:
    winning_symbols = ['@', '#', '$', '^']
    left_part = current_ticket[:10]
    right_part = current_ticket[10:]
    winning_ticket = False
    if len(current_ticket) != 20:
        print("invalid ticket")
        continue
    for current_symbol in winning_symbols:
        for repeating_symbol in range(10, 5, -1):
            repeating_check = repeating_symbol * current_symbol
            if repeating_check in left_part and repeating_check in right_part:
                if repeating_symbol == 10:
                    winning_ticket = True
                    print(f'ticket "{current_ticket}" - {repeating_symbol}{current_symbol} Jackpot!')
                    break
                else:
                    winning_ticket = True
                    print(f'ticket "{current_ticket}" - {repeating_symbol}{current_symbol}')
                    break
    if not winning_ticket:
        print(f'ticket "{current_ticket}" - no match')





