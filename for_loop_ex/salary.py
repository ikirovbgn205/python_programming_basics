FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

number_tabs_opened = int(input())
salary = int(input())

is_lost = False

for _ in range(number_tabs_opened):
    name_tabs = input()

    if name_tabs == 'Facebook':
        salary -= FACEBOOK_FINE

    elif name_tabs == 'Instagram':
        salary -= INSTAGRAM_FINE

    elif name_tabs == 'Reddit':
        salary -= REDDIT_FINE

    if salary <= 0:
        is_lost = True
        break

if is_lost:
    print('You have lost your salary.')
else:
    print(salary)