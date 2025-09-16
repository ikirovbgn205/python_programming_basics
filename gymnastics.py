country = input()
subject = input()

difficulty_score = 0
performance_score = 0

if country == 'Russia':
    if subject == 'ribbon':
        difficulty_score = 9.100
        performance_score = 9.400
    elif subject == 'hoop':
        difficulty_score = 9.300
        performance_score = 9.800
    elif subject == 'rope':
        difficulty_score = 9.600
        performance_score = 9.000

elif country == 'Bulgaria':
    if subject == 'ribbon':
        difficulty_score = 9.600
        performance_score = 9.400
    elif subject == 'hoop':
        difficulty_score = 9.550
        performance_score = 9.750
    elif subject == 'rope':
        difficulty_score = 9.500
        performance_score = 9.400

elif country == 'Italy':
    if subject == 'ribbon':
        difficulty_score = 9.200
        performance_score = 9.500
    elif subject == 'hoop':
        difficulty_score = 9.450
        performance_score = 9.350
    elif subject == 'rope':
        difficulty_score = 9.700
        performance_score = 9.150

final_score = difficulty_score + performance_score
diff = 20 % final_score
percent = (diff / 20) * 100

print(f'The team of {country} get {(final_score):.3f} on {subject}.')
print(f'{(percent):.2f}%')