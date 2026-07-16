import re

batRegex = re.compile(r"Bat(wo)?man")

mo1 = batRegex.search("The Adventures of Batman")

mo2 = batRegex.search("The adventures of Batwoman")

print(mo1.group())
print(mo2.group())

phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")

mo3 = phoneRegex.search("My number is 324-331-5019")
mo4 = phoneRegex.search("My number is 555-4321")

print(mo3.group())
print(mo4.group())
