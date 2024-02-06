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

  def weekly_salary(self):
    return self.salary * 40

if __name__ == "__main__":
  rolf = WorkingStudent("Rolf", "MIT", 35.5)
  print(rolf.school)
  print(rolf.salary)

  rolf.marks.append(10)
  rolf.marks.append(8)
  rolf.marks.append(8)
  rolf.marks.append(7)

  print(rolf.average())
  print(rolf.weekly_salary())
