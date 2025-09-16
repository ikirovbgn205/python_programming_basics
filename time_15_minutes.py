ADDED_TIME = 15

hours = int(input())
minutes = int(input()) + ADDED_TIME

if minutes >= 60:
    minutes -= 60
    hours += 1

if hours >= 24:
    hours -= 24

if minutes < 10:
    print(f"{hours}:0{minutes}")
else :
    print(f"{hours}:{minutes}")