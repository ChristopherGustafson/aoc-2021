
import time
import numpy as np

# Day 3 Part 1

with open("day03/input.txt") as input:
  file_list = input.read().split("\n")
  file_array = np.array(file_list)[:-1]

  start_time = time.time()  

  # Count number of ones for each bit
  one_bit_count = [0] * len(list(file_array[0]))
  for line in file_array:
    bits = list(line)
    for i in range(len(bits)):
      if bits[i] == '1':
        one_bit_count[i] = one_bit_count[i] + 1
  
  # Compute gamma/epsilon
  gamma = 0
  epsilon = 0
  for i in range(len(one_bit_count)): 
    if one_bit_count[i] > (len(file_array)/2):
      gamma = gamma + 2 ** (len(one_bit_count)-i-1)
    else:
      epsilon = epsilon + 2 ** (len(one_bit_count)-i-1)

  print(f"Gamma: {gamma}")
  print(f"Epsilon: {epsilon}")
  print(f"Product: {gamma*epsilon}")

  end_time = time.time()

print(f"Total execution time: {round(end_time-start_time, 2)} seconds")


