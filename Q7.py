names = input("Enter names: ").split()
d = {name: len(name) for name in names}
print(d)
print("Longest:", max(d, key=d.get))
print("Shortest:", min(d, key=d.get))
print("Sorted:", dict(sorted(d.items(), key=lambda x: x[1])))
print("Length >5:", [k for k,v in d.items() if v > 5])
print("Keys:", d.keys())
print("Values:", d.values())
x = input("Check name: ")
print(x in d)
d[x] = len(x)
del d[names[0]]
print("Total items:", len(d))