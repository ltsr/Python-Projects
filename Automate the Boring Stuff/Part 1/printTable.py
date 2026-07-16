tableData = [["apples", "oranges", "cherries", "banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["dogs", "cats", "moose", "goose"]]

i = 0
j = 0

#print(len(tableData))
#print(len(tableData[0]))

for j in range(0, len(tableData[0])):
    print()
    for i in range(0, len(tableData)):
        print(tableData[i][j], end=" ")