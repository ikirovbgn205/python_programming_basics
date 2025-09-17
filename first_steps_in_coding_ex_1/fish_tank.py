length = int(input())
width = int(input())
height = int(input())
capacity_percent = float(input())

volume = length * width * height
volume_in_liters = volume / 1000
filled_space = capacity_percent / 100
liters_needed = volume_in_liters * (1 - filled_space)

print(liters_needed)