positive = 0
negative = 0

while True:

    command = input()

    if command == 'stop':
        break

    number = int(command)

    if number < 0:
        print('Number is negative.')
        continue

    is_prime = False

    for num in range(2, number):
        if number % num == 0:
            is_prime = True

    if is_prime:
        negative += number
    else:
        positive += number


print(f'Sum of all prime numbers is: {positive}')
print(f'Sum of all non prime numbers is: {negative}')