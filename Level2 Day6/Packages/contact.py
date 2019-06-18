contacts = {}

def addContact(name,phone):
    # verify contact exist or not
    if name not in contacts:
        contacts[name] = phone
        print("Contact %s added" % name)
    else:
        print("contact %s already exists" % name)
    return

def searchContacts(name):
    if name in contacts:
        print(name,":" , contacts[name])
    else:
        print("%s doesnot exist" % name)
    return

def allContacts():
    for i in contacts:
        print(i,":",contacts[i])
    return

def modifyContact(name,phone):
    if name in contacts:
        contacts[name] = phone
        print("%s : %s updated successfully" %(name,phone))
    else:
        print("%s doesnot exist" % name)

def removeContact(name):
    if name in contacts:
        contacts.pop(name)
        print("%s : deleted successfully" %name)
    else:
        print("%s doesnot exist" % name)
        
def importContact(newContacts):
    contacts.update(newContacts)
    print("%s Contacts imported successfully" %len(newContacts))