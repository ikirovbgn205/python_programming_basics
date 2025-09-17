GREEN_PAINT = 3.4
RED_PAINT = 4.3
DOOR = 1.2 * 2
WINDOW = 1.5 * 1.5

x = float(input())
y = float(input())
h = float(input())

front_side = (x * x * 2) - DOOR
left_right_side = (x * y - WINDOW) * 2

roof_front_side = ((x * h) / 2) * 2
top_roof = (x * y) * 2

red_paint  = (roof_front_side + top_roof) / RED_PAINT
green_paint = (front_side + left_right_side) / GREEN_PAINT

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")