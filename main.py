from termcolor import colored
from pyfiglet import Figlet
import numpy as np

#def uniform_cost_search():


#def astar_misplaced_tile():


#def astar_manhattan():


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
    print("This is the 8 puzzle you entered:")
    print(puzzle)

    print("Lastly, enter which algorithm you would like to run on the puzzle.\n")
    print ("[1] Uniform Cost Search\n[2] A* with the Misplaced Tile heuristic\n[3] A* with the Manhattan Distance heuristic\n")

    alg_input = input("Input 1, 2, or 3 for the algorithm: ")
    while (alg_input not in ["1", "2", "3"]):
        alg_input = input("Invalid input. Please enter 1, 2, or 3 only: ")    
    if alg_input == 1:
        uniform_cost_search(puzzle)
    if alg_input == 2: 
        astar_misplaced_tile(puzzle)
    if alg_input == 3:
        astar_manhattan(puzzle)

if __name__ == "__main__":
    main()