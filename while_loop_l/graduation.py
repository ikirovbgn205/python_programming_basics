student_name = input()

total_grade = 0
graduated_years = 0
failed_years = 0


while graduated_years < 12 :

    grades = float(input())

    if grades < 4:
        failed_years += 1

        if failed_years > 1:
            current_failed_year = graduated_years + 1
            print(f'{student_name} has been excluded at {current_failed_year} grade')
            break

        continue

    graduated_years += 1
    total_grade += grades

else:
    average = total_grade / graduated_years
    print(f"{student_name} graduated. Average grade: {average:.2f}")
