

deposit = int(input())
deposit_deadline = int(input())
annual_interest_rate = float(input()) / 100

all_earnings = deposit + deposit_deadline * ((deposit * annual_interest_rate) / 12)

print (all_earnings)