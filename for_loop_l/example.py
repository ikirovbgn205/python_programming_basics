text = ''

sum = 0

for _ in range(len(text)):
    if text[_] == 'a':
        sum += 1
    if text[_] =='e':
        sum += 2
    if text[_] =='i':
        sum += 3
    if text[_]=='o':
        sum += 4
    if text[_] =='u':
        sum += 5

print(sum)
