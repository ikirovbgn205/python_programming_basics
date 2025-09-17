annual_fee = int(input())

shoes = annual_fee - (annual_fee * 0.40)
team = shoes - (shoes * 0.20)
ball = team * 0.25
accessoaries = ball * 0.20

total_annual_fee = (annual_fee + shoes + team
                    + ball + accessoaries)

print(f"{total_annual_fee:.2f}")
