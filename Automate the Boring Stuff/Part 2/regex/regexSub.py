import re

namesRegex = re.compile(r"Agent \w+")
namesRegex2 = re.compile(r"(?<=Agent\s)\w+")
namesRegex3 = re.compile(r"Agent (\w)\w*")
print(namesRegex.sub("CENSORED", "Agent Alice gave some clues to Agent Bob."))
print(namesRegex2.sub("CENSORED", "Agent Alice gave some clues to Agent Bob."))
print(namesRegex3.sub(r"\1*****", "Agent Alice gave some clues to Agent Bob."))