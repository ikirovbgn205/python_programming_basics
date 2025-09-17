shirt_price = float(input())
needed_money_for_ball = float(input())

price_shorts = shirt_price * 0.75
socks_price = price_shorts * 0.20
shoes_price = (price_shorts + shirt_price ) * 2

total_money = shirt_price + price_shorts + socks_price + shoes_price

discount = total_money - (total_money * 0.15)

if total_money >= needed_money_for_ball:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {discount:.2f} lv.')
else:
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {needed_money_for_ball - discount:.2f} lv. more.')