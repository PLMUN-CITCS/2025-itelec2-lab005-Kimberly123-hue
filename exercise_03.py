a = 10
b = 5
c = 3

result1 = a + b * c
print("Result of a + b * c:", result1)

result2 = (a + b) * c
print("Result of (a + b) * c:", result2)

result3 = a - b
print("Result of a - b:", result3)

result4 = a / b
result5 = a // b
print("Result of a / b:", result4)
print("Result of a // b (floor division):", result5)

result6 = a % b
result7 = a ** c
print("Result of a % b (modulus):", result6)
print("Result of a ** c (exponentiation):", result7)

result8 = (a + b - c) * (a / b)
print("Result of (a + b - c) * (a / b):", result8)

exercise_04.py

import math

number = 16
sqrt_result = math.sqrt(number)
pi_value = math.pi
angle_degrees = 30
angle_radians = math.radians(angle_degrees)
sin_result = math.sin(angle_radians)
cos_result = math.cos(angle_radians)
tan_result = math.tan(angle_radians)
exp_result = math.exp(2)
log_result = math.log(10)  # Natural log (base e)
log10_result = math.log(100, 10) # Log base 10

print("Square root of", number, "is:", sqrt_result)
print("Value of pi is:", pi_value)
print("Sine of 30 degrees (in radians) is:", sin_result)
print("Cosine of 60 degrees (in radians) is:", cos_result)
print("Tangent of 45 degrees (in radians) is:", tan_result)
print("Exponential of 2 is:", exp_result)
print("Logarithm (base e) of 10 is:", log_result)
print("Logarithm (base 10) of 100 is:", log10_result)
