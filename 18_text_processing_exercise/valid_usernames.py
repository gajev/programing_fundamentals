usernames = input().split(", ")
for username in usernames:
    valid_username = True
    if not 3 <= len(username) <= 16:
        valid_username = False
        continue
    for valid_symbol in username:
        if not valid_symbol.isalnum():
            if valid_symbol != "-" and valid_symbol != "_":
                valid_username = False
                break
    if valid_username:
        print(username)
