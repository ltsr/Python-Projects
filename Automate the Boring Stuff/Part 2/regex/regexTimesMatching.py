import re

regex = re.compile(r"(Ha){3,5}")
regex2 = re.compile(r"(Ha){3,}")

mo1 = regex.search("HaHaHa")
mo2 = regex.search("HaHaHaHa")

mo3 = regex.search("HaHa")

print(mo1.group())
print(mo2.group())

print(mo3 == None)

mo4 = regex2.search("HaHaHaHaHaHaHa")

print(mo4.group())