while True:
    destination = input()

    if destination == 'End':
        break

    minimal_budget = float(input())
    saved_money = 0

    while saved_money < minimal_budget:
        save = float(input())
        saved_money += save

    print(f'Going to {destination}!')