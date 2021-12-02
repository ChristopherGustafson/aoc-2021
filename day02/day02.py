
import time
import numpy as np

with open("day02/input.txt") as input:
  file_list = input.read().split("\n")
  file_array = np.array(file_list)[:-1]

  start_time = time.time()  

  # Part 1
  horizontal = 0
  depth = 0
  for line in file_array:
    command = line.split(" ")
    if command[0] == "forward":
      horizontal = horizontal + int(command[1])
    elif command[0] == "down":
      depth = depth + int(command[1])
    elif command[0] == "up":
      depth = depth - int(command[1])
  print(horizontal * depth)

  # Part 2
  horizontal = 0
  depth = 0
  aim = 0
  for line in file_array:
    command = line.split(" ")
    if command[0] == "forward":
      horizontal = horizontal + int(command[1])
      depth = depth + aim * int(command[1])
    elif command[0] == "down":
      aim = aim + int(command[1])
    elif command[0] == "up":
      aim = aim - int(command[1])
  print(horizontal * depth)

  end_time = time.time()

print(f"Total execution time: {round(end_time-start_time, 2)} seconds")