text = input()
encrypted_version = ""
for character in text:
    ord_cipher = ord(character) + 3
    encrypted_version += chr(ord_cipher)
print(encrypted_version)
