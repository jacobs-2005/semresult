print("For the First semester")

def add_numbers(*args):
    return sum(args)

# Getting input for the first set of marks
marks1 = input("Enter marks for the first set, separated by space: ").split()
marks1 = [int(num) for num in marks1]  # Convert strings to integers
result1 = add_numbers(*marks1)
print(f"The sum for set 1 is: {result1}")

# Getting input for the second set of marks
marks2 = input("Enter marks for the second set, separated by space: ").split()
marks2 = [int(num) for num in marks2]  # Convert strings to integers
result2 = add_numbers(*marks2)
print(f"The sum for set 2 is: {result2}")

# Getting input for the third set of marks
marks3 = input("Enter marks for the third set, separated by space: ").split()
marks3 = [int(num) for num in marks3]  # Convert strings to integers
result3 = add_numbers(*marks3)
print(f"The sum for set 3 is: {result3}")

# Getting input for the fourth set of marks
marks4 = input("Enter marks for the fourth set, separated by space: ").split()
marks4 = [int(num) for num in marks4]  # Convert strings to integers
result4 = add_numbers(*marks4)
print(f"The sum for set 4 is: {result4}")

# Getting input for the fifth set of marks

marks5 = input("Enter marks for the fifth set, separated by space: ").split()
marks5 = [int(num) for num in marks5]  # Convert strings to integers
result5 = add_numbers(*marks5)
print(f"The sum for set 5 is: {result5}")

marks6 = input("Enter marks for the sixth set, separated by space: ").split()
marks6 = [int(num) for num in marks6]  # Convert strings to integers
result6 = add_numbers(*marks6)
print(f"The sum for set 6 is: {result6}")

# Adding the results of all sets
total_sum = result1 + result2 + result3 + result4 + result5 + result6
print(f"The total marks (sum of all sets) is: {total_sum}")

# Division function
def div(marks, total_sum):
    return total_sum / marks

# Getting input for the mark to divide the total by
mark_to_divide = int(input("Enter a mark to divide the total sum by: "))

# Performing division
division_result = div(mark_to_divide, total_sum)
print(f"The result of dividing the total marks by {mark_to_divide} is: {division_result}")
