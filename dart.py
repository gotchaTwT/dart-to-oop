class Students:

    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

    def display_student(self):
        print("-" * 30)
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Year Level: {self.year_level}")
        print("-" * 30)


class StudentInformationSystem:

    def __init__(self):
        self.students = []
        self.next_id = 1

    # ADD STUDENT
    def add_student(self):
        print("\nAdd Student")

        name = input("Enter student name: ")
        course = input("Enter student course: ")
        year_level = input("Enter student year level: ")

        student = Students(
            self.next_id,
            name,
            course,
            year_level
        )

        self.students.append(student)
        self.next_id += 1

        print(f"\nStudent {name} added successfully!")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def view_student(self):
        print("\nView Students")

        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display_student()
            print()

    def update_student(self):
        print("\nUpdate Student")

        if not self.students:
            print("No students found.")
            return

        try:
            student_id = int(input("Enter student ID to update: "))
        except ValueError:
            print("Invalid input. Please enter a valid student ID.")
            return

        student = self.find_student(student_id)

        if student is None:
            print(f"Student with ID {student_id} not found.")
            return

        updated_name = input("Enter updated name: ")
        updated_course = input("Enter updated course: ")
        updated_year_level = input("Enter updated year level: ")

        student.name = updated_name
        student.course = updated_course
        student.year_level = updated_year_level

        print(f"Student {student_id} updated successfully!")

    def delete_student(self):
        print("\nDelete Student")

        if not self.students:
            print("No students found.")
            return

        try:
            student_id = int(input("Enter student ID to delete: "))
        except ValueError:
            print("Invalid input. Please enter a valid student ID.")
            return

        student = self.find_student(student_id)

        if student is None:
            print(f"Student with ID {student_id} not found.")
            return

        self.students.remove(student)

        print(f"Student {student_id} deleted successfully!")

    def display_all_students(self):
        print("\nAll Students")

        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display_student()
            print()

    def run(self):
        while True:
            print("\n" + "-" * 30)
            print("Student Information System")
            print("-" * 30)
            print("1. Add Student")
            print("2. View Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            print("-" * 30)

            try:
                choice = int(input("Enter your choice (1-5): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
                continue

            if choice == 1:
                self.add_student()

            elif choice == 2:
                self.view_student()

            elif choice == 3:
                self.update_student()

            elif choice == 4:
                self.delete_student()

            elif choice == 5:
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")

def main():
    system = StudentInformationSystem()
    system.run()


if __name__ == "__main__":
    main()