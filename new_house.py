ROSE = 5
DAHLIAS = 3.80
TULIPS = 2.80
NARCISSUS = 3
GLADIOLUS = 2.50

flowers = input()
qty_flowers = int(input())
budget = int(input())

final_price = 0

if flowers == 'Roses':
    final_price = qty_flowers * ROSE
    if qty_flowers > 80 :
        final_price -= (final_price * 0.10)

elif flowers == 'Dahlias':
    final_price = qty_flowers * DAHLIAS
    if qty_flowers > 90:
        final_price -= (final_price * 0.15)

elif flowers == 'Tulips':
    final_price = qty_flowers * TULIPS
    if qty_flowers > 80:
        final_price -= (final_price * 0.15)

elif flowers == 'Narcissus':
    final_price = qty_flowers * NARCISSUS
    if qty_flowers < 120:
        final_price += (final_price * 0.15)

elif flowers == 'Gladiolus':
    final_price = qty_flowers * GLADIOLUS
    if qty_flowers < 80:
        final_price += (final_price * 0.20)

if budget >= final_price:
    print(f'Hey, you have a great garden with {qty_flowers} {flowers} and {budget - final_price:.2f} leva left.')
elif budget <= final_price:
    print(f'Not enough money, you need {abs(budget - final_price):.2f} leva more.')