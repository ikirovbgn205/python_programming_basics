locations = int(input())
dig = 0
enough = False

for _ in range(locations):

    av_digging_per_day = int(input())
    count_days = int(input())

    for _ in range(count_days):
        gold = float(input())
        dig += gold
        average_gold_dig = dig / count_days

        if average_gold_dig > av_digging_per_day:
            enough = True
            dig = 0
            print(f'Good job! Average gold per day: {average_gold_dig:.2f}.')
            break

    if average_gold_dig < av_digging_per_day:
        print(f"You need {(av_digging_per_day - average_gold_dig):.2f} gold.")




