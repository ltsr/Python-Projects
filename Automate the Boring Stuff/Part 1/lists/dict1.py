myCat = {"size":"fat", "color":"gray", "disposition":"loud"}

print(f"My cat has {myCat["color"]} fur.")

for k,v in myCat.items():
    print(f"Key: {k}, Value: {v}")

print("fat" in myCat.values())