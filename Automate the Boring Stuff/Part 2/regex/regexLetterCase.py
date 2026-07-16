import re

reg1 = re.compile("robocop", re.I) # Ignore case

print(reg1.search("RoboCop is part man, part robot, all cop.").group())

print(reg1.search("ROBOCOP protects all humans.").group())

print(reg1.search("rOBoCoP can't write its name properly.").group())