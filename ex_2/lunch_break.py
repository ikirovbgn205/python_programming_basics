from math import ceil

LUNCH_TIME = 1/8
REST_TIME = 1/4

serial_name = str(input())
chapter_time = int(input())
break_time = int(input())

lunch_time = break_time * LUNCH_TIME
rest_time = break_time * REST_TIME
left_time = break_time - lunch_time - rest_time

if left_time >= chapter_time:
    print(f"You have enough time to watch {serial_name} and left with {ceil(left_time - chapter_time)} minutes free time.")
elif chapter_time >= left_time:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(chapter_time - left_time)} more minutes.")
