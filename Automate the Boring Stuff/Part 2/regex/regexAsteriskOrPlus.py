import re

batRegex = re.compile(r"Bat(wo)*man") # Matches zero or multiple instances of "wo"

mo1 = batRegex.search("The Adventures of Batman")
mo2 = batRegex.search("The Adventures of Batwoman")
mo3 = batRegex.search("The Adventures of Batwowowowowowoman")

print(mo1.group())
print(mo2.group())
print(mo3.group())

batRegex2 = re.compile(r"Bat(wo)+man") # Matches one or multiple instances of "wo"

mo4 = batRegex2.search("The Adventures of Batman")

print(mo4 == None)