allGuests = {"Alice" : {"Apples" : 5, "Pretzels" : 12}, "Bob" : {"Ham sandwiches" : 3, "Apples" : 2}, "Carol" : {"Cups" : 3, "Apple pies" : 1} }

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought += v.get(item, 0)
    return numBrought

print("Number of items being brought: ")
print("Apples: " + str(totalBrought(allGuests, "Apples")))
print("Cups: " + str(totalBrought(allGuests, "Cups")))
print("Cakes: " + str(totalBrought(allGuests, "Cakes")))
print("Ham sandwiches: " + str(totalBrought(allGuests, "Ham sandwiches")))
print("Apple pies: " + str(totalBrought(allGuests, "Apple pies")))