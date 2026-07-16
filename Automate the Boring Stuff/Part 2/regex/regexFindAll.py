import re

numberRegex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")

print(numberRegex.findall("Home: 455-129-7560 Work: 958-314-4491 Mobile: (333)-"))



