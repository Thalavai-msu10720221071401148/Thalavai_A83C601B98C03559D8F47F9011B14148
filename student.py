class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"{self.name}, {self.roll_number}, CGPA: {self.cgpa}"

def sort_students(student_list):
    # Sort the student_list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students1 = [
    Student("Alice", "001", 3.9),
    Student("Bob", "002", 3.8),
    Student("Charlie", "003", 4.0),
    Student("David", "004", 3.7),
]

students2 = [
    Student("Eve", "005", 3.5),
    Student("Frank", "006", 3.6),
    Student("Grace", "007", 3.9),
]

sorted_students1 = sort_students(students1)
sorted_students2 = sort_students(students2)

print("Sorted Students 1:")
for student in sorted_students1:
    print(student)

print("\nSorted Students 2:")
for student in sorted_students2:
    print(student)