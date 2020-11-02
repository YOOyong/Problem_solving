data = input()

string = []
digits = 0

for letter in data:
    if letter.isdigit():
        digits += int(letter)
    else:
        string.append(letter)

string.sort()

print("".join(string) + str(digits))


#str.isdigit() .isalpha()