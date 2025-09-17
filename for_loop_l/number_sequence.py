import sys

n = int(input())

smallest_number = sys.maxsize
biggest_number = -sys.maxsize

for _ in range(n):
    current_number = int(input())
    if current_number < smallest_number:
        smallest_number = current_number
    if current_number > biggest_number:
        biggest_number = current_number

print(f'Max number: {biggest_number}')
print(f'Min number: {smallest_number}')