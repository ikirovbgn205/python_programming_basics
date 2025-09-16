from math import ceil
from math import floor

rocket = float(input())
count_rocket = int(input())
count_shoes = int(input())

total_rockets = rocket * count_rocket
shoes = round(rocket / 6, 2)
total_shoes = round(count_shoes * shoes, 2)
other_equipment = round((total_shoes + total_rockets) * 0.2, 2)

total = total_shoes + total_rockets + other_equipment

athlete_price = floor (total /8)
sponsor_price = ceil((total * 7) / 8)

print(f"Price to be paid by Djokovic {athlete_price}")
print(f"Price to be paid by sponsors {sponsor_price}")
