MAY_OCTOBER_STUDIO = 50
MAY_OCTOBER_APARTMENT = 65
JUNE_SEPTEMBER_STUDIO = 75.20
JUNE_SEPTEMBER_APARTMENT = 68.70
JULY_AUGUST_STUDIO = 76
JULY_AUGUST_APARTMENT = 77

month = input()
qty_nights = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = qty_nights * MAY_OCTOBER_STUDIO
    apartment_price = qty_nights * MAY_OCTOBER_APARTMENT

    if qty_nights > 14 :
        studio_price -= studio_price * 0.30
    elif qty_nights > 7:
        studio_price -= studio_price * 0.05

elif month == 'June' or month == 'September':
    studio_price = qty_nights * JUNE_SEPTEMBER_STUDIO
    apartment_price = qty_nights * JUNE_SEPTEMBER_APARTMENT

    if qty_nights > 14:
        studio_price -= studio_price * 0.20

elif month == 'July' or month == 'August':
    studio_price = qty_nights * JULY_AUGUST_STUDIO
    apartment_price = qty_nights * JULY_AUGUST_APARTMENT

if qty_nights > 14:
    apartment_price -= apartment_price * 0.10

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')

