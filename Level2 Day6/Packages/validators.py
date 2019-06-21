import re

def emailValidator(email):
    pattern = '^[0-9a-z][0-9a-z_.]{4,14}[@][a-z0-9]{3,15}[.][a-z]{2,4}'
    if re.match(pattern,str(email)):
        return True
    else:
        return False
emailValidator('babutilak234@gmail.com')

def phoneNumberValidator(number):
    pattern = '^[6-9][0-9]{9}$|^[6-9][0-9]{9}|^[+91]{10}$'
    if re.match(pattern,str(number)):
        return True
    else:
        return False