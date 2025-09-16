volume = int(input())
first_tube_debit = int(input())
second_tube_debit = int(input())
hours = float(input())

first_tube_fill = (first_tube_debit * hours)
second_tube_fill = second_tube_debit * hours

sum_fill = first_tube_fill + second_tube_fill
first_tube_percent = (first_tube_fill / sum_fill) * 100
second_tube_percent = (second_tube_fill / sum_fill) * 100
percent_full = (sum_fill / volume) * 100

if sum_fill > volume:
    print(f'For {hours} hours the pool overflows with {sum_fill - volume} liters.')

else:
    print(f'The pool is {percent_full:.2f}% full. '
          f'Pipe 1: {first_tube_percent:.2f}%. Pipe 2: {second_tube_percent:.2f}%.')