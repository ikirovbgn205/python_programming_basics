width = int(input())
length = int(input())

qty_part = width * length

cake_left = 0

while qty_part >= cake_left:

    command = input()

    if command == "STOP":
        break

    cake_left += int(command)

if qty_part <= cake_left:
    print(f'No more cake left! You need {abs(qty_part - cake_left)} pieces more.')
else:
    print(f'{abs(cake_left - qty_part)} pieces are left.')