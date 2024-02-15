class Student:
    def __init__(self, roll_number, name, percentage):
        self.roll_number = roll_number
        self.name = name
        self.percentage = percentage

# a) Accept details of n students
n = int(input("Enter the number of students: "))
students = []

for _ in range(n):
    roll_number = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    percentage = float(input("Enter Percentage: "))
    student = Student(roll_number, name, percentage)
    students.append(student)

# b) Search details of a particular student on the basis of roll number
search_roll_number = int(input("Enter Roll Number to search: "))
found_student = None

for student in students:
    if student.roll_number == search_roll_number:
        found_student = student
        break

if found_student:
    print("Details of the searched student:")
    print("Roll Number:", found_student.roll_number)
    print("Name:", found_student.name)
    print("Percentage:", found_student.percentage)
else:
    print("Student not found.")

# c) Display the result of all the students
print("\nDetails of all students:")
for student in students:
    print(f"Roll Number: {student.roll_number}, Name: {student.name}, Percentage: {student.percentage}")

# d) Find the topper amongst them
topper = max(students, key=lambda x: x.percentage)
print("\nTopper:")
print("Roll Number:", topper.roll_number)
print("Name:", topper.name)
print("Percentage:", topper.percentage)
