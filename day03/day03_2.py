
import time
import numpy as np

# Day 3 Part 2

def rating_recursion(
  diagnostic_report: list,
  search_most_common: bool, 
  current_index: int):
  # If only one line was left after filtering, return it as the answer
  if len(diagnostic_report) == 1:
    return int(diagnostic_report[0],2)

  # Find the indexes of the lines with leading ones or zeroes
  leading_one = []
  leading_zero = []
  for line in diagnostic_report:
    if line[current_index] == '1':
      leading_one.append(line)
    else:
      leading_zero.append(line)

  # Check if there where more leading ones or zeroes, and
  # recusivly check for the next index with the approriate
  # filtered lines
  if search_most_common:
    if len(leading_one) >= len(leading_zero):
      return rating_recursion(leading_one, search_most_common, current_index+1)
    else:
      return rating_recursion(leading_zero, search_most_common, current_index+1)
  else:
    if len(leading_zero) <= len(leading_one):
      return rating_recursion(leading_zero, search_most_common, current_index+1)
    else:
      return rating_recursion(leading_one, search_most_common, current_index+1)
def rating(diagnostic_report: list, search_most_common: bool):
  return rating_recursion(diagnostic_report, search_most_common, 0)


with open("day03/input.txt") as input:
  file_list = input.read().split("\n")
  file_array = np.array(file_list)[:-1]

  start_time = time.time()  

  oxygen_support_rating = rating(file_array, True)
  co2_scrubber_rating = rating(file_array, False)
  print(f"Oxygen Support Rating: {oxygen_support_rating}")
  print(f"CO2 Scrubber Rating: {co2_scrubber_rating}")
  print(f"Product: {oxygen_support_rating*co2_scrubber_rating}")

  end_time = time.time()

print(f"Total execution time: {round(end_time-start_time, 2)} seconds")


