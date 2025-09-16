price_vegetable = float(input())
price_fruit = float(input())
kilos_vegetable = int(input())
kilos_fruit = int(input())

sum_veg_price = price_vegetable * kilos_vegetable
sum_fruit_price = price_fruit * kilos_fruit

final_price = (sum_veg_price + sum_fruit_price)
price_euro = final_price / 1.94

print(f"{price_euro:.2f}")
