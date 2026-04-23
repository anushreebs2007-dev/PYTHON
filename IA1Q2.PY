s = input("Enter string: ")
print("Upper:", s.upper())
print("Lower:", s.lower())
vowels = "aeiouAEIOU"
v = c = d = sp = 0
for ch in s:
    if ch.isdigit():
        d += 1
    elif ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
    else:
        sp += 1
print("Vowels:", v, "Consonants:", c, "Digits:", d, "Special:", sp)

words = s.split()
print("Longest:", max(words, key=len))
print("Shortest:", min(words, key=len))
print("Title Case:", s.title())