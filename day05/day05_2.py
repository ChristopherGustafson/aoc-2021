
import time
import numpy as np

# range() that can both handle increasing and decreasing ranges
def flexible_range_incl(start:int, stop:int):
  if start < stop:
    return range(start, stop+1)
  else:
    return range(start, stop-1, -1)

with open("day05/input.txt") as input:
  file_list = input.read().split("\n")
  file_array = np.array(file_list)[:-1]

  start_time = time.time()  

  # Map((x-cord, y-cord) -> number of crossing lines)
  cords = {}

  for line in file_array:
    xy_cords = line.split(" -> ")
    x1 = int(xy_cords[0].split(",")[0])
    y1 = int(xy_cords[0].split(",")[1])
    x2 = int(xy_cords[1].split(",")[0])
    y2 = int(xy_cords[1].split(",")[1])
 
    if x1 == x2:
      for y in flexible_range_incl(y1, y2):
        if count := cords.get((x1, y)):
          cords[(x1, y)] = count + 1
        else:
          cords[(x1, y)] = 1
    elif y1 == y2:
      for x in flexible_range_incl(x1, x2):
        if count := cords.get((x, y1)):
          cords[(x, y1)] = count + 1
        else:
          cords[(x, y1)] = 1
    else:
      for x, y in zip(flexible_range_incl(x1, x2), flexible_range_incl(y1, y2)):
        if count := cords.get((x, y)):
          cords[(x, y)] = count + 1
        else:
          cords[(x, y)] = 1

  points = 0
  for count in cords.values():
    if count > 1:
      points = points + 1

  print(f"Points: {points}")

  end_time = time.time()

print(f"Total execution time: {round(end_time-start_time, 2)} seconds")