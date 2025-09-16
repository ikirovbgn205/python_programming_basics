control_minutes = int(input())
control_seconds = int(input())
length = float(input())
seconds_for_100_meters = int(input())

minutes_in_seconds = control_minutes * 60 + control_seconds
time_shorting = length / 120
full_time_shorting = time_shorting * 2.5

marins_time = (length / 100) * seconds_for_100_meters - full_time_shorting

if marins_time <= minutes_in_seconds:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {(marins_time):.3f}.')
else:
    print(f'No, Marin failed! He was {abs(marins_time - minutes_in_seconds):.3f} second slower.')
