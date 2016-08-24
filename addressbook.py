import os

class AddressBook:
 def __init__(self, path):
  self.path = path+'.txt'
  if not os.path.exists(self.path):
   f.open(self.path, 'w')
   f.close()
 def add_contact(self, person):
  f = open(self.path)
  contact_list = []
  while True:
   line = f.readline()
   if len(line) == 0:
    break
   else:
    contact_list.append(line)
  f.close()
  contact_list.append(person.get_info()+'\n')
  f = open(self.path, 'w')
  contacts = ''
  for contact in contact_list:
   contacts += contact
  f.write(contacts)
  f.close()
  print(person.get_info(), '- was be added.')

 def del_contact(self, person):
  f = open(self.path)
  contact_list = []
  while True:
   line = f.readline()
   if line == person.get_info()+'\n':
    pass
   elif len(line) == 0:
    break
   else:
    contact_list.append(line)
  f.close()
  f = open(self.path, 'w')
  contacts = ''
  for contact in contact_list:
   contacts += contact
  f.write(contacts)
  f.close()

 def show_contacts(self):
  f = open(self.path)
  print('Contacts:')
  while True:
   line = f.readline()
   if len(line) == 0:
    break
   else:
    print(line, end='')
  f.close()
