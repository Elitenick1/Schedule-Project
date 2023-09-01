import csv

class ClassSection:
  all_classes = {}

def __init__(self, name, teacher, period, size):
  self.class_name = name
  self.teacher = teacher
  self.period = period
  self.size = int(size)
  self.roster = []
  try:
    ClassSection.all_classes[self.class_name].append(self)
  except:
    ClassSection.all_classes[self.class_name] = []
    ClassSection.all_classes[self.class_name].append(self)
    
  def __repr__(self):
    return f"{self.class_name} taught by {self.teacher} in period {self.period}"
    
  @classmethod
  def import_classes(cls, filename: str):
    with open(filename, "r") as f:
      reader = csv.DictReader(f)
      items= list(reader)
    for item in items:
      ClassSection(
        name = item.get('name'),
        teacher = item.get('teacher'),
        size = item.get('class size'),
        
      )