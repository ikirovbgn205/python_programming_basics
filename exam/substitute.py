K = int(input())
L = int(input())
M = int(input())
N = int(input())

combinations = 0

number_one = ''
number_two = ''

for first_number in range(K , 8 + 1):
    for second_number in range(9 , L - 1, -1 ):
        for third_number in range(M, 8 + 1):
            for fourth_number in range(9, N - 1, -1):


                number_one += f'{first_number}{second_number}'
                number_two += f'{third_number}{fourth_number}'

                result = f"{first_number}{second_number} - {third_number}{fourth_number}"
                if first_number % 2 == 0 and second_number % 2 != 0:
                    if third_number % 2 == 0 and fourth_number % 2 != 0:
                        print(result)
                        if f'{number_one} - {number_two}' == result:
                            print('Cannot change the same player.')



