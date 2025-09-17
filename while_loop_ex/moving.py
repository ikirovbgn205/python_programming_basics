length = int(input())
width = int(input())
higth = int(input())

free_space = length * width * higth

cubic_meters = 0

while free_space >= cubic_meters:

    command = input()

    if command == 'Done':
        break

    cubic_meters += int(command)

if free_space >= cubic_meters:
    print(f'{abs(free_space - cubic_meters)} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(cubic_meters - free_space)} Cubic meters more.')



