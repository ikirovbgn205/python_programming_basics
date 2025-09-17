budget_fishing = int(input())
season = input()
qty_fishing = int(input())

boat_loan = 0

if season == 'Spring':
    boat_loan = 3000
    if qty_fishing <= 6:
        boat_loan -= boat_loan * 0.10
    elif 7 <= qty_fishing <= 11:
        boat_loan -= boat_loan * 0.15
    elif qty_fishing >= 12:
        boat_loan -= boat_loan * 0.25

elif season == 'Summer' or season == 'Autumn':
    boat_loan = 4200
    if qty_fishing <= 6:
        boat_loan -= boat_loan * 0.10
    elif 7 <= qty_fishing <= 11:
        boat_loan -= boat_loan * 0.15
    elif qty_fishing >= 12:
        boat_loan -= boat_loan * 0.25

elif season == 'Winter':
    boat_loan = 2600
    if qty_fishing <= 6:
        boat_loan -= boat_loan * 0.10
    elif 7 <= qty_fishing <= 11:
        boat_loan -= boat_loan * 0.15
    elif qty_fishing >= 12:
        boat_loan -= boat_loan * 0.25

if season != 'Autumn' and qty_fishing % 2 == 0:
    boat_loan -= boat_loan * 0.05


if boat_loan <= budget_fishing:
    print(f'Yes! You have {budget_fishing - boat_loan:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(budget_fishing - boat_loan):.2f} leva.')