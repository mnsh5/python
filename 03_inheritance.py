class Student:
  def __init__(self, name, school) -> None:
    self.name = name
    self.school = school
    self.marks = []

  def average(self):
    return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
  def __init__(self, name, school, salary) -> None:
    super().__init__(name, school) # Student
    self.salary = salary

rolf = WorkingStudent("Rolf", "MIT", 15.5)
print(rolf.school)
print(rolf.salary)
