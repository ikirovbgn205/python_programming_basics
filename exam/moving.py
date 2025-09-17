width = int(input())
length = int(input())
hight = int(input())

cubic_meters = width * length * hight
needed_cubic_meters = 0
is_full = False

while cubic_meters >= needed_cubic_meters:
    command = input()

    if command == 'Done':
        break
    needed_cubic_meters += int(command)

if cubic_meters >= needed_cubic_meters:
    print(f'{abs(cubic_meters - needed_cubic_meters)} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(needed_cubic_meters - cubic_meters)} Cubic meters more.')



