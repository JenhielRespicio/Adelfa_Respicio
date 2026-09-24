# ADD THE MATH LIBRARY
import math

# SHOW ALL INPUTS NEEDED FOR THE PROGRAM
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# CALCULATE THE VALUES
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# PRINT THE SOLVED CALCULATIONS
print()
print(f"The distance between the two points is: {distance:.2f}")

# REFLECTION AND EVALUATION
# Using a library is more practical than writing calculations from scratch
# because it saves us time and makes sure of a precise result while making our code more readable
# and short.
# For example, in my activity, I managed to get the square root and power values accurately
# instead of manually writing formulas step-by-step.

# THE GUIDE QUESTION ANSWERS
# 1. The math library made our program more simple by handling all the advanced
# mathematical logic for us.
# 2. The math.sqrt() and the math.pow() functions were easy to use because we
# only needed to add our numbers into them and getting accurate results.
# 3. Without sqrt() and pow(), I would have written more lines of code since I had
# to type more formulas just to get the answers.