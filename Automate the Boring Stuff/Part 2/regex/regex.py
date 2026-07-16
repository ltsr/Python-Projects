import re

phoneNumberRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") # raw string with r
matchObject = phoneNumberRegex.search("My number is 395-321-5906. Pleased to meet you!")

try:
    print("Phone number found: " + matchObject.group())
except:
    print("Phone number not found.")