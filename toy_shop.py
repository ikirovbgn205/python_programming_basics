PUZZLE = 2.60
DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2

DISCOUNT = 0.25
RENT = 0.10

vacation_price = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_teddy_bear = int(input())
count_minion = int(input())
count_truck = int(input())

total_toys_count = count_dolls + count_minion + count_puzzles + count_truck + count_teddy_bear
sum_toys_price = ((count_truck * TRUCK)
                  + (count_minion * MINION)
                  + (count_puzzles * PUZZLE)
                  + (count_dolls * DOLL)
                  + (count_teddy_bear * TEDDY_BEAR))

if total_toys_count >= 50:
    sum_toys_price -= (sum_toys_price * DISCOUNT)

sum_toys_price -= (sum_toys_price * RENT)

if sum_toys_price >= vacation_price:
    print(f"Yes! {sum_toys_price - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {abs(sum_toys_price - vacation_price):.2f} lv needed.")