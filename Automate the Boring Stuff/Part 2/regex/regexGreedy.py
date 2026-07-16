import re

greedyRegex = re.compile(r"(Ha){3,5}") # Uses the longest possible result
mo1 = greedyRegex.search("HaHaHaHaHa")
print(mo1.group())

nonGreedyRegex = re.compile(r"(Ha){3,5}?") # Uses the shortest possible result
mo2 = nonGreedyRegex.search("HaHaHaHaHa")
print(mo2.group())