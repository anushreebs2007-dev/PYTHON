s = {
    'a': [1, 2, 2],
    'b': [3, 3, 4]
}
s = {k: list(dict.fromkeys(v)) for k, v in s.items()}

print(s)