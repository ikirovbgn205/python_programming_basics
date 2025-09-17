from math import floor


WINNER = 2000
FINALIST = 1200
SEMI_FINALIST = 720

count_tournaments = int(input())
starting_points = int(input())

tournament_points = 0
wins = 0

for _ in range(count_tournaments):
    stage_in_tournament = input()

    if stage_in_tournament == 'W':
        tournament_points += WINNER
        wins += 1

    elif stage_in_tournament == 'F':
        tournament_points += FINALIST

    elif stage_in_tournament == 'SF':
        tournament_points += SEMI_FINALIST

final_points = starting_points + tournament_points

average_points = tournament_points / count_tournaments
wins_rate = (wins / count_tournaments) * 100

print(f'Final points: {final_points}')
print(f'Average points: {floor(average_points)}')
print(f'{wins_rate:.2f}%')



