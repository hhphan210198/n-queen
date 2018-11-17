This includes solvers for two n-queen problems:
1. nqueen_minconflict.py solves a random-generated n-queen problem using the min-conflict heuristic function. The program
takes two argument, the number of trials and the board size, and prints out the initial board, solution board, 
and number of iterations it takes in each trial. At the end, it also prints out the average number of iterations. One
will realize that the number of iterations it takes to solve a given board is independent of the board's size (which is
usually about 100).
2. nqueen_solution prints out the number of solutions for the n-queen problems using backtracking. It counts the number 
of solution quite fast for boards of size up to 10. However, from n = 11, it starts taking much longer to compute. 
