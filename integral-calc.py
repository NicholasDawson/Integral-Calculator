from math import *

def left_riemann_sum(function, lower_limit, upper_limit, partitions):
    subinterval_width = (upper_limit - lower_limit) / partitions
    subintervals = [lower_limit + subinterval_width * x for x in range(partitions)]
    rectangles = []
    for x in subintervals:
        rectangles.append(eval(function))
    result = subinterval_width * sum(rectangles)
    print_result = str(round(subinterval_width, 3)) + " * (" + ' + '.join([str(round(x, 3)) for x in rectangles]) + ")"
    return round(result, 3), print_result

def right_riemann_sum(function, lower_limit, upper_limit, partitions):
    subinterval_width = (upper_limit - lower_limit) / partitions
    subintervals = [lower_limit + subinterval_width * x for x in range(1, partitions + 1)]
    rectangles = []
    for x in subintervals:
        rectangles.append(eval(function))
    result = subinterval_width * sum(rectangles)
    print_result = str(round(subinterval_width, 3)) + " * (" + ' + '.join([str(round(x, 3)) for x in rectangles]) + ")"
    return round(result, 3), print_result

def midpoint_riemann_sum(function, lower_limit, upper_limit, partitions):
    subinterval_width = (upper_limit - lower_limit) / partitions
    subintervals = [lower_limit + (subinterval_width / 2) + subinterval_width * x for x in range(partitions)]
    rectangles = []
    for x in subintervals:
        rectangles.append(eval(function))
    result = subinterval_width * sum(rectangles)
    print_result = str(round(subinterval_width, 3)) + " * (" + ' + '.join([str(round(x, 3)) for x in rectangles]) + ")"
    return round(result, 3), print_result

def trapezoidal_riemann_sum(function, lower_limit, upper_limit, partitions):
    subinterval_width = (upper_limit - lower_limit) / partitions
    subintervals = [lower_limit + subinterval_width * x for x in range(partitions + 1)]
    subintervals += subintervals[1:-1]
    rectangles = []
    for x in subintervals:
        rectangles.append(eval(function))
    result = 0.5 * subinterval_width * sum(rectangles)
    print_result = "1/2 * " + str(round(subinterval_width, 3)) + " * (" + ' + '.join([str(round(x, 3)) for x in rectangles]) + ")"
    return round(result, 3), print_result

def calculate_integral(function, lower_limit, upper_limit):
    subinterval_width = (upper_limit - lower_limit) / 1000
    subintervals = [lower_limit + subinterval_width * x for x in range(1001)]
    subintervals += subintervals[1:-1]
    rectangles = []
    for x in subintervals:
        rectangles.append(eval(function))
    result = 0.5 * subinterval_width * sum(rectangles)
    return round(result, 3)

print('INTEGRAL CALCULATOR')
print('BY: NICK DAWSON')
print('=' * 20)

mode = input('Select Mode: "E" (Estimate) | "C" (Calculate): ')

print('=' * 20)

# Estimate Mode
if mode in ['e', 'E']:
    while True:
        lower_limit = eval(input("Enter the lower limit: ").replace('^', '**'))
        upper_limit = eval(input("Enter the upper limit: ").replace('^', '**'))

        function = str(input("Enter the function: ").replace('^', '**'))

        partitions = eval(input("Enter the amount of partitions: ").replace('^', '**'))


        print("-" * 20)
        left = left_riemann_sum(function, lower_limit, upper_limit, partitions)
        print("Left Sum is:", left[0])
        print(left[1])

        right = right_riemann_sum(function, lower_limit, upper_limit, partitions)
        print("Right Sum is:", right[0])
        print(right[1])
        
        midpoint = midpoint_riemann_sum(function, lower_limit, upper_limit, partitions)
        print("Midpoint Sum is:", midpoint[0])
        print(midpoint[1])

        trapezoidal = trapezoidal_riemann_sum(function, lower_limit, upper_limit, partitions)
        print("Trapezoidal Sum is:", trapezoidal[0])
        print(trapezoidal[1])

        print('=' * 20)
    
# Calculate Mode
if mode in ['c', 'C']:
    while True:
        lower_limit = eval(input("Enter the lower limit: ").replace('^', '**'))
        upper_limit = eval(input("Enter the upper limit: ").replace('^', '**'))
        function = str(input("Enter the function: ").replace('^', '**'))
        
        print("-" * 20)
        
        print('Area is: ' + str(calculate_integral(function, lower_limit, upper_limit)))

        print('=' * 20)
