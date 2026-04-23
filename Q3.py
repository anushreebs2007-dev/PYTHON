students = {"A": 85, "B": 90, "C": 78}
print("Highest:", max(students, key=students.get))
print("Lowest:", min(students, key=students.get))
avg = sum(students.values()) / len(students)
print("Average:", avg)
sorted_dict = dict(sorted(students.items(), key=lambda x: x[1]))
print("Sorted:", sorted_dict)
students["D"] = 88
del students["A"]
# Remove duplicate values
unique = {}
for k, v in students.items():
    if v not in unique.values():
        unique[k] = v
print("No duplicates:", unique)
print(students.get("B"))
students["B"] = 95
for k, v in students.items():
    print(k, v)
print("B exists:", "B" in students)
d2 = {"E": 70}
students.update(d2)
s = "hello"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
keys = ["x", "y"]
values = [1, 2]
d = dict(zip(keys, values))
print(d)