username = input()
password = input()

data = input()

while data != password:
    data = input()
    if data == password:
        break
    data = input()

print(f'Welcome {username}!')
