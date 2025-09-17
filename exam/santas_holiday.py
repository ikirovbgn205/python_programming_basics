ROOM_FOR_ONE_PERSON = 18.00
APARTMENT = 25.00
PRESIDENT_APARTMENT = 35.00

days_stay = int(input())
type_room = (input())
grade = input()

nights = days_stay - 1

nights_price = 0

if type_room == 'room for one person':
    nights_price = nights * ROOM_FOR_ONE_PERSON

elif type_room == 'apartment':
    nights_price = nights * APARTMENT
    if days_stay < 10 :
        nights_price -= nights_price * 0.30
    elif 10 <= days_stay < 15 :
        nights_price -= nights_price * 0.35
    else:
        nights_price -= nights_price * 0.50

elif type_room == 'president apartment':
    nights_price = nights * PRESIDENT_APARTMENT
    if days_stay < 10 :
        nights_price -= nights_price * 0.10
    elif 10 <= days_stay < 15 :
        nights_price -= nights_price * 0.15
    else:
        nights_price -= nights_price * 0.20

if grade == 'positive':
    nights_price += nights_price * 0.25
else:
    nights_price -= nights_price * 0.10

print(f'{nights_price:.2f}')
