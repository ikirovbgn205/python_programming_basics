BROTHER_MONEY = 1

age = int(input())
money_washing_machine = float(input())
toy_price = int(input())

increase_money_for_birth = 10
total_money = 0
toy_count = 0

for age in range(1,age + 1):

    if age % 2 == 0:
        total_money += (increase_money_for_birth - BROTHER_MONEY)
        increase_money_for_birth += 10
    else:
        toy_count += 1

total_money += toy_count * toy_price

if total_money >= money_washing_machine:
    print(f'Yes! {total_money - money_washing_machine:.2f}')
else:
    print(f'No! {money_washing_machine - total_money:.2f}')
