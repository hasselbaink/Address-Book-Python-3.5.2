#!/usr/bin/env python3

import os
import sys

class Person:
 def __init__(self, name, number):
  self.name = name
  self.number = number

 def get_info(self):
  return self.name + ' | ' + self.number

class AddressBook:
 def __init__(self, path):
  self.path = path + '.txt'
  if not os.path.exists(self.path):
   f = open(self.path, 'w')
   f.close()

 def add_contact(self, person):
  f = open(self.path, 'r')
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
  f = open(self.path, 'r')
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
  f = open(self.path, 'r')
  print('Contacts:')
  while True:
   line = f.readline()
   if len(line) == 0:
    break
   else:
    print(line, end='')
  f.close()

if len(sys.argv) == 3:
 if sys.argv[1] == 'show':
  addrbook = AddressBook(sys.argv[2])
  addrbook.show_contacts()
elif len(sys.argv) == 6:
 if sys.argv[1]=='add' and sys.argv[2]=='contact':
  person = Person(sys.argv[3], sys.argv[4])
  addrbook = AddressBook(sys.argv[5])
  addrbook.add_contact(person)
 elif sys.argv[1]=='del' and sys.argv[2]=='contact':
  person = Person(sys.argv[3], sys.argv[4])
  addrbook = AddressBook(sys.argv[5])
  addrbook.del_contact(person)
