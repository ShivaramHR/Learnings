# Custom Interpreter

A small programming language interpreter written in Python.

## Features
- print statements
- variables
    Syntax:
    - var x = 5 {this assigns the value of x to 5}
    - you can now use math operations in variables
    Eg: var x = 4 5 add {it assigns the value of x to 9}
- stacks and their operations
    Syntax:
    - stack x [1,2,3] {creates a new stack}
    - stack append variable_name value
    - stack pop variable_name
    - stack del variable_name index 
- arithmetic operations
    Syntax:
    - math n1 n2 op
- multi-number math operations
- operator dispatch table
- more features will be added

## Example program

var x 10
var y 5

math x y add
print "done"

## Run

python main.py program.my