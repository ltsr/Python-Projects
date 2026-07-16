import pyperclip

txt = "This is a text copied by pyperclip module"
pyperclip.copy(txt)

print(pyperclip.paste())