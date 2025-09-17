MIN_POINTS = 1250.5

actor_name = input()
academy_points = float(input())
judge = int(input())

is_nomine = False

for _ in range(judge):
    judge_name = input()
    judge_points = float(input())

    academy_points += len(judge_name) * judge_points / 2

    if academy_points > MIN_POINTS:
        is_nomine = True
        break

if is_nomine:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {MIN_POINTS - academy_points:.1f} more!')
