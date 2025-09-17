PACKEGE_PEN = 5.80
PACKEGE_MARKERS = 7.20
LITER_CLEANER = 1.20

number_of_pack_pen = int(input()) * PACKEGE_PEN
number_of_pack_markers = int(input()) * PACKEGE_MARKERS
liters_cleaner = int(input()) * LITER_CLEANER
price_materials = number_of_pack_pen + number_of_pack_markers + liters_cleaner
discount = int(input()) / 100

total_price = price_materials - (price_materials * discount)

print(total_price)





