from sys import maxsize
number = input()
biggest_num = -maxsize

while number != 'Stop':

    num = int(number)

    if biggest_num < num:
        biggest_num = num
    number = input()

print(biggest_num)