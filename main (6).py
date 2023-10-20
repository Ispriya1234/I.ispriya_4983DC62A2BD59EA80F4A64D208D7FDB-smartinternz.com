class Student:

  def __init__(self, name, roll_number, cgpa ):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  sorted_students  = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students

students = [
  Student("Dinesh","A1","8.7"),
  Student("aarthi","A2","8.9"),
  Student("Karthi","A3","9.2"),
  Student("priya","A4","9.9"),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))
  