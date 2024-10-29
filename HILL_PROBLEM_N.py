def generate_all_configurations(initial_state):
  """Generates all possible configurations for placing queens on a chessboard, starting from an initial state.

  Args:
    initial_state: A list representing the initial placement of queens on the board.

  Returns:
    A list of all possible configurations, where each configuration is represented as a list of length n,
    where the i-th element indicates the column of the queen in the i-th row.
  """

  def generate_configurations_helper(row, board, solutions):
    if row == len(initial_state):
      solutions.append(list(board))
      return

    for col in range(len(initial_state)):
      if is_safe(row, col, board):
        board[row] = col
        generate_configurations_helper(row + 1, board, solutions)
        board[row] = None

  def is_safe(row, col, board):
    for i in range(row):
      if board[i] == col or abs(board[i] - col) == row - i:
        return False
    return True

  def calculate_heuristic(board):
    conflicts = 0
    for i in range(len(board)):
      for j in range(i + 1, len(board)):
        if board[i] == board[j] or abs(board[i] - board[j]) == i - j:
          conflicts += 1
    return conflicts

  solutions = []
  board = list(initial_state)
  generate_configurations_helper(0, board, solutions)

  # Find the configuration with a heuristic value of 0
  for configuration in solutions:
    heuristic = calculate_heuristic(configuration)
    if heuristic == 0:
      print("Solution found:")
      print(configuration)
      return

  print("No solution found.")

# Get the initial state from the user
initial_state = input("Enter the initial state (e.g., 0 2 1 3): ").split()
initial_state = [int(x) for x in initial_state]

# Generate all possible configurations and find the solution
generate_all_configurations(initial_state)