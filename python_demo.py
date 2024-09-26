import json
from abc import ABC, abstractmethod
 
# Abstract class (Abstraction)
class Person(ABC):
    def __init__(self, name, age):
        self._name = name  # Encapsulation (Protected Attribute)
        self.age = age
 
    @abstractmethod
    def get_details(self):
        pass
 
# Teacher class inheriting from Person (Inheritance)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
 
    def get_details(self):
        return f"Teacher Name: {self._name}, Age: {self.age}, Subject: {self.subject}"
 
# Student class inheriting from Person (Inheritance and Polymorphism)
class Student(Person):
    def __init__(self, name, age, student_id, marks):
        super().__init__(name, age)
        self.student_id = student_id
        self.marks = marks
 
    def get_details(self):
        average_marks = sum(self.marks) / len(self.marks) if self.marks else 0
        return f"Student Name: {self._name}, Age: {self.age}, ID: {self.student_id}, Average Marks: {average_marks:.2f}"
 
# File Handling Functions
def save_data_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Data saved to {filename} successfully.")
    except Exception as e:
        print(f"Error saving data to file: {e}")
 
def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Data loaded from {filename} successfully.")
        return data
    except FileNotFoundError:
        print(f"{filename} not found.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []
 
# Data: Lists of teachers and students
teachers = [
    Teacher("Alice", 40, "Math"),
    Teacher("Bob", 35, "English")
]
 
students = [
    Student("John Doe", 16, 1001, [85, 78, 92]),
    Student("Jane Smith", 17, 1002, [88, 90, 79])
]
 
# Set of registered subjects (using Set)
subjects = {"Math", "English", "Science"}
 
# Dictionary of registered users (Dictionary)
registered_users = {
    "admin": "admin123",
    "teacher": "teach123",
    "student": "stud123"
}
 
# Tuple of admin privileges (using Tuple)
admin_privileges = ("add user", "remove user", "view logs")
 
# Function to show menu and handle user choices
def show_menu():
    while True:
        print("\nMenu:")
        print("1. Show Teachers Data")
        print("2. Show Students Data")
        print("3. Save Data to File")
        print("4. Load Data from File")
        print("5. Add New Teacher")
        print("6. Add New Student")
        print("7. Show Available Subjects")
        print("8. Show Admin Privileges")
        print("9. Exit")
 
        try:
            choice = int(input("Enter your choice (1-9): "))
 
            if choice == 1:
                print("\nTeachers Data:")
                for teacher in teachers:
                    print(teacher.get_details())
 
            elif choice == 2:
                print("\nStudents Data:")
                for student in students:
                    print(student.get_details())
 
            elif choice == 3:
                # Save both teachers and students data to a file (File Handling)
                data = {
                    "teachers": [teacher.get_details() for teacher in teachers],
                    "students": [student.get_details() for student in students]
                }
                save_data_to_file(data, 'school_data.json')
 
            elif choice == 4:
                # Load data from file (File Handling)
                data = load_data_from_file('school_data.json')
                print("Loaded Data: ", data)
 
            elif choice == 5:
                # Adding a new teacher (List usage)
                name = input("Enter teacher's name: ")
                age = int(input("Enter teacher's age: "))
                subject = input(f"Enter subject from available subjects {subjects}: ")
 
                if subject in subjects:
                    teachers.append(Teacher(name, age, subject))
                    print("Teacher added successfully.")
                else:
                    print("Invalid subject. Please choose from available subjects.")
 
            elif choice == 6:
                # Adding a new student (List usage)
                name = input("Enter student's name: ")
                age = int(input("Enter student's age: "))
                student_id = int(input("Enter student ID: "))
                marks = list(map(int, input("Enter marks (comma-separated): ").split(',')))
                students.append(Student(name, age, student_id, marks))
                print("Student added successfully.")
 
            elif choice == 7:
                print(f"Available Subjects: {subjects}")  # Display subjects (Set)
 
            elif choice == 8:
                print(f"Admin Privileges: {admin_privileges}")  # Display admin privileges (Tuple)
 
            elif choice == 9:
                print("Exiting...")
                break
 
            else:
                print("Invalid choice. Please choose a number between 1 and 9.")
 
        except ValueError:
            print("Please enter a valid number.")
 
# Function to demonstrate exception handling
def login():
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    try:
        if registered_users[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password!")
    except KeyError:
        print("Username not found!")
    except Exception as e:
        print(f"An error occurred during login: {e}")
 
# Start the program
if __name__ == "__main__":
    login()
    show_menu()