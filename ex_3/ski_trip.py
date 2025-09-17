ROOM_FOR_ONE_PERSON = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35

days_stay = int(input())
type_space = input()
rating =  input()

nights_stay = days_stay - 1
final_price = 0

if type_space == 'room for one person':
    final_price = nights_stay * ROOM_FOR_ONE_PERSON


elif type_space == 'apartment':
    final_price = nights_stay * APARTMENT
    if days_stay < 10 :
        final_price -= final_price * 0.30
    elif 10 <= days_stay <= 15 :
        final_price -= final_price * 0.35
    else:
        final_price -= final_price * 0.50


elif type_space == 'president apartment':
    final_price = nights_stay * PRESIDENT_APARTMENT
    if days_stay < 10 :
        final_price -= final_price * 0.10
    elif 10 <= days_stay <= 15 :
        final_price -= final_price * 0.15
    else:
        final_price -= final_price * 0.20

if rating == 'positive':
    final_price += final_price * 0.25
elif rating == 'negative':
    final_price -= final_price * 0.10

print(f"{final_price:.2f}")