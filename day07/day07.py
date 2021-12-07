
import time
import numpy as np
import statistics as st
import math

with open("day07/input.txt") as input:
  file_list = input.read().split("\n")
  file_array = np.array(file_list)[:-1]

  start_time = time.time()  

  positions = list(map(int, file_array[0].split(",")))
  
  # Part 1
  median_pos = st.median(positions)
  fuel_sum = 0
  for pos in positions:
    fuel_sum = fuel_sum + abs(pos-median_pos)
  print(f"Part 1: Fuel sum: {int(fuel_sum)}")

  # Part 2
  mean_pos = round((st.mean(positions)))
  min_fuel_sum = math.inf

  # Calculate for fuel sum for mean +/- 1 beacuse the minimal fuel sum
  # is found where mean - 1/2 <= position <= mean + 1/2. 
  # Thanks u/throwaway7824365346 for the proof https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/ 
  
  for delta in range(-1,2):
    current_fuel_sum = 0
    for pos in positions:
      current_fuel_sum = current_fuel_sum + sum(range(abs(pos-(mean_pos+delta))+1))
    if current_fuel_sum < min_fuel_sum: min_fuel_sum = current_fuel_sum  
  print(f"Part 2: Fuel sum: {int(min_fuel_sum)}")

  end_time = time.time()

print(f"Total execution time: {round(end_time-start_time, 2)} seconds")