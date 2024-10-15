class PuzzleStateDFS:
    def __init__(self, board, g=0, parent=None):
        self.board = board
        self.g = g  # Cost from start to current state
        self.parent = parent  # To trace the solution path
        self.zero_pos = self.find_zero()

    def find_zero(self):
        return np.argwhere(self.board == 0)[0]

    def get_neighbors(self):
        neighbors = []
        x, y = self.zero_pos
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for dx, dy in directions:
            if 0 <= x + dx < 3 and 0 <= y + dy < 3:
                new_board = self.board.copy()
                new_board[x, y], new_board[x + dx, y + dy] = new_board[x + dx, y + dy], new_board[x, y]
                neighbors.append(PuzzleStateDFS(new_board, self.g + 1, self))
        
        return neighbors

    def print_board(self):
        print("\n".join(" ".join(str(cell) for cell in row) for row in self.board))
        print()

def dfs(initial_board):
    stack = [PuzzleStateDFS(initial_board)]
    visited = set()

    while stack:
        current_state = stack.pop()
        
        # Print the current state of the board
        current_state.print_board()
        print(f"Depth: {current_state.g}\n")

        if np.array_equal(current_state.board, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])):
            return current_state.g  # Return the number of moves to reach the goal

        visited.add(tuple(current_state.board.flatten()))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board.flatten()) not in visited:
                stack.append(neighbor)

    return -1  # If no solution is found


# Example usage for DFS
initial_board_dfs = np.array([[1, 2, 3], [4, 0, 6], [7, 5, 8]])
moves_dfs = dfs(initial_board_dfs)
print(f"Number of moves to solve the puzzle (DFS): {moves_dfs}")
