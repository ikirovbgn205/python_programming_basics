degrees = int(input())
time_of_the_day = input ()

shoes = ''
clothes = ''

if 10 <= degrees <= 18 :
    if time_of_the_day == 'Morning':
        shoes = 'Sneakers'
        clothes = 'Sweatshirt'
    elif time_of_the_day == 'Afternoon':
        shoes = 'Moccasins'
        clothes = 'Shirt'
    elif  time_of_the_day == 'Evening':
        shoes = 'Moccasins'
        clothes = 'Shirt'

elif 18 <= degrees <= 24 :
    if time_of_the_day == 'Morning':
        shoes = 'Moccasins'
        clothes = 'Shirt'
    elif time_of_the_day == 'Afternoon':
        shoes = 'Sandals'
        clothes = 'T-Shirt'
    elif time_of_the_day == 'Evening':
        shoes = 'Moccasins'
        clothes = 'Shirt'

elif degrees >= 25 :
    if time_of_the_day == 'Morning':
        shoes = 'Sandals'
        clothes = 'T-Shirt'
    elif time_of_the_day == 'Afternoon':
        shoes = 'Barefoot'
        clothes = 'Swim Suit'
    elif time_of_the_day == 'Evening':
        shoes = 'Moccasins'
        clothes = 'Shirt'

print(f"It's {degrees} degrees, get your {clothes} and {shoes}.")