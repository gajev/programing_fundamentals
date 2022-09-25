



beach = input()
beach = beach.lower()
counter = 0
list_beach = ["sand", "water", "fish", "sun"]

import re

for item in re.finditer("sand", beach):
        counter += 1
for item in re.finditer("water", beach):
        counter += 1
for item in re.finditer("fish", beach):
        counter += 1
for item in re.finditer("sun", beach):
        counter += 1
print(counter)



