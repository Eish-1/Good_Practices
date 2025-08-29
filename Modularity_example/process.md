================

# An Example of modular programming

================

1. Understand the problem
2. plan the solution
3. implement

The problem

Going to plan it using hierarchy charts.

The solution

## Problem

lowest score drop: so take input values of marks , remove the lowest one , calculate the average, add input validation that's it

## Breaking it down in hierarchy

main
|-- get_score()
|-- calc_avg()
|-- |-- find_lowest()

## good practice

1. Write pseudocode, lay down the logical steps in simple words before implementation
2. As you write each function, test it in the main file. So that you know if anything explodes, dynamite wasn't present in the previous functions
