target = int(input())

complete_target = False
money_saved = 0

while True :

    command = input()
    command_two = input()

    if command != 'closed':
        break

    elif command == 'haircut':
        if command_two == 'mens':
            money_saved += 15

        elif command_two == 'ladies':
            money_saved += 20

        elif command_two == 'kids':
            money_saved += 10

    elif command == 'color':
        if command_two == 'touch up':
            money_saved += 20

        elif command_two == 'full color':
            money_saved += 30

    elif money_saved >= target:
        complete_target = True
        break

if complete_target :
    print(f'You have reached your target for the day!')
    print(f'Earned money: {money_saved}lv.')
else:
    print(f'Target not reached! You need {target - money_saved}lv. more.')
    print(f'Earned money: {money_saved}lv.')

