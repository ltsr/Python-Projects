import re

regexEndsWithHello = re.compile(r"(H|h)ello(\.*|!*)$")

print(regexEndsWithHello.findall("He said hello!!!"))

regexStartsWithMarth = re.compile(r"^Marth\s")

print(regexStartsWithMarth.findall("Marth is going to save the day!"))

regexAllDigits = re.compile(r"^\d+$")

print(regexAllDigits.findall("930697903026771306478439"))