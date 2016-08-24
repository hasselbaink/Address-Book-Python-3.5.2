class Person:
 def __init__(self, name, number):
  self.name = name
  self.number = number

 def get_info(self):
  return self.name + ' | ' + self.number
