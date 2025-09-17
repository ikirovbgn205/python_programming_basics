from sys import maxsize

number = input()
max_number = -maxsize

while number != 'Stop':

    num = int(number)

    if max_number < num:
        max_number = num
    number = input()

print(max_number)
