import numpy as np
import heapq

class PuzzleState:
    def __init__(self, board, g=0):
        self.board = board
        self.g = g  # Cost from start to current state
        self.h = self.manhattan_distance()  # Heuristic cost to goal
        self.f = g + self.h  # Total cost
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
                neighbors.append(PuzzleState(new_board, self.g + 1))
        
        return neighbors

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i, j] != 0:
                    goal_x = (self.board[i, j] - 1) // 3
                    goal_y = (self.board[i, j] - 1) % 3
                    distance += abs(goal_x - i) + abs(goal_y - j)
        return distance

    def __lt__(self, other):
        return self.f < other.f

    def print_board(self):
        print("\n".join(" ".join(str(cell) for cell in row) for row in self.board))
        print()

def a_star_manhattan(initial_board):
    initial_state = PuzzleState(initial_board)
    
    open_set = []
    heapq.heappush(open_set, initial_state)
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        # Print the current state of the board and its f, g, h values
        current_state.print_board()
        print(f"g: {current_state.g}, h: {current_state.h}, f: {current_state.f}\n")

        if np.array_equal(current_state.board, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])):
            return current_state.g  # Return the number of moves to reach the goal

        closed_set.add(tuple(current_state.board.flatten()))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board.flatten()) in closed_set:
                continue

            neighbor.f = neighbor.g + neighbor.h

            if not any(np.array_equal(neighbor.board, state.board) and neighbor.g >= state.g for state in open_set):
                heapq.heappush(open_set, neighbor)

    return -1  # If no solution is found


# Example usage for Manhattan distance
initial_board = np.array([[1, 2, 3], [4, 0, 6], [7, 5, 8]])
moves = a_star_manhattan(initial_board)
print(f"Number of moves to solve the puzzle (Manhattan): {moves}")
