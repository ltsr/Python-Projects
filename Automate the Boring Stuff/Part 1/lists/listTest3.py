things = ["apple", "banana", "tofu", "cat", "mouse", "juice", "stone", "house"]
text = ""

for i in range(0, len(things)-2):
    text += str(things[i]).capitalize() + ", "

text += str(things[-2]).capitalize() + " and " + str(things[-1]).capitalize()

print(text)