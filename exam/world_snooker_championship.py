championship_stage = input()
type_ticket = input()
qty_tickets = int(input())
photo = input()

price = 0
photo_price = 0
discount = 0

if championship_stage == "Quarter final":
    if type_ticket == "Standard":
        price += 55.50 * qty_tickets
    elif type_ticket == "Premium":
        price += 105.20 * qty_tickets
    elif type_ticket == "VIP":
        price += 118.90 * qty_tickets

elif championship_stage == "Semi final":
    if type_ticket == "Standard":
        price += 75.88 * qty_tickets
    elif type_ticket == "Premium":
        price += 125.22 * qty_tickets
    elif type_ticket == "VIP":
        price += 300.40 * qty_tickets

elif championship_stage == "Final":
    if type_ticket == "Standard":
        price += 110.10 * qty_tickets
    elif type_ticket == "Premium":
        price += 160.66 * qty_tickets
    elif type_ticket == "VIP":
        price += 400 * qty_tickets


if price > 4000:
    discount = price * 0.25
elif price > 2500:
    discount = price * 0.10

if photo == "Y":
    photo_price += 40 * qty_tickets
    if price > 4000:
        photo_price = 0

total_price = price + photo_price - discount
print(f'{total_price:.2f}')