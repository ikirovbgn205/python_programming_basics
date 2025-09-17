record_in_seconds = float(input())
record_in_meters = float(input())
time_per_meter = float(input())

time_for_swimming = record_in_meters * time_per_meter
added_time = (record_in_meters // 15) * 12.5
real_record = time_for_swimming + added_time
time_needed = real_record - record_in_seconds

if record_in_seconds > real_record:
    print(f"Yes, he succeeded! The new world record is {real_record:.2f} seconds.")
else :
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")
