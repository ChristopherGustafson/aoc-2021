
import time
import numpy as np

with open("day01/input.txt") as input:
  file = input.read().split("\n")
  depths = np.array(file)
  
  start_time = time.time()  

  increasing = 0
  for i in range(1,len(depths)-1):
    if int(depths[i]) > int(depths[i-1]):
      increasing = increasing+1
  print(increasing)

  increasing = 0
  for i in range(0, len(depths)-4):
    A = int(depths[i]) + int(depths[i+1]) + int(depths[i+2])
    B = int(depths[i+1]) + int(depths[i+2]) + int(depths[i+3])
    if B > A:
      increasing = increasing+1
  print(increasing)

  end_time = time.time()

print(f"Total execution time: {round(end_time-start_time, 2)} seconds")