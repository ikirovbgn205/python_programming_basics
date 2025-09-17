VIDEO_CARD_PRICE = 250
PROCESSOR_PRICE = 0.35
RAM_PRICE = 0.10

peter_budget = float(input())
qty_video_card = int(input())
qty_processors = int(input())
qty_ram = int(input())

price_video_card = qty_video_card * VIDEO_CARD_PRICE
price_processors = (price_video_card * PROCESSOR_PRICE) * qty_processors
price_ram = (price_video_card * RAM_PRICE) * qty_ram
sum_price = price_video_card + price_processors + price_ram

if qty_video_card > qty_processors:
    sum_price -= sum_price * 0.15

if peter_budget >= sum_price:
    print(f"You have {peter_budget - sum_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {sum_price - peter_budget:.2f} leva more!")