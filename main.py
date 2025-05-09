from termcolor import colored
from pyfiglet import Figlet
import numpy as np
from copy import deepcopy #https://stackoverflow.com/questions/15214404/how-can-i-copy-an-immutable-object-like-tuple-in-python
from queue import PriorityQueue #https://builtin.com/data-science/priority-queues-in-python
import heapq #https://builtin.com/data-science/priority-queues-in-python

class Problem:
    def __init__(self, initial_state):
        self.INITIAL_STATE = initial_state
        self.GOAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

def get_index_zero(state):
    state = state
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return (row, col)

def swap(state, index1, index2):
    new_state = []
    for row in state:
        new_state.append(list(row))
    temp = new_state[index1[0]][index1[1]]
    new_state[index1[0]][index1[1]] = new_state[index2[0]][index2[1]]
    new_state[index2[0]][index2[1]] = temp

    tuple_state = (tuple(new_state[0]), tuple(new_state[1]), tuple(new_state[2]))

    return tuple_state

def get_children(state):
    zero_index = get_index_zero(state)
    possible_moves = [(-1, 0), (1,0), (0, -1), (0, 1)]
    valid_states = []
    for move in possible_moves:
        new_row = zero_index[0] + move[0]
        new_col = zero_index[1] + move[1]

        if new_row >= 0 and new_row <=2 and new_col >=0 and new_col <=2:
            valid_states.append(swap(state, zero_index, (new_row, new_col)))
    
    return(valid_states)

def uniform_cost_search(problem):
    goal_state = problem.GOAL_STATE
    start_state = problem.INITIAL_STATE

    queue = PriorityQueue()
    queue.put((0, start_state, [], 0))
    max_queue_size = 1

    expanded = set()

    while not queue.empty():
        
        cost, curr_state, path, depth = queue.get()

        if curr_state == goal_state:
            return cost, curr_state, path, depth, len(expanded), max_queue_size

        if curr_state in expanded:
            continue

        expanded.add(curr_state)

        for new_state in get_children(curr_state):
            if new_state not in expanded:
                new_path = path[:]
                new_path.append(curr_state)
                new_depth = depth + 1
                heuristic = 0
                new_cost = cost + 1
                queue.put((cost + heuristic, new_state, new_path, new_depth))
                max_queue_size = max(max_queue_size, queue.qsize())
                
    
    return None, None, None, None, None, None
    
def misplaced_tile(state, goal_state):
    num_misplaced_tiles = 0
    for i in range(3):
        for j in range(3):
            if goal_state[i][j] != 0:
                if state[i][j] != goal_state[i][j]:
                    num_misplaced_tiles += 1
    return num_misplaced_tiles

def astar_misplaced_tile(problem):
    goal_state = problem.GOAL_STATE
    start_state = problem.INITIAL_STATE

    queue = PriorityQueue()
    queue.put((0, start_state, [], 0))
    max_queue_size = 1

    expanded = set()

    while not queue.empty():
        
        cost, curr_state, path, depth = queue.get()

        if curr_state == goal_state:
            return cost, curr_state, path, depth, len(expanded), max_queue_size

        if curr_state in expanded:
            continue

        expanded.add(curr_state)

        for new_state in get_children(curr_state):
            if new_state not in expanded:
                new_path = path[:]
                new_path.append(curr_state)
                new_depth = depth + 1
                heuristic = misplaced_tile(new_state, goal_state)
                new_cost = cost + 1
                queue.put((cost + heuristic, new_state, new_path, new_depth))
                max_queue_size = max(max_queue_size, queue.qsize())

    return None, None, None, None, None, None

def manhattan_distance(state, goal_state):
    total_distance = 0
    for num in range(1,9):
        state_index = (-1, -1)
        goal_index = (-1, -1)
        for i in range(3):
            for j in range(3):
                if state[i][j] == num:
                    state_index = (i, j)
                if goal_state[i][j] == num:
                    goal_index = (i, j)
        total_distance += abs(state_index[0] - goal_index[0]) + abs(state_index[1] - goal_index[1])
    return total_distance

