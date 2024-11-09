# Even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_or_odd(3))
print(even_or_odd(4))
    
# Basic operations
def basic_operations(operation, value1, value2):
    if operation == "add":
        return value1 + value2
    elif operation == "subtract":
        return value1 - value2
    elif operation == "multiplay":
        return value1 * value2
    elif operation == "divide":
        if value2 != 0:
            return value1 / value2
        else:
            return "Division by zero is underfined"

print(basic_operations("subtract", 14, 7))
print(basic_operations("multiplay", 150, 270))
print(basic_operations("divide", 14, 3))
print(basic_operations("divide", 14, 0))

# Total points
def total_point(games):
    points = 0
    for game in games:
        x, y = map(int, game.split(":"))
        if x > y:
            points += 3
        elif x == y:
            points += 1
    return points

games = ["3:1", "4:4", "5:0", "1:3"]
print(total_point(games))

# The largest number
def largest_number(a, b, c):
    return max(a + b + c, a * b *c, (a + b) * c, a * (b + c))

print(largest_number(5,8,6))

# Optinal
# Showing the result and that operation has chosen 
def largest_number1(a, b, c):
    # List of combinations
    combinations = [
        (a + b + c, "a + b + c"),
        (a * b * c, "a * b * c"),
        ((a + b) * c, "(a + b) * c"),
        (a * (b + c), "a * (b + c)")
    ]
    # Finding optinal operation and Max value
    max_value, operation = max(combinations, key=lambda x: x[0])

    print(f"Chosen operation: {operation} = {max_value}")

    return max_value

print(largest_number1(5,8,6))

# Power of N-th
def index(array, number):
    if number < len(array):
        return array[number] ** number
    else:
        return -1

print(index([4, 6, 22, 7, 88], 2))
print(index([4, 6, 22, 7, 88], 5))

# Quarter of the year
def quater_of_the_yera(month):
    return (month + 2) // 3

print(quater_of_the_yera(3))
print(quater_of_the_yera(8))

# Century from year
def century(year):
    return (year + 99) // 100

print(century(2024))
print(century(1568))

# Form the minimum
def form_the_minimum(array):
    array.sort()
    smallest_number = "".join(map(str, array))
    return int(smallest_number)

print(form_the_minimum([10, 4, 22, 3, 56]))
print(form_the_minimum([3, 1, 5, 2, 4, 6, 9, 7, 8]))