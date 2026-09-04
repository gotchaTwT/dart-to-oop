import 'dart:io';

List<Map<String, dynamic>> students = [];

void main() {
  while (true) {
    print("==========================");
    print("STUDENT INFORMATION SYSTEM");
    print("==========================");
    print("1. Add student");
    print("2. View student");
    print("3. Update student");
    print("4. Delete student");
    print("5. Exit");
    print("==========================");

    stdout.write("Choose Between 1 to 5: ");
    int choice = int.parse(stdin.readLineSync()!);

    switch (choice) {
      case 1:
        addStudent();
        break;

      case 2:
        viewStudent();
        break;

      case 3:
        updateStudent();
        break;

      case 4:
        deleteStudent();
        break;

      case 5:
        print("5. Exit");
        return;

      default:
        print("Invalid choice. Please choose 1 to 5.");
    }
  }
}

void addStudent() {
  print("\nADD STUDENT");

  stdout.write("Name: ");
  String name = stdin.readLineSync()!;

  stdout.write("Course: ");
  String course = stdin.readLineSync()!;

  stdout.write("Year Level: ");
  String yearLevel = stdin.readLineSync()!;

  students.add({
    "id": students.length + 1,
    "name": name,
    "course": course,
    "yearLevel": yearLevel,
  });

  print("Student added successfully!\n");
}

void viewStudent() {
  print("\nVIEW STUDENT");

  if (students.isEmpty) {
    print("No Records Found\n");
    return;
  }

  for (int i = 0; i < students.length; i++) {
    var student = students[i];

    print("--------------------------");
    print("Student ID: ${student["id"]}");
    print("Name: ${student["name"]}");
    print("Course: ${student["course"]}");
    print("Year Level: ${student["yearLevel"]}");
    print("--------------------------");
  }

  print("");
}

void updateStudent() {
  print("\nUPDATE STUDENT");

  if (students.isEmpty) {
    print("No Records Found\n");
    return;
  }

  stdout.write("Enter Student ID: ");
  int id = int.parse(stdin.readLineSync()!);

  int index = students.indexWhere((student) => student["id"] == id);

  if (index == -1) {
    print("Student not found.\n");
    return;
  }

  stdout.write("Updated Name: ");
  String updatedName = stdin.readLineSync()!;

  stdout.write("Updated Course: ");
  String updatedCourse = stdin.readLineSync()!;

  stdout.write("Updated Year Level: ");
  String updatedYearLevel = stdin.readLineSync()!;

  // Update existing student
  students[index]["name"] = updatedName;
  students[index]["course"] = updatedCourse;
  students[index]["yearLevel"] = updatedYearLevel;

  print("Update Successfully!\n");
}

void deleteStudent() {
  print("\nDELETE STUDENT");

  if (students.isEmpty) {
    print("No Records Found\n");
    return;
  }

  stdout.write("Enter Student ID: ");
  int id = int.parse(stdin.readLineSync()!);

  int index = students.indexWhere((student) => student["id"] == id);

  if (index == -1) {
    print("Student not found.\n");
    return;
  }

  students.removeAt(index);

  print("Student deleted successfully!\n");
}