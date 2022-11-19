morse_code = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
              "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",".--.": "P",
              "--.-": "Q", ".-.": "R", "...": "S", "-": "T","..-": "U", "...-": "V", ".--": "W", "-..-": "X",
              "-.--": "Y", "--..": "Z"}
initial_code = input().split()
final_string = ""
for check in initial_code:
    if check in morse_code:
        final_string += morse_code[check]
    else:
        final_string += " "
print(final_string)