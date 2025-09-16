training_tax = int(input())

basketball_shoes = training_tax - (training_tax * 0.40)
basketball_team = basketball_shoes - (basketball_shoes * 0.20)
ball = basketball_team * 0.25
accessories = ball * 0.20

total_price = basketball_shoes + basketball_team + ball + accessories + training_tax

print(total_price)