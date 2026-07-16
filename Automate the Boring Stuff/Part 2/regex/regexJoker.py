import re

reg_1 = re.compile(r"\w+?.at")

print(reg_1.findall("The cat in the hat sat on the flat mat."))

reg_2 = re.compile(r"First name: (.*) Last name: (.*)")

mo = reg_2.search("First name: Al Last name: Sweigart")

mo1 = mo.group(1)
mo2 = mo.group(2)

print(f"{mo1} {mo2}")

reg_3 = re.compile(r"<.*?>")

print(reg_3.findall("<This is a sentence 1.> This is now a sentence 2.>"))

reg_4 = re.compile(".*")
reg_4_DOTALL = re.compile(".*", re.DOTALL)

print(reg_4.search("Serve the public trust.\nProtect the innocent.\nUphold the law.").group())
print("**********************\n**********************\n**********************\n**********************\n")
print(reg_4_DOTALL.search("Serve the public trust.\nProtect the innocent.\nUphold the law.").group())