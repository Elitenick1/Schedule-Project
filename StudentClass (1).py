import random
import csv
from ClassSection import ClassSection

class Student:
  all_students = []
  def __init__(self, name, grade, advisor, reqs):
    self.name = name
    self.grade = grade
    self.advisor = advisor
    self.requests = [req for req in reqs if req != "" and req != "Study Skills"]
    self.schedule = {
      "Q1/3 P1": None,
      "Q1/3 P2": None,
      "Q1/3 P3": None,
      "Q1/3 P4": None,
      "Q2/4 P1": None,
      "Q2/4 P2": None,
      "Q2/4 P3": None,
      "Q2/4 P4": None,
    }
    Student.all_students.append(self)

  def scheduling(self):
    added = 0 
    random.shuffle(self.requests)
    length = list(self.schedule.values())
    length = [x for x in length if x != None]
    for i in self.requests:
      if i != "Latin 5" and i != "Latin 4" and i != "Continuing Studies in Drawing  Painting & 2D Design" and i != "Independent Study - The New Space Race" and i != "Honors Latin 5: Adv. Latin Prose" and i != "Anatomy and Physiology" and i != "Honors Latin 4: Adv. Latin Prose" and i != "Honors Latin 4/5: Adv. Latin Prose":
        
        for j in ClassSection.all_classes[i]:
          roster_length = len(j.roster)
          if len(j.roster) < j.size and len(self.requests) > len(length):
            if self.schedule[j.period] is None:
              added += 1
              self.schedule[j.period] = 1
              break
          else:
            pass
    if added == len(self.requests):
      self.perfect = True
    if self.perfect == True:
      pass
    else:
      try:
        Student.rescheduling()
      except:
        pass

  @staticmethod
  def rescheduling(student):
    while student.perfect is not True:
      for x in student.schedule:
        sce = student.schedule[x]
        sce.remove(student)
      student.schedule = {
        "Q1/3 P1": None,
        "Q1/3 P2": None,
        "Q1/3 P3": None,
        "Q1/3 P4": None,
        "Q2/4 P1": None,
        "Q2/4 P2": None,
        "Q2/4 P3": None,
        "Q2/4 P4": None,
      }
      student.scheduling()

  def __repr__(self):
    print()
    two = len(self.requests)
    one = list(self.schedule.values())
    one = [x for x in one if x != None]
    lone = len(one)
    string = ""
    keys = list(self.schedule.keys())
    values = list(self.schedule.values())
    for x in range(len(self.schedule)):
      string = string + f"\n\t{keys[x]}: {values[x]}"
    return f"{self.name}, {self.grade}th grade. {lone} out of {two} classes {string}"

  @classmethod
  def import_student(cls, filename:str):
    with open (filename, "r") as f:
      reader = csv.DictReader(f)
      items = list(reader)
    for item in items:
      Student(
        name = item.get('name'),
        grade = item.get('grade'),
        advisor = item.get('advisor'),
        reqs = [item.get('req1'), item.get('req2'), item.get('req3'), item.get('req4'), item.get('req5'), item.get('req6'), item.get('req7'), item.get('req8'), item.get('req9')]
        )