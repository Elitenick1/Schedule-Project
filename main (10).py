import random
from StudentClass import Student
from ClassSection import ClassSection

def roster(student):
  two = len(student.requests)
  one  = list(student.schedule.values())
  one = [x for x in one if x is not None]
  lone = len(one)
  return f"{student.name} is in {student.grade} \n They have {lone} out of {two} classes \n {student.schedule}"

if __name__ == '__main__':
  Student.import_student("sample student data no names.csv")
  ClassSection.import_classes("sample class data.csv")

  #shuffling the schedule
  random.shuffle(Student.all_students)
  for x in Student.all_students:
    Student.scheduling(x)

  #number of perfect and imperfect schedules
  imperfects = []
  pamount = 0
  impamount = 0
  for x in Student.all_students:
    if x.perfect == True:
      pamount += 1
    elif x.perfect == False:
      impamount += 1
      imperfects.append(x)

      
  for i in imperfects:
    print(i)
  print()
  
  print(f"{pamount} students have a perfect schedule")
  print(f"{impamount} students have an imperfect schedule")
  print(f"{round(pamount/(pamount + impamount) * 100, 2)}% of students have a perfect schedule")
