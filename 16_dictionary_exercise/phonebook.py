contact = input()
phone_book = {}
while "-" in contact:
    contact = contact.split("-")
    phone_book[contact[0]] = contact[1]
    contact = input()
for check in range(int(contact)):
    current_contact = input()
    if current_contact in phone_book:
        print(f"{current_contact} -> {phone_book[current_contact]}")
    else:
        print(f"Contact {current_contact} does not exist.")

