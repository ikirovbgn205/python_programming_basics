target_for_day = int(input())

money_saved = 0

while True :
    command_one = input()
    command_two = input()

    if command_one == 'closed':
        break

    elif command_one == 'haircut':
        if command_two == 'mens':
            money_saved += 15
        elif command_two == 'ladies':
            money_saved += 20
        elif command_two == 'kids':
            money_saved += 10

    elif command_one == 'color':
        if command_two == 'touch up':
            money_saved += 20
        elif command_two == 'full color':
            money_saved += 30



if money_saved > target_for_day :
    print(f'You have reached your target for the day!')
    print(f'Earned money: {money_saved}lv.')
else:
    print(f'Target not reached! You need {target_for_day - money_saved}lv. more.')
    print(f'Earned money: {money_saved}lv.')

