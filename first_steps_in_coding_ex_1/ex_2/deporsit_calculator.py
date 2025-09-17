deposit = float(input())
term_of_deposit = int(input())
interest_rate = float(input()) / 100

annual_sum = deposit + term_of_deposit * ((deposit * interest_rate) / 12)

print(annual_sum)
