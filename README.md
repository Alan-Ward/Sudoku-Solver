# Sudoku-Solver

## Description and Background
As the name implies, this project is a Python script that accurately solves an incomplete matrix. I made this project in the fall of 2022, during my first year of computer science. The motivation for the project was to learn to problem solve better, specifically solving a problem I had no idea where to start. It was a great learning experience and took many hours to work out, but challenged me to think outside of the box. 

## Technical Specifics 
The input is a Sudoku matrix in the form of an 81-length array. In hindsight, a 9 by 9 matrix would have been a smarter design, but that's just part of the learning process. There are some supporting functions: vertical_check(), horizontal_check(), and cube_check(), which check to see if there are contradictions in the matrix that need to be fixed. These functions are vital for the main function sudoku_solver(). sudoku_solver() is a recursive backtracking algorithm that initially checks to see if the matrix is complete, and if not, adds a valid value to the first free cell, then runs the function with the updated matrix. There might not be detectible contradictions early on in the process, but later on, the function might get stuck, so it will go back one layer and try another value. If the incorrect(but technically undetectable) number happened many layers back, the algorithm will iterate from 1-10 and when all numbers are wrong, it will go back another layer and try that again (2-10, assuming it was already on 1). as the matrix gets more full, the process will get quicker and quicker.

## Special Case

If the inputted matrix is empty, the finished matrix will always look like this:

___________________
|1 2 3|4 5 6|7 8 9|
|4 5 6|7 8 9|1 2 3|
|7 8 9|1 2 3|4 5 6|
___________________
|2 1 4|3 6 5|8 9 7|
|3 6 5|8 9 7|2 1 4|
|8 9 7|2 1 4|3 6 5|
___________________
|5 3 1|6 4 2|9 7 8|
|6 4 2|9 7 8|5 3 1|
|9 7 8|5 3 1|6 4 2|
___________________

Notice that the first row is perfectly ordered from 1-9


## Instructions
to download the code and try it out for yourself:
1. Create a folder in the desired location
2. Navigate to the folder in a command line
3. Clone repository (git clone https://github.com/Alan-Ward/Sudoku-Solver.git)
4. Open Sudoku-Solver.py in your favorite IDE
5. Manually enter unsolved matrix into "matrix"
6. Run file

Thanks for checking out my repository
