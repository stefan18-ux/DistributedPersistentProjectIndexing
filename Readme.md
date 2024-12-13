# Simple Code Interpreter

This project implements a basic interpreter that reads a sequence of commands from an input file and processes them based on certain rules. The interpreter maintains a **mapping** of variables (keys) to **values** (stored as a list of tuples, where each tuple contains a value and its associated level). The program supports simple commands such as assignment (`=`), printing (`print`), and block-level nesting using braces (`{` and `}`). It also handles variable-level scoping.

## Features:
- **Variable Assignment**: Supports the assignment of values (both numbers and variables).
- **Printing**: Outputs the most recent value of a variable or `null` if the variable doesn't exist.
- **Block Scoping**: Variables can be scoped within blocks defined by `{}` and are removed when exiting the block.
- **Nested Levels**: Keeps track of nested levels, and each variable can have different values depending on the block depth.
- **Error Handling**: If the file isn't provided, the program will display an error and exit.


## Files:
- `main.py`: Contains the interpreter logic.
- `input.txt`: An example input file that contains the commands to be processed.

## Logic Explanation:

The core idea of the interpreter is to manage variables across different **levels** (scopes). Here's how it works:

- **Levels and Scopes**: When entering a new block (denoted by `{`), the level is incremented. Each variable has a value associated with the current level, meaning that variables can have different values in different scopes. When exiting a block (denoted by `}`), the level is decremented and variables defined at that level are removed.
  
- **Assignment**: When assigning a value to a variable, the interpreter first checks if that variable already has a value at the current level:
  - If the variable already exists at the current level, the value is updated.
  - If the variable does not exist at the current level, it is added to the list of variables at that level.
  
- **Printing**: When printing a variable, the interpreter looks for the value at the most recent level (i.e., the last assigned value).

### Example Scenario:

Consider the following sequence of commands:

```
x = 1 

scope {
    y = 2 
    print x 
}

print y 

scope { 
    z = 3 
    print x 
    print y 
    print z 
}

print z
```

The logic will execute the commands as follows:

1. `x = 1`: The variable `x` is assigned the value `1` at level `0`.
2. `{` (enter block): The level is incremented to `1`.
3. `y = 2`: The variable `y` is assigned the value `2` at level `1`.
4. `print x`: The program prints the value of `x`. At level `1`, `x` still has the value `1`, as it's defined at level `0`.
5. `}` (exit block): The level is decremented to `0`.
6. `print y`: The program prints `null`, as `y` was only defined at level `1` and is not visible at level `0`.
7. `{` (enter block): The level is incremented to `1` again.
8. `z = 3`: The variable `z` is assigned the value `3` at level `1`.
9. `print x`: The program prints `1`, as `x` is defined at level `0`.
10. `print y`: The program prints `2`, as `y` is defined at level `1`.
11. `print z`: The program prints `3`, as `z` is defined at level `1`.
12. `}` (exit block): The level is decremented to `0`.
13. `print z`: The program prints `null`, as `z` is defined only at level `1`.

### Demo Output:

```bash
[['1', 0]]
1
# x has the value 1 on the first level

[]
null
# y does not exist

[['1', 0]]
1
# x still has the value 1 from on the first level

[]
null
# y does not exist

[['3', 1]]
3
# z has the value 3 from the first level

[]
null
#z does not exist anymore
```

## How to Use:

1. **Input File**:
   Create a text file (e.g., `input.txt`) containing commands.
2. **Run the Program**:
Run the program by passing the input file as an argument:

```bash
python main.py input.txt

