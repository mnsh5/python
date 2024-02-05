class Course:
  def __init__(self, name, instructor) -> None:
    self.name = name
    self.instructor = instructor
    self.students = []

  def add_student(self, student):
    self.students.append(student)
    print(f"{student.first_name} {student.last_name} has been added to the course {self.name}.")

  def list_students(self):
    print(f"Students enrolled in {self.name}:")
    for student in self.students:
        print(f"- {student.first_name} {student.last_name}")

