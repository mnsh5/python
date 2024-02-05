from course import Course
from student import Student


if __name__ == "__main__":
    subhash = Student("Subhash", "Prakash", "subhashprakash", "subhas@gmail.com", "s123kash")
    rahul = Student("Rahul", "Kumar", "rahulkumar", "rahul@gmail.com", "password123")
    amit = Student("Amit", "Singh", "amitsingh", "amit@gmail.com", "securepass")
    yuki = Student("Yuki", "Tanaka", "yukitanaka", "yuki@gmail.com", "pass123")
    akira = Student("Akira", "Sato", "akirasato", "akira@gmail.com", "pass456")
    mikhail = Student("Mikhail", "Ivanovich", "ivanivanov", "ivan@gmail.com", "russianpass")
    elena = Student("Elena", "Petrova", "elenapetrova", "elena@gmail.com", "russianpass123")
    anastasiya = Student("Anastasiya", "Viktorovna", "voronina", "voronina@gmail.com", "russianpass123")

    math_course = Course("Mathematics 101", "Professor Smith")

    math_course.add_student(subhash)
    math_course.add_student(rahul)
    math_course.add_student(amit)
    math_course.add_student(yuki)
    math_course.add_student(akira)
    math_course.add_student(mikhail)
    math_course.add_student(elena)
    math_course.add_student(anastasiya)

    math_course.list_students()
