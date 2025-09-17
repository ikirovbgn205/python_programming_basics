count_pages = int(input())
pages_per_hour = int(input())
days = int(input())

needed_hours = (count_pages // pages_per_hour) // days

print (needed_hours)