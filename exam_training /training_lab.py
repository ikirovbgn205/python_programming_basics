CORRIDOR = 100

h_in_meters = float(input())
w_in_meters = float(input())

h_in_centimeters = h_in_meters * 100
w_in_centimeters = w_in_meters * 100
available_width = w_in_centimeters - CORRIDOR

num_desk_per_row = available_width  // 70
num_rows = h_in_centimeters // 120
total_workspace = num_rows * num_desk_per_row - 3


print(f"{total_workspace}")
