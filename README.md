# Uninformed Search Assignment

Note: The user must have Python already installed on their local machine in order for this program script to run.

This assignment is a program that uses Breadth-first Search (BFS) and Depth-first Search (DFS) in order to solve the 24-puzzle problem. I first started using both algorithms to solve the 8-puzzle problem, then upscaled to the 24-puzzle problem.

Some code (such as in `puzzle.py`) is reused from my "Informed Search" assignment, as I completed that one before doing this assignment.

**WARNING:** Just like with the "Informed Search" assignment, there is a possibility that this program might crash the user's local machine. I created this program locally on my PC, which has a limited amount of RAM. Due to this, I hard-coded RAM guardrails into this program so that it maxes out how much RAM is allowed to be used during runs (3000000 states is the max amount that are allowed to be searched through). I was aware that this guard would not allow me to solve the given 24-puzzle problem in the assignment.

--------------------------------
## How to execute:
* Clone this repo from GitHub using `git clone https://github.com/emirick72/CS-580_Uniformed_Search_Assignment.git`
* `cd` into the repo on your machine (`cd CS-580_Uniformed_Search_Assignment`)
* Command to run the program: `python main.py`
* Command to generate the results into `results.txt`: `python generate_uninformed_results.py`