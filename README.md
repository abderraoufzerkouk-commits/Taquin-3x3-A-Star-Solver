# 8-Puzzle Solver Using A\* Search Algorithm

A Python implementation of the **A\* search algorithm** to solve the 3×3 sliding puzzle (8-Puzzle), using the Manhattan distance heuristic.

## Overview

The 8-Puzzle consists of a 3×3 board containing eight numbered tiles and one empty space, represented by `0`.

The objective is to reach a predefined target configuration by sliding adjacent tiles into the empty space.

This project separates the puzzle model from the search algorithm into two Python modules.

## Features

- 3×3 puzzle representation using immutable tuples.
- Generation of valid neighboring states.
- Legal tile movement validation.
- Randomized puzzle generation through valid moves.
- Solvability verification relative to the target state.
- A\* search algorithm implementation.
- Manhattan distance heuristic.
- Priority queue using Python's `heapq`.
- Reconstruction of the complete solution path.
- Tracking of explored states.

## Algorithm

The solver uses the A\* search algorithm, which evaluates each state using:

**f(n) = g(n) + h(n)**

Where:

- `g(n)` is the actual cost from the initial state to the current state.
- `h(n)` is the estimated remaining cost, calculated using Manhattan distance.
- `f(n)` is the total estimated cost of the solution path through the current state.

### Manhattan Distance

The heuristic calculates the sum of the horizontal and vertical distances between each tile's current position and its target position.

The empty tile (`0`) is excluded.

### Search Optimization

The implementation uses:

- `heapq` to efficiently retrieve the state with the lowest priority.
- `itertools.count()` to provide a unique insertion order when priorities are equal.
- A dictionary to track the best known path cost for each state.
- A parent dictionary to reconstruct the solution path.

## Target Configuration

The target state used by the solver is:

```text
1  2  3
8  0  4
7  6  5
```

## Project Structure

```text
Taquin-3x3-A-Star-Solver/
│
├── Puzzle.py
├── Solver.py
├── README.md
└── .gitignore
```

### Modules

**Puzzle.py**

Defines the `Puzzle` class, responsible for:

- Board representation and validation.
- Generating neighboring states.
- Performing legal moves.
- Shuffling the puzzle.
- Checking solvability.

**Solver.py**

Defines the `Node` and `Solver` classes, responsible for:

- Manhattan distance calculation.
- A\* search execution.
- Priority queue management.
- Tracking explored states.
- Reconstructing the solution path.

## Usage

Make sure Python is installed, then place both Python files in the same directory.

Example:

```python
from Puzzle import Puzzle
from Solver import Solver

# Create an initial puzzle state
puzzle = Puzzle()
puzzle.shuffle(10)

# Display the initial state
puzzle.pprint()

# Solve the puzzle using A*
solver = Solver()
solution = solver.solve(puzzle.board)

if solution is not None:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)
    print("Explored states:", solver.etats_explores)

    for step, state in enumerate(solution):
        print(f"Step {step}:")
        for i in range(0, 9, 3):
            print(state[i:i + 3])
else:
    print("No solution exists.")
```

## Requirements

- Python 3
- No external libraries required.

The project uses Python standard library modules:

- `heapq`
- `itertools`
- `random`

## License

This project is available for educational and personal use.
