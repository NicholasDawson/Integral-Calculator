[![Run on Repl.it](https://repl.it/badge/github/NicholasDawson/Integral-Calculator)](https://repl.it/github/NicholasDawson/Integral-Calculator)

# Integral-Calculator
A program to estimate the left, right, and midpoint Riemann sums and also trapezoidal sums. 
It can also calculate the exact area under the curve of a function.

## Parameters:
#### Estimate Mode:
- Lower Limit
- Upper Limit
- Function (in terms of x)
- Amount of Sections (rectangles or trapezoids)
#### Calculate Mode:
- Lower Limit
- Upper Limit
- Function (in terms of x)

## Output:
#### Estimate Mode: 
The program will output all 4 sums listed above along with the equation used to calculate them.
Math functions are imported so you can use sin, cos, e, pi, etc. in your parameters.
#### Calculate Mode:
The program will output the area under the curve rounded to 3 decimal places.

## Example Calculate Mode:
```
INTEGRAL CALCULATOR
BY: NICK DAWSON
====================
Select Mode: "E" (Estimate) | "C" (Calculate): C
====================
Enter the lower limit: 0
Enter the upper limit: 12
Enter the function: 5^2 + 5 * x
--------------------
Area is: 660.0
====================
```

## Example Estimate Mode:
```
INTEGRAL CALCULATOR
BY: NICK DAWSON
====================
Select Mode: "E" (Estimate) | "C" (Calculate): E
====================
Enter the lower limit: 0
Enter the upper limit: 12
Enter the function: x^2
Enter the amount of partitions: 5
--------------------
Left Sum is: 414.72
2.4 * (0.0 + 5.76 + 23.04 + 51.84 + 92.16)
Right Sum is: 760.32
2.4 * (5.76 + 23.04 + 51.84 + 92.16 + 144.0)
Midpoint Sum is: 570.24
2.4 * (1.44 + 12.96 + 36.0 + 70.56 + 116.64)
Trapezoidal Sum is: 587.52
1/2 * 2.4 * (0.0 + 5.76 + 23.04 + 51.84 + 92.16 + 144.0 + 5.76 + 23.04 + 51.84 + 92.16)
====================
```
