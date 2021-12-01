
import time
import numpy as np

with open("input.txt") as input:
  file_list = input.read().split("\n")
  file_array = np.array(file_list)

  start_time = time.time()  

  # Insert solution

  end_time = time.time()

print(f"Total execution time: {round(end_time-start_time, 2)} seconds")