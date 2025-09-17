count = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(count):
    num = int(input())

    if num < 200:
        p1 += 1

    elif 200 <= num <= 399:
        p2 += 1

    elif 400 <= num <= 599:
        p3 += 1

    elif 600 <= num <= 799:
        p4 += 1

    else:
        p5 += 1

percent_p1 = p1 / count * 100
percent_p2 = p2 / count * 100
percent_p3 = p3 / count * 100
percent_p4 = p4 / count * 100
percent_p5 = p5 / count* 100

print(f'{percent_p1:.2f}%')
print(f'{percent_p2:.2f}%')
print(f'{percent_p3:.2f}%')
print(f'{percent_p4:.2f}%')
print(f'{percent_p5:.2f}%')