def astar_manhattan(problem):
    goal_state = problem.GOAL_STATE
    start_state = problem.INITIAL_STATE

    queue = PriorityQueue()
    queue.put((0, start_state, [], 0))
    max_queue_size = 1

    expanded = set()

    while not queue.empty():
        
        cost, curr_state, path, depth = queue.get()

        if curr_state == goal_state:
            return cost, curr_state, path, depth, len(expanded), max_queue_size

        if curr_state in expanded:
            continue

        expanded.add(curr_state)

        for new_state in get_children(curr_state):
            if new_state not in expanded:
                new_path = path[:]
                new_path.append(curr_state)
                new_depth = depth + 1
                heuristic = manhattan_distance(new_state, goal_state)
                new_cost = cost + 1
                queue.put((cost + heuristic, new_state, new_path, new_depth))
                max_queue_size = max(max_queue_size, queue.qsize())

    return None, None, None, None, None, None


def main():
    f = Figlet(font="slant")
    print(colored(f.renderText("8 Puzzle Solver"), "green"))
    print("Welcome to my 8 puzzle project for CS205: AI!")
    print("To get started, input each row of the puzzle. Each tile number should be separated by space. Please enter valid 8 puzzles only.")
    puzzle_rows = []
    #prompting user to input puzzle
    numbers = []
    row_inputs = []
    for i in range(1, 4):
        while True:
            try:
                row = list(map(int, input(f"Input row {i}: ").strip().split()))
                #check that each no numbers are repeated
                if (len(set(row)) != len(row)) | any(num in numbers for num in row):
                    print(f"Duplicate numbers are not allowed. Please re-enter row {i}:")
                    continue
                #check that each number is 0-8
                if any(num < 0 or num > 8 for num in row):
                    print(f"Each number must be between 0 and 8. Please re-enter row {i}:")
                    continue
                #check that each row is 3 numbers only
                if len(row) != 3:
                    print(f"Each row must contain exactly 3 numbers. Please re-enter row {i}:")
                    continue                
                numbers.extend(row)
                row_inputs.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers separated by spaces.")

    for row in row_inputs:
        puzzle_rows.append(np.array(row))
    #our puzzle will be a 2d numpy array    
    puzzle = np.array(puzzle_rows)

    start_state = (tuple(row_inputs[0]), tuple(row_inputs[1]), tuple(row_inputs[2]))
    problem1 = Problem(start_state)

    print("This is the 8 puzzle you entered:")
    print(puzzle)

    print("Lastly, enter which algorithm you would like to run on the puzzle.\n")
    print ("[1] Uniform Cost Search\n[2] A* with the Misplaced Tile heuristic\n[3] A* with the Manhattan Distance heuristic\n")

    alg_input = input("Input 1, 2, or 3 for the algorithm: ")
    while (alg_input not in ["1", "2", "3"]):
        alg_input = input("Invalid input. Please enter 1, 2, or 3 only: ")    
    
    cost, curr_state, path, depth, expanded, max_queue_size = None, None, None, None, None, None

    if alg_input == "1":
        cost, curr_state, path, depth, expanded, max_queue_size = uniform_cost_search(problem1)
    if alg_input == "2": 
        cost, curr_state, path, depth, expanded, max_queue_size = astar_misplaced_tile(problem1)
    if alg_input == "3":
        cost, curr_state, path, depth, expanded, max_queue_size = astar_manhattan(problem1)
    
    if cost != None:
        goal = ((1, 2, 3), 
                (4, 5, 6), 
                (7, 8, 0))
        count = 0
        print("States Expanded:")
        for state in path:
            if count  == 0:
                print("Beginning State:")
            else:
                print("State", count, "Expanded:")
            count += 1
            for row in state:
                print(row)
        print("Goal State Reached at Depth", depth)
        for row in goal:
            print(row)
        print(expanded, "States Expanded to Reach Solution")
        print("Max Queue Size:", max_queue_size)
    else:
        print("No solution")


if __name__ == "__main__":
    main()