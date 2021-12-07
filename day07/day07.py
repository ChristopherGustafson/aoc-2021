
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
  mean_pos = math.floor((st.mean(positions)))
  fuel_sum = 0
  for pos in positions:
    fuel_sum = fuel_sum + sum(range(abs(pos-(mean_pos))+1))
  print(f"Part 2: Fuel sum: {int(fuel_sum)}")

  end_time = time.time()

print(f"Total execution time: {round(end_time-start_time, 2)} seconds")