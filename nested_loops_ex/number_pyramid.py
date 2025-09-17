n = int(input())

current_number = 1
is_current_number =  False

for row in range(1, n + 1):
    for col in range(1, row + 1):

        if current_number > n:
            is_current_number = True
            break
        print(str(current_number) + ' ', end='')
        current_number += 1

        if is_current_number:
            break

    print()