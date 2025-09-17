students = int(input())

group_one = 0
group_two = 0
group_three = 0
group_four = 0


total_grades = 0

for _ in range(students):
    score = float(input())

    if score >= 5:
        group_one += 1

    elif 4 <= score <= 4.99:
        group_two += 1

    elif 3 <= score <= 3.99:
        group_three += 1

    else:
        group_four += 1

    total_grades += score

top_students = group_one / students * 100
between_four_five = group_two / students * 100
between_three_four = group_three / students * 100
failed = group_four / students * 100

average_score = total_grades / students

print(f'Top students: {top_students:.2f}%')
print(f'Between 4.00 and 4.99: {between_four_five:.2f}%')
print(f'Between 3.00 and 3.99: {between_three_four:.2f}%')
print(f'Fail: {failed:.2f}%')
print(f'Average: {average_score:.2f}')