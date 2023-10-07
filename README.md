# N-puzzle-solver-with-heuristic-

8-Puzzle Solver using A* Algorithm
Introduction
The 8-Puzzle, also known as the sliding puzzle, is a popular puzzle game consisting of a grid of N tiles (where N can be 8, 15, 24, etc.) and one empty space. The goal is to rearrange the tiles to reach a specific target configuration from a given initial state. Tiles can be moved one at a time into the empty space, and the puzzle is solved when the tiles match the target configuration.

In this project, we implement the A* algorithm to solve the 8-Puzzle problem. The A* algorithm combines a heuristic value (h-score), which represents the estimated distance from the current state to the goal state, with a cost value (g-score), which represents the number of moves made to reach the current state. The total score (f-score) is calculated as:

f-score = h-score + g-score

For the 8-Puzzle problem, we use the Manhattan distance between misplaced tiles as the h-score and count the number of moves (g-score) from the initial state to the current state.

Implementation
Our implementation of the A* algorithm considers the following steps:

Initialize the puzzle with the given initial state and target state.
Maintain a priority queue (or a min-heap) to explore the puzzle states with the lowest f-score.
While there are unexplored states in the queue:
Pop the state with the lowest f-score.
Generate neighboring states by moving tiles.
Calculate the f-scores for the neighboring states.
Add the neighboring states to the queue.
Keep track of the parent state to reconstruct the solution path.
Usage
To use this 8-Puzzle solver, follow these steps:

Clone this repository to your local machine.
Modify the initial state and target state in the code as needed.
Run the code to solve the puzzle.
The program will display each step's move and the puzzle's current state until it reaches the target state.
The solution path will be printed upon successfully solving the puzzle.

Example:
# Set the initial and target states
initial_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Run the solver
solver = EightPuzzleSolver(initial_state, target_state)
solver.solve()

