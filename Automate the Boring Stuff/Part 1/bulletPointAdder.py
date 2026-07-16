#! python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

#TODO: Separate lines and add asterisks.

lines = text.split('\n')

#text = ""

for i in range(len(lines)):
    lines[i] = "* " + lines[i]
    #text += lines[i]

text = "\n".join(lines)

pyperclip.copy(text)