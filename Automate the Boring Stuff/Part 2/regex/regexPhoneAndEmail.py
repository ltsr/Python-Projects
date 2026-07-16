#! python3
# regexPhoneAndEmail.py - A program that finds emails and phone numbers in a text clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
                            (\d{3}|\(\d{3}\))?  # Area code
                            (\s|-|\.)?  # Separator
                            \d{3}  # First three digits
                            (\s|-|\.)  # Separator
                            \d{4}  # Last four digits
                            (\s*(ext|x|ext.)\s*\d{2,5})?  # Extension
                            )''', re.VERBOSE)
                            


# ((\d{3}|\d{3}\))?(\s|-|\.)? \d{3}(\s|-|\.)?\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?) Non-verbose

emailRegex = re.compile(r'''(
                            [a-zA-Z0-9._%+-]+ # Username
                            @                 # @ symbol
                            [a-zA-Z0-9._]+    # Domain name
                            (\.[a-zA-Z]{2-4}) # Dot something (.com, .org, etc.)
                            )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[6] != "":
        phoneNum += " +" + groups[6]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    print("No matching emails or phone numbers found.")