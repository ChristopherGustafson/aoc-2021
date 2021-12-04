
import time
import numpy as np
import copy

# Check if a board has Bingo
def check_board(marked):
  row_bingo = [True] * 5
  col_bingo = [True] * 5
  for row in range(5):
    for col in range(5):
      if not marked[row * 5 + col]:
        row_bingo[row] = False
      if not marked[row + col * 5]:
        col_bingo[row] = False
  return (True in row_bingo or True in col_bingo)

# Return sum of all unmarked numbers in the board
def sum_of_unchecked(board):
  numbers, marked = board
  sum = 0
  for i in range(len(numbers)):
    if not marked[i]:
      sum = sum + numbers[i]
  return sum

with open("day04/input.txt") as input:
  file_list = input.read().split("\n")
  file_array = np.array(file_list)[:-1]

  start_time = time.time()

  # Insert solution
  drawn_numbers = file_array[0].split(",")
  drawn_numbers = map(int, drawn_numbers)

  # Parse input boards
  boards = []
  board = []
  for line in file_array[2:]:
    if line == "":
      boards.append((board, np.zeros(25)))
      board = []
      continue
    for number in line.split(" "):
      if number != "":
        board.append(int(number))

  # Calculate score of first and last winning board  
  part1_score = 0
  part2_score= 0
  board_finished = np.zeros(len(boards))
  for number in drawn_numbers:
    for i, board in enumerate(boards):
      board_numbers, marked = board
      if number in board_numbers:
        marked[board_numbers.index(number)] = 1
      if not board_finished[i] and check_board(marked):
        board_finished[i] = 1
        if part1_score == 0: 
          part1_score = sum_of_unchecked(board) * number
        if 0 not in board_finished:
          part2_score = sum_of_unchecked(board) * number
          break
    if part2_score != 0: break

  print(f"Part 1 score: {part1_score}")
  print(f"Part 2 score: {part2_score}")
        

  end_time = time.time()

print(f"Total execution time: {round(end_time-start_time, 2)} seconds")