
# Note: Reused some code from Informed Search assignment (did that asst before this one)

import time
import os
import psutil
from collections import deque
from puzzle import PuzzleState


def check_memory_limit(max_gb=4.0):
    """
    Function that constantly checks the memory usage for the overall program.
    A MemoryError will be raised if the memory limit (4.0 GB) is exceeded.
    This function was added due to the RAM constraints on my local machine.
    Note: This function was reused from the Informed Search asst.
    """
    process = psutil.Process(os.getpid())
    mem_usage_gb = process.memory_info().rss / (1024 ** 3)
    if mem_usage_gb > max_gb:
        raise MemoryError(
            f"Memory limit of {max_gb} GB has been exceeded. Script used {mem_usage_gb:.2f} GB of RAM "
            f"(Limit: {max_gb} GB). Stopping program to prevent system from crashing."
        )

def breadth_first_search(initial_state, max_frontier_size=2000000, max_rab_gb=4.0):
    """
    Breadth-first Search (BFS) algorithm implementation.
    Searches all nodes level by level (wide before deep)
    """
    start_time = time.time()
    frontier = deque([initial_state])
    visited_states = {initial_state.board}
    max_frontier_reached = 1
    explored_nodes_count = 0

    while frontier:
        if explored_nodes_count % 5000 == 0:
            check_memory_limit(max_gb=max_rab_gb)

        if len(frontier) > max_frontier_size:
            raise MemoryError(f"BFS frontier limit reached. Limit is {max_frontier_size} states.")

        max_frontier_reached = max(max_frontier_reached, len(frontier))
        current_state = frontier.popleft()

        if current_state.is_goal():
            end_time = time.time()
            path = []
            curr = current_state
            while curr.parent is not None:
                path.append(curr.move)
                curr = curr.parent
            path.reverse()

            return {
                "success": True,
                "path": path,
                "cost": current_state,
                "explored_nodes_count": explored_nodes_count,
                "max_frontier": max_frontier_reached,
                "time_elapsed": end_time - start_time
            }
        explored_nodes_count += 1

        for neighbor in current_state.get_neighbors():
            if neighbor.board not in visited_states:
                visited_states.add(neighbor.board)
                frontier.append(neighbor)

    return {
        "success": False,
        "explored_nodes_count": explored_nodes_count,
        "max_frontier": max_frontier_reached,
        "time_elapsed": time.time() - start_time
    }

def depth_first_search(initial_state, max_stack_size=1000000, max_ram_gb=4.0, max_depth=50):
    """
    Depth-first Search (DFS) algorithm implementation.
    Searches all nodes going deep down one path first (deep before wide/deep before level-by-level)
    Added a max depth limit to prevent excessive RAM usage so machine doesn't freeze/die
    """
    start_time = time.time()
    initial_path_states = {initial_state.board}
    stack = [(initial_state, initial_path_states)]
    max_stack_reached = 1
    explored_nodes_count = 0

    while stack:
        if explored_nodes_count % 5000 == 0:
            check_memory_limit(max_gb=max_ram_gb)

        if len(stack) > max_stack_size:
            raise MemoryError(f"DFS stack limit reached. Limit is {max_stack_size} states.")

        max_stack_reached = max(max_stack_reached, len(stack))

        current_state, path_states = stack.pop()

        if current_state.is_goal():
            end_time = time.time()
            path = []
            curr = current_state
            while curr.parent is not None:
                path.append(curr.move)
                curr = curr.parent
            path.reverse()

            return {
                "success": True,
                "path": path,
                "cost": current_state.cost,
                "explored_nodes_count": explored_nodes_count,
                "max_stack_frontier": max_stack_reached,
                "time_elapsed": end_time - start_time
            }

        if current_state.cost >= max_depth:
            continue
        explored_nodes_count += 1

        for neighbor in reversed(current_state.get_neighbors()):
            if neighbor.board not in path_states:
                new_path_states = path_states.copy()
                new_path_states.add(neighbor.board)
                stack.append((neighbor, new_path_states))

    return {
        "success": False,
        "explored_nodes_count": explored_nodes_count,
        "max_stack_frontier": max_stack_reached,
        "time_elapsed": time.time() - start_time
    }
