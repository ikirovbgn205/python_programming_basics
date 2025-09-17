name = input()

total_score = 0
years_counter = 0
failed_years = 0

while years_counter < 12:

    grade = float(input())

    if grade < 4:
        failed_years += 1

        if failed_years > 1:
            current_failed_year = years_counter + 1
            print(f'{name} has been excluded at {current_failed_year} grade')
            break

        continue


    total_score += grade
    years_counter += 1

else:
    average_score = total_score / years_counter
    print(f'{name} graduated. Average grade: {average_score:.2f}')

