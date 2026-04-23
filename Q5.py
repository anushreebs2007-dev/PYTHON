s = input("Enter sentence: ")
words = s.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print("Frequency:", freq)
max_word = max(freq, key=freq.get)
print("Most frequent:", max_word)
sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("Sorted:", sorted_words)