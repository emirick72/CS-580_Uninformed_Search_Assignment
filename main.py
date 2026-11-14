
# Note: Reused some code from Informed Search assignment (did that asst before this one)

import sys
from puzzle import PuzzleState
from uninformed_solver import breadth_first_search, depth_first_search

def parse_input():
    """
    Accept arbitrary input from user.
    """
    print("--- Uninformed Search Puzzle Solver Program ---")
    print("Enter your unsolved puzzle as integers separated by spaces.")
    print("Use '0' to represent the blank space in the puzzle board.")
    print("Example for the 8-puzzle: 1 2 3 4 0 5 6 7 8")

    user_input = input("\nEnter intial state: ").strip()
    try:
        board = [int(x) for x in user_input.split()]
    except ValueError:
        print("Error: Please enter valid integers only.")
        sys.exit(1)

    total_tiles = len(board)
    if total_tiles == 9:
        size = 3
    elif total_tiles == 25:
        size = 5
    else:
        print(f"Error: Invalid number of tiles ({total_tiles}). You can only have 9 tiles (for the 8-puzzle) or 25 tiles (for the 24-puzzle).")
        sys.exit(1)

    return board, size

def main():
    board, size = parse_input()
    print("\nInitial Board Layout:")
    initial_state = PuzzleState(board, size=size)

    # Let user choose either BFS or DFS alg.
    print("\nChoose Algorithm:")
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    user_choice = input("Enter 1 or 2: ").strip()

    #algorithm_choice = "BFS" if user_choice == "1" else "DFS"
    #print(f"\nRunning {algorithm_choice} algorithm...")

    # BFS OR DFS ALGORITHM EXECUTION STUFF GOES HERE
    try:
        if user_choice == "1":
            print("BFS Running...")
            result = breadth_first_search(initial_state, max_rab_gb=3.0)
        else:
            print("DFS Running...")
            result = depth_first_search(initial_state, max_ram_gb=3.0, max_depth=30)

        if result["success"]:
            print(f"\nAlgorithm run was successful. Solution found in {result['time_elapsed']:.4f} seconds.")
            print(f"Solution Length: {result['cost']} moves")
            print(f"States Explored: {result['explored_nodes_count']}")
            print(f"Peak Frontier Size (BFS) or Peak Stack Size (DFS): {result['max_stack_frontier']}")
            print(f"Moves: {result['path']}")
        else:
            print("\nSearch completed, though no solution was found within set RAM limits.")
    except MemoryError as e:
        print(f"\n[RAM Limit Protection triggered]: {e}")

if __name__ == "__main__":
    main()