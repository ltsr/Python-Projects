# arr = ["cat", "rat", "bat", "stat", "lat", "elephant"]

# # List everything except for the last element
# print(arr[:-1])

# # List starting from that element
# print(arr[2:])

# # List first and second element (index 2 is not included, so no 3rd element!!)
# print(arr[0:2])

# arr2 = [1, 2, 3] + [4, 5, 6]

# del arr2[2]

# print(arr2)

catNamesList = []

while True:
    print(f"Enter the name of a cat {str(len(catNamesList) + 1)} or enter nothing to stop: ", end="")
    nameOfCat = input()
    if nameOfCat == "":
        break
    
    catNamesList += [nameOfCat]

print("The cat names are:")
for name in catNamesList:
    print(name)