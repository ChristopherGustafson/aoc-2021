
import time
import numpy as np

with open("day06/input.txt") as input:
  file_list = input.read().split("\n")

  start_time = time.time()  

  # Insert solution
  max_days_part_1 = 80
  max_days_part_2 = 256
  part_1_result = 0
  part_2_result = 0
  
  initial_fish = file_list[0].split(",")
  fish_timers = np.zeros(9)
  for fish in initial_fish:
    fish_timers[int(fish)] = fish_timers[(int(fish))] + 1

  for day in range(max_days_part_2):
    # Save if reached part 1 result
    if day == max_days_part_1:
      part_1_result = int(sum(fish_timers))

    new_fish_timers = np.zeros(9)
    for i in range(8, 0, -1):
      new_fish_timers[i-1] = fish_timers[i] 
    new_fish_timers[8] = fish_timers[0]
    new_fish_timers[6] = new_fish_timers[6] + fish_timers[0] 
    fish_timers = new_fish_timers

  part_2_result = int(sum(fish_timers))

  print(f"Part 1: {part_1_result}")
  print(f"Part 2: {part_2_result}")

  end_time = time.time()

print(f"Total execution time: {round(end_time-start_time, 2)} seconds")