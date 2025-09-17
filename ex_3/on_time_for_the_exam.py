exam_time_hours = int(input())
exam_time_minutes = int(input())
arrival_time_hours = int(input())
arrival_time_minutes = int(input())

exam_in_minutes = (exam_time_hours * 60) + exam_time_minutes
arrival_minutes =(arrival_time_hours * 60) + arrival_time_minutes

time_diff = exam_in_minutes - arrival_minutes

time = ''

if time_diff > 30 :
    time = 'Early'
elif time_diff < 0 :
    time = 'Late'
else:
    time = 'On time'

hours = abs(time_diff) // 60
minutes = abs(time_diff) % 60

result = ''
if hours > 0:
    result += f'{hours}:{minutes:02d} hours'
elif minutes > 0:
    result += f'{minutes} minutes'

if time_diff > 0:
    result += f' before the start'
elif time_diff < 0:
    result += f' after the start'

print(time)
print(result)
