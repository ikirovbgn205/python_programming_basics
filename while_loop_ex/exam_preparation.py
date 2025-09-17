count_poor_grades = int(input())

number_problems = 0
total_score = 0
poor_grades = 0

last_problem = ''

is_enough = False



while count_poor_grades > poor_grades:
    problem_name = input()
    if problem_name == 'Enough':
        is_enough = True
        break

    score = int(input())
    if score <= 4:
        poor_grades += 1

    number_problems += 1
    total_score += score
    last_problem = problem_name

if is_enough:
    average_score = total_score / number_problems
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {number_problems}')
    print(f'Last problem: {last_problem}')
else:
    print(f'You need a break, {count_poor_grades} poor grades.')
