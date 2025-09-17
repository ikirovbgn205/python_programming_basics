NYLON_PRICE_PER_METER = 1.50
PAINT_PRICE_PER_LITER = 14.50
THINNER_PRICE_PER_LITER = 5.00
BAGS_PRICE = 0.40

qty_nylon = int(input())
qty_paint = int(input())
qty_thinner = int(input())
hours = int(input())

qty_nylon += 2
qty_paint += (qty_paint * 0.10)

materials_cost = (qty_nylon * NYLON_PRICE_PER_METER
                  + qty_paint * PAINT_PRICE_PER_LITER
                  + qty_thinner * THINNER_PRICE_PER_LITER
                  +BAGS_PRICE)
worker_salary = (materials_cost * 0.30) * hours
final_price = materials_cost + worker_salary

print(final_price)