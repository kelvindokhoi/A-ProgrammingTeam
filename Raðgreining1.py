def is_low_pressure(weathermap, row, col):
  """Checks if a cell is a low pressure system.

  Args:
      weathermap: A list of lists representing the pressure map.
      row: The row index of the cell.
      col: The column index of the cell.

  Returns:
      True if the cell is a low pressure system, False otherwise.
  """  
  # Check if the cell is on the boundary (no four neighbors)
  if row <= 0 or col <= 0 or row >= len(weathermap) - 1 or col >= len(weathermap[0]) - 1:
    return False

  # Check if the pressure is lower than all four neighbors
  return (weathermap[row][col] < weathermap[row][col-1] and
          weathermap[row][col] < weathermap[row][col+1] and
          weathermap[row][col] < weathermap[row-1][col] and
          weathermap[row][col] < weathermap[row+1][col])

def main():
  """Reads the input, checks for low pressure systems, and prints the result."""
  rows, cols = map(int, input().split())
  weathermap = [[int(x) for x in input().split()] for _ in range(rows)]

  # Print the weathermap for verification (optional)
  # print("\nWeathermap:")
  # for row in weathermap:
  #   print(' '.join(map(str, row)))

  # Check for low pressure systems
  low_pressure_found = False
  for row in range(rows):
    for col in range(cols):
      if is_low_pressure(weathermap, row, col):
        low_pressure_found = True
        break  # Exit inner loop if found

  if low_pressure_found:
    print("Jebb")
  else:
    print("Neibb")

if __name__ == "__main__":
  main()