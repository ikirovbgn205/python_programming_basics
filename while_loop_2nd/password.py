username = input()
password = input()

code = input()

while code != password:
    code = input()

print(f'Welcome {username}!')