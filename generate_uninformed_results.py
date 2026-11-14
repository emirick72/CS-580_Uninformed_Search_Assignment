
from puzzle import PuzzleState
from uninformed_solver import breadth_first_search, depth_first_search

def format_board_string(board, size):
    """
    Return a formatting string that represents the board.
    """
    lines = []
    for i in range(0, len(board), size):
        row = board[i: i + size]
        lines.append(" " + " ".join(f"{val:2}" if val != 0 else " _" for val in row))
    return "\n".join(lines)


def run_benchmark(file_handle, title, board, size, max_ram_gb=4.0):
    """
    Run both BFS and DFS for the board and log the results in results.txt file.
    """
    file_handle.write("=" * 60 + "\n")
    file_handle.write(f"TEST CASE: {title}\n")
    file_handle.write("=" * 60 + "\n")
    file_handle.write("Initial Board:\n")
    file_handle.write(format_board_string(board, size) + "\n\n")

    initial_state = PuzzleState(board, size=size)

    # TEST OUT BFS HERE
    print(f"Running BFS on {title}...")
    file_handle.write("--- BREADTH-FIRST SEARCH ---\n")
    try:
        bfs_result = breadth_first_search(initial_state, max_ram_gb=max_ram_gb)
        if bfs_result["success"]:
            file_handle.write("Status: SUCCESS\n")
            file_handle.write(f"Time Elapsed:       {bfs_result['time_elapsed']:.6f} seconds")
            file_handle.write(f"Solution Length:    {bfs_result['cost']} moves\n")
            file_handle.write(f"States Explored:    {bfs_result['explored_nodes_count']}\n")
            file_handle.write(f"Peak Frontier:      {bfs_result['max_stack_frontier']}\n")
            file_handle.write(f"Solution Path:      {' -> '.join(bfs_result['path'])}\n\n")
        else:
            file_handle.write("Status:              FAILED (No solution found.)\n\n")
    except MemoryError as e:
        print(f"RAM safeguard triggered for {title}: {e}")
        file_handle.write(f"Status:         Stopped/RAM Safeguard Triggered\n")
        file_handle.write(f"Details:        {e}\n\n")


    # TEST OUT DFS HERE
    print(f"Running DFS on {title}...")
    file_handle.write("--- DEPTH-FIRST SEARCH ---\n")
    try:
        dfs_result = depth_first_search(initial_state, max_ram_gb=max_ram_gb, max_depth=35)
        if dfs_result["success"]:
            file_handle.write("Status: SUCCESS\n")
            file_handle.write(f"Time Elapsed:       {dfs_result['time_elapsed']:.6f} seconds")
            file_handle.write(f"Solution Length:    {dfs_result['cost']} moves\n")
            file_handle.write(f"States Explored:    {dfs_result['explored_nodes_count']}\n")
            file_handle.write(f"Peak Frontier:      {dfs_result['max_stack_frontier']}\n")
            file_handle.write(f"Solution Path:      {' -> '.join(dfs_result['path'])}\n\n")
        else:
            file_handle.write("Status:              FAILED (No solution found; depth limit exceeded.)\n\n")
    except MemoryError as e:
        print(f"RAM safeguard triggered for {title}: {e}")
        file_handle.write(f"Status:         Stopped/RAM Safeguard Triggered\n")
        file_handle.write(f"Details:        {e}\n\n")


def main():
    """
    Main driver function for generating the results.
    """
    # 8-puzzle test cases
    puzzle_8_easy = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    puzzle_8_medium = [1, 3, 0, 4, 2, 5, 7, 8, 6]

    # 24-puzzle test cases
    puzzle_24_medium = [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 0, 14, 15,
        16, 17, 13, 18, 20,
        21, 22, 23, 19, 24
    ]

    puzzle_24_assignment_hard = [
        9, 24, 3, 5, 17,
        6, 0, 13, 19, 10,
        11, 21, 22, 1, 20,
        16, 4, 14, 12, 15,
        8, 18, 23, 2, 7 
    ]

    with open("results.txt", "w", encoding="utf-8") as f:
        f.write("Uninformed Search (BFS and DFS) Benchmark and Sample Solutions\n\n")

        run_benchmark(f, "8-Puzzle (Easy, 2 moves max)", puzzle_8_easy, 3)
        run_benchmark(f, "8-Puzzle (Medium)", puzzle_8_medium, 3)

        run_benchmark(f, "24-Puzzle (Medium)", puzzle_24_medium, 5, max_ram_gb=4.0)
        run_benchmark(f, "24-Puzzle (Assignment, given)", puzzle_24_assignment_hard, 5, max_ram_gb=4.0)

    print("\nAll benchmarks complete. Results are written to `results.txt` file.")


if __name__ == "__main__":
    main()