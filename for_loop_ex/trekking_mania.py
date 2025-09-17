number_groups = int(input())

count_musala = 0
count_monblan = 0
count_kilimanjaro = 0
count_k2 = 0
count_everest = 0

for _ in range(number_groups):
    people_in_group = int(input())

    if people_in_group <= 5:
        count_musala += people_in_group

    elif 6 <= people_in_group <= 12:
        count_monblan += people_in_group

    elif 13 <= people_in_group <= 25:
        count_kilimanjaro += people_in_group

    elif 26 <= people_in_group <= 40:
        count_k2 += people_in_group

    else:
        count_everest += people_in_group

total_count = count_musala + count_monblan + count_kilimanjaro + count_k2 + count_everest

percent_musala = count_musala / total_count * 100
percent_monblan = count_monblan / total_count * 100
percent_kilimanjaro = count_kilimanjaro / total_count * 100
percent_k2 = count_k2 / total_count * 100
percent_everest = count_everest / total_count * 100

print(f'{percent_musala:.2f}%')
print(f'{percent_monblan:.2f}%')
print(f'{percent_kilimanjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')

