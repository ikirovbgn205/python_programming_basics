DECOR = 0.10
DISCOUNT = 0.10

budget_movie = float(input())
number_statist = int(input())
clothing_price_per_statist = float(input())

decor = budget_movie * DECOR
clothing_price = clothing_price_per_statist *  number_statist

if number_statist > 150:
    clothing_price -= clothing_price * DISCOUNT

total_movie_price = decor + clothing_price

if total_movie_price > budget_movie:
    print(f"Not enough money!")
    print(f"Wingard needs {total_movie_price - budget_movie:.2f} leva more.")
else :
    print(f"Action!")
    print(f"Wingard starts filming with {budget_movie - total_movie_price:.2f} leva left.")