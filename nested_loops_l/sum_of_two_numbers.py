first_number = int(input())
second_number = int(input())
magic_number = int(input())

counter_combinations = 0
is_found = False

for n1 in range(first_number, second_number + 1):
    for n2 in range(first_number, second_number + 1):
        counter_combinations += 1

        if n1 + n2 == magic_number:
            is_found = True
            print(f'Combination N:{counter_combinations} ({n1} + {n2} = {magic_number})')
            break

    if is_found:
        break
else:
    print(f'{counter_combinations} combinations - neither equals {magic_number}')