from sys import maxsize

n = int(input())

sum = 0
max_num = -maxsize

for _ in range(n):
    number = int(input())

    if number > max_num:
        max_num = number

    sum += number

half_sum = sum - max_num

if half_sum == max_num:
    print('Yes')
    print(f'Sum = {half_sum}')
else:
    diff = abs(max_num - half_sum)
    print('No')
    print(f'Diff = {diff}')
