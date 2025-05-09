from main import Problem, uniform_cost_search, astar_misplaced_tile, astar_manhattan

#test cases as listed on slides https://www.dropbox.com/scl/fo/lucvvfzc0fi7zf3tdlvpx/AJFYrHAXs3fO1nj_OeFxwvc?dl=0&e=2&preview=Eight-Puzzle_briefing_and_review_of_search.pptx&rlkey=cpr5hsj0grbd3pueqm05iao21
test_cases = [
    {
        "name": "Expected to be solved at depth 0",
        "start": ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    },
    {
        "name": "Expected to be solved at depth 2",
        "start": ((1, 2, 3), (4, 5, 6), (0, 7, 8))
    },
    {
        "name": "Expected to be solved at depth 4",
        "start": ((1, 2, 3), (5, 0, 6), (4, 7, 8))
    },
    {
        "name": "Expected to be solved at depth 8",
        "start": ((1, 3, 6), (5, 0, 2), (4, 7, 8))
    },
    {
        "name": "Expected to be solved at depth 12",
        "start": ((1, 3, 6), (5, 0, 7), (4, 8, 2))
    },
    {
        "name": "Expected to be solved at depth 16",
        "start": ((1, 6, 7), (5, 0, 3), (4, 8, 2))
    },
    {
        "name": "Expected to be solved at depth 20",
        "start": ((7, 1, 2), (4, 8, 5), (6, 3, 0))
    },
    {
        "name": "Expected to be solved at depth 24",
        "start": ((0, 7, 2), (4, 6, 1), (3, 5, 8))
    }
]

algorithms = {
    "Uniform Cost Search": uniform_cost_search,
    "A* with the Misplaced Tile heuristic": astar_misplaced_tile,
    "A* with the Manhattan Distance heuristic": astar_manhattan
}


#running each test case and outputting to a new file 
with open("test_output.txt", "w") as f:
    for test_case in test_cases:
        f.write(f"=== {test_case['name']} ===\n")
        f.write("Start State:\n")
        for row in test_case["start"]:
            f.write(f"{row}\n")
        problem = Problem(test_case["start"])
        #shown for all three algorithms
        for alg_name, alg_func in algorithms.items():
            f.write(f"\nAlgorithm: {alg_name}\n")
            cost, curr_state, path, depth, expanded, max_queue_size = alg_func(problem)
            #output simply modified from main to print out to file
            if cost is not None:
                f.write("States Expanded:\n")
                count = 0
                for state in path:
                    if count == 0:
                        f.write("Beginning State:\n")
                    else:
                        f.write(f"State {count} Expanded:\n")
                    for row in state:
                        f.write(f"{row}\n")
                    count += 1

                f.write(f"Goal State Reached at Depth {depth}\n")
                for row in curr_state:
                    f.write(f"{row}\n")
                f.write(f"{expanded} States Expanded to Reach Solution\n")
                f.write(f"Max Queue Size: {max_queue_size}\n")
            else:
                f.write("No solution\n")