#!/usr/bin/env python3

import sys
import person
import addressbook

if len(sys.argv) == 3:
 if sys.argv[1] == 'show':
  addrbook = addressbook.AddressBook(sys.argv[2])
  addrbook.show_contacts()
elif len(sys.argv) == 6:
 if sys.argv[1]=='add' and sys.argv[2]=='contact':
  pers = person.Person(sys.argv[3], sys.argv[4])
  addrbook = addressbook.AddressBook(sys.argv[5])
  addrbook.add_contact(pers)
 elif sys.argv[1]=='del' and sys.argv[2]=='contact':
  pers = person.Person(sys.argv[3], sys.argv[4])
  addrbook = addressbook.AddressBook(sys.argv[5])
  addrbook.del_contact(pers)
