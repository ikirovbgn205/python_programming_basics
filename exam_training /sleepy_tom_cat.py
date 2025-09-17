NEEDED_SLEEPING_TIME  = 30_000
PLAY_DAYS_OFF = 127
PLAY_WORKING_DAYS = 63

days_off = int(input())

working_days = 365 - days_off

play_time = days_off * PLAY_DAYS_OFF + working_days * PLAY_WORKING_DAYS

if play_time > NEEDED_SLEEPING_TIME:
    total_minutes = play_time - NEEDED_SLEEPING_TIME
    hours = total_minutes // 60
    minutes = total_minutes % 60
    print(f'Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    total_minutes = NEEDED_SLEEPING_TIME - play_time
    hours = total_minutes // 60
    minutes = total_minutes % 60
    print(f'Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
