class Student:
    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

    def display_student(self):
        print("-" * 30)
        print("Student Information System")
        print("-" * 30)
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Year Level: {self.year_level}")
        print("-" * 30)


class StudentInformationSystem:
    def __init__(self):
        self.students = []
        self.next_id = 1

    def add_student(self):
        print("\nADD STUDENT")

        name = input("Enter your Name: ")
        course = input("Enter your Course: ")
        year_level = input("Enter your Year Level: ")

        student = Student(
            self.next_id,
            name,
            course,
            year_level
        )

        self.students.append(student)
        self.next_id += 1

        print(f"Student {name} added successfully!")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def view_student(self):
        print("\nVIEW STUDENTS")

        if not self.students:
            print("Student not found.")
            return

        for student in self.students:
            student.display_student()
            print()

    def update_student(self):
        print("\nUPDATE STUDENT")

        if not self.students:
            print("Student not found.")
            return

        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid Student ID. Try Again!")
            return

        student = self.find_student(student_id)

        if student is None:
            print(f"Student with ID {student_id} not found.")
            return

        updated_name = input("Enter Updated Name: ")
        updated_course = input("Enter Updated Course: ")
        updated_year_level = input("Enter Updated Year Level: ")

        student.name = updated_name
        student.course = updated_course
        student.year_level = updated_year_level

        print(f"Student {student_id} is updated successfully!")

    def delete_student(self):
        print("\nDELETE STUDENT")

        if not self.students:
            print("Student not found.")
            return

        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid Student ID. Try Again!")
            return

        student = self.find_student(student_id)

        if student is None:
            print(f"Student with ID {student_id} not found.")
            return

        self.students.remove(student)

        print(f"Student with ID {student_id} deleted successfully!")

    def run(self):
        while True:
            print("\n" + "-" * 30)
            print("STUDENT INFORMATION SYSTEM")
            print("-" * 30)
            print("1. Add Student")
            print("2. View Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            print("-" * 30)

            try:
                choose = int(input("Choose No. 1 to 5: "))
            except ValueError:
                print("Invalid No. Try Again!")
                continue

            if choose == 1:
                self.add_student()

            elif choose == 2:
                self.view_student()

            elif choose == 3:
                self.update_student()

            elif choose == 4:
                self.delete_student()

            elif choose == 5:
                print("\nThank you for using the Student Information System!")
                break

            else:
                print("Invalid No. Try Again!")


def main():
    system = StudentInformationSystem()
    system.run()


if __name__ == "__main__":
    main()
