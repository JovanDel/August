import re

phoneNumber = "800-555-1212 #This my phone number"

phoneNumberClean = re.sub(r'#.*$', "Jovan", phoneNumber)
print (phoneNumberClean)

num = re.sub(r'\D', "",phoneNumber)
print (num)
