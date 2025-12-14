# Task 1: Python Basics & Data Types

# Declaring variables
age = 25 # int
height = 5.4 # float
name = "Binal" # string
is_student = True # boolean

print(age, height, name, is_student)

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Name:", name)
print("Age:", age)
print("Marks:", marks)

# Arithmetic operations
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Task 2: Data Structures & Loops

# List of numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Dictionary
student = {
    "name": "Binal",
    "age": 25,
    "course": "Data Analytics",
    "marks": 88
}

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)

# Task 3: Functions & Lambda

# Total & average marks
def calculate_total_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

marks_list = [70, 80, 90]
total, avg = calculate_total_avg(marks_list)
print("Total:", total)
print("Average:", avg)

# Even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))

# Lambda function (square)
square = lambda x: x * x
print("Square:", square(5))

# Return even numbers from list
def get_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

print(get_even_numbers(numbers))
# Task 4: File Handling

# Create & write file
with open("sample.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5\n")

# Read file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Append content
with open("sample.txt", "a") as file:
    file.write("Line 6\n")

# Count lines
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))
# Task 5: CSV, JSON & Regex

import csv
import json
import re

# CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Binal", 25, 88])
    writer.writerow(["Amit", 24, 78])

# Read CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# JSON file
students_data = [
    {"name": "Binal", "age": 25},
    {"name": "Amit", "age": 24},
    {"name": "Neha", "age": 23}
]

with open("students.json", "w") as file:
    json.dump(students_data, file, indent=4)

# Regex operations
text = "My phone number is 98765-43210!"

# Extract numbers
print(re.findall(r"\d+", text))

# Remove special characters
print(re.sub(r"[^a-zA-Z0-9 ]", "", text))

# Validate phone number
phone = "9876543210"
if re.match(r"^\d{10}$", phone):
    print("Valid phone number")
else:
    print("Invalid phone number")
# Task 6: Mini Python Program

import re

# Take input
user_text = input("Enter some text: ")

# Store in file
with open("user_data.txt", "w") as file:
    file.write(user_text)

# Read file
with open("user_data.txt", "r") as file:
    data = file.read()

# Clean data using regex
cleaned_data = re.sub(r"[^a-zA-Z0-9 ]", "", data)

# Display result
print("Cleaned Output:", cleaned_data)


