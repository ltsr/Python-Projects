import re

regSearch = re.compile(r"Batman|Tina Fey")

mo1 = regSearch.search("Batman and Tina Fey")

print(mo1.group())

mo2 = regSearch.search("Tina Fey and Batman")

print(mo2.group())

batManRegex = re.compile(r"Bat(man|mobile|copter|bat)")

mo3 = batManRegex.search("This Batcopter can't fly")

print(mo3.group())