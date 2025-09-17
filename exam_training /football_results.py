first_result = str(input().replace('.', ':'))
second_result = str(input().replace('.', ':'))
third_result = str(input().replace('.', ':'))

first_score = first_result.split(':')
second_score = second_result.split(':')
third_score = third_result.split(':')

first_first_score = int(first_score[0])
first_second_score = int(first_score[1])
second_first_score = int(second_score[0])
second_second_score = int(second_score[1])
third_first_score = int(third_score[0])
third_second_score = int(third_score[1])

won = 0
loss = 0
draw = 0

for scores in [(first_first_score,first_second_score),
                   (second_first_score,second_second_score),
                   (third_first_score, third_second_score)]:
    if scores[0] > scores[1]:
        won += 1
    elif scores[0] < scores[1]:
        loss += 1
    elif scores[0] == scores[1]:
        draw += 1

print(f"Team won {won} games.")
print(f"Team lost {loss} games.")
print(f"Drawn games: {draw}")
