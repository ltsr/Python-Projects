list1 = ["amazing", "tubular", "Alice", "Michael", "zoomies", "tree", "KDE"]

# list1.sort(key=str.lower) 
# This sorts by the letters but also combines the upper and lower cases
# Example: ["Alice", "KDE", "Michael", "amazing", "tree", "tubular", "zoomies"] -> ["Alice", "amazing", "KDE", "Michael", "tree", "tubular", "zoomies"]


list1.sort(reverse=True)

# list1.reverse() IS NOT THE SAME AS list1.sort(reverse=True) (This sorts the list first and then reverses the order!!!)

print(list1)