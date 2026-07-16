import re

phoneNumberRegex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)") # raw string with r
matchObject = phoneNumberRegex.search("My number is (395) 321-5906. Pleased to meet you!")

try:
    print("Phone number found: " + matchObject.group()) # matchObject.group(0) also works
    print("Group 1: " + matchObject.group(1))
    print("Group 2: " + matchObject.group(2))
    areaCode, mainNumber = matchObject.groups()
    print("Area code: " + areaCode)
    print("Main number: " + mainNumber)
except:
    print("Phone number not found.")