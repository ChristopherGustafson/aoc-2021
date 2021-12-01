
import time

with open("input.txt") as input:
  file = input.read().split("\n\n")

  start_time = time.time()  

  # Insert solution

  end_time = time.time()

print(f"Total execution time: {round(end_time-start_time, 2)} seconds")