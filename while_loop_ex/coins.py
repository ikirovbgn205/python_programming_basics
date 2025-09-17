change = int(float(input()) * 100)

coin_count = 0

while change:

    if change >= 200:
        change -= 200
        coin_count += 1

    elif 100 <= change <= 199:
        change -= 100
        coin_count += 1

    elif change >= 50:
        change -= 50
        coin_count += 1

    elif change >= 20:
        change -= 20
        coin_count += 1

    elif change >= 10:
        change -= 10
        coin_count += 1

    elif change >= 5:
        change -= 5
        coin_count += 1

    elif change >= 2:
        change -= 2
        coin_count += 1

    elif change >= 1:
        change -= 1
        coin_count += 1

print(coin_count)
