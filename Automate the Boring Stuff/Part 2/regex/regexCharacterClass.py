import re

xmasRegex = re.compile(r"\d+\s\w+") # One or more digits \d+, empty space \s, one or more letters, numbers or underscore \w+

print(xmasRegex.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"))


exampleText = "This is an example of a text that contains both vowels and consonants. It took at least 2 minutes to write this text."
vowelRegex = re.compile(r"[aiueoAIUEO]")
print(vowelRegex.findall(exampleText))
print("*****************************")
consonantRegex = re.compile(r"[^\s\W\daiueoAIUEO]") # Exclude vowels, numbers, underscores, spaces
print(consonantRegex.findall(exampleText))
