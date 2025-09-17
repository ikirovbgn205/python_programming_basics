money_needed = float(input())
saved_money = float(input())

days = 0
days_spend = 0
is_enough = False

while days_spend < 5:
    action = input()
    money = float(input())

    days += 1

    if action == 'spend':
        days_spend += 1
        saved_money = saved_money - money if saved_money > money else 0

    elif action == 'save':
        saved_money += money
        days_spend = 0

        if saved_money >= money_needed:
            is_enough = True
            break

if is_enough:
    print(f'You saved the money for {days} days.')
else:
    print(f"You can't save the money.")
    print(days)

