class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age



def main_menu():
    print()
    print("What would you like to do?")
    print("1. Create New Students")
    print("e. Exit")

    option = input("Please type the number corresponding to the action? ")

    if option == "1":
        create_new_students()
    if option == "e":
        exit()


def create_new_students():
    print("Press Enter to stop entering students")
    student_name = input("Enter the student's name ")

    if student_name == "":
        main_menu()

    student_age = input("Enter the student's age ")

    student1 = Student(student_name, student_age)
    print(student1.name)
    print(student1.age)

    create_new_students()

