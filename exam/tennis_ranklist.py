from math import floor

W = 2000
F = 1200
SF = 720

count_tournaments = int(input())
starting_points = int(input())


count_points = 0
wins = 0

for _ in range(count_tournaments):
    tournament_stage = str(input())

    if tournament_stage == 'W':
        count_points += W
        wins += 1
    elif tournament_stage == 'F':
        count_points += F
    elif tournament_stage == 'SF':
        count_points += SF

total_points = starting_points + count_points
percentage_wins = wins / count_tournaments * 100

print(f'Final points: {total_points}')
print(f'Average points: {floor(count_points/ count_tournaments):.0f}')
print(f'{percentage_wins:.2f}%')

