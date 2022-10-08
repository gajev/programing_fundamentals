times_of_racers = input().split()
number_of_laps = int((len(times_of_racers) - 1) / 2)
index = number_of_laps

left_racer_times = times_of_racers[0: index]
right_racer_times = times_of_racers[index + 1::]
right_racer_times.reverse()
final_time_left = 0
final_time_right = 0

for time in left_racer_times:
    if int(time) == 0:
        final_time_left *= 0.8
    else:
        final_time_left += int(time)

for time in right_racer_times:
    if int(time) == 0:
        final_time_right *= 0.8
    else:
        final_time_right += int(time)
if final_time_left > final_time_right:
    print(f"The winner is right with total time: {final_time_right:.1f}")
else:
    print(f"The winner is left with total time: {final_time_left:.1f}")

