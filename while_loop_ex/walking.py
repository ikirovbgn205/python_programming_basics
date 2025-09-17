GOAL_STEPS = 10_000

sum_steps = 0

while sum_steps < GOAL_STEPS:
    command = input()

    if command == 'Going home':
        steps_to_home = int(input())
        sum_steps += steps_to_home
        break

    sum_steps += int(command)

if sum_steps >= GOAL_STEPS:
    print('Goal reached! Good job!')
    print(f'{sum_steps - GOAL_STEPS} steps over the goal!')
else:
    print(f'{GOAL_STEPS - sum_steps} more steps to reach goal.')