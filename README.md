[![Run on Repl.it](https://repl.it/badge/github/NicholasDawson/Integral-Calculator)](https://repl.it/github/NicholasDawson/Integral-Calculator)

# Integral-Calculator
A program to calculate the left, right, and midpoint Riemann sums and also trapezoidal sums. 

### Parameters:
- Lower Limit
- Upper Limit
- Function (in terms of x)
- Amount of Sections (rectangles or trapezoids)

### Output:
The program will output all 4 sums listed above along with the equation used to calculate them.
Math functions are imported so you can use sin, cos, e, pi, etc. in your parameters.

### Example:
```
INTEGRAL CALCULATOR
BY: NICK DAWSON
--------------------
To use exponents use ** instead of ^
Example: (5 * x + 3)**2
====================
Enter the lower limit: 1
Enter the upper limit: 12
Enter the function: sin(x) * 5
Enter the amount of partitions: 6
--------------------
Left Sum is: 5.249
1.833 * (4.207 + 1.517 + -4.995 + 1.076 + 4.436 + -3.378)
Right Sum is: -7.383
1.833 * (1.517 + -4.995 + 1.076 + 4.436 + -3.378 + -2.683)
Midpoint Sum is: -1.753
1.833 * (4.704 + -2.858 + -3.221 + 4.529 + 0.869 + -4.981)
Trapezoidal Sum is: -1.067
1/2 * 1.833 * (4.207 + 1.517 + -4.995 + 1.076 + 4.436 + -3.378 + -2.683 + 1.517 + -4.995 + 1.076 + 4.436 + -3.378)
====================
```
