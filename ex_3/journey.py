stay_budget = float(input())
season = input()

destination = ''
type_stay = ''

if stay_budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        type_stay = 'Camp'
        stay_budget = stay_budget * 0.30
    elif season == 'winter':
        type_stay = 'Hotel'
        stay_budget = stay_budget * 0.70

elif stay_budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        type_stay = 'Camp'
        stay_budget = stay_budget * 0.40
    elif season == 'winter':
        type_stay = 'Hotel'
        stay_budget = stay_budget * 0.80

elif stay_budget >= 1000:
    destination = 'Europe'
    if season == 'summer':
        type_stay = 'Hotel'
        stay_budget = stay_budget * 0.90
    elif season == 'winter':
        type_stay = 'Hotel'
        stay_budget = stay_budget * 0.90

print(f'Somewhere in {destination}')
print(f'{type_stay} - {stay_budget:.2f}')