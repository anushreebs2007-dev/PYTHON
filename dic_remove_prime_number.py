s = {
    'a': [1, 2, 2],
    'b': [3, 3, 4]
}
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
s = {k: [x for x in dict.fromkeys(v) if not is_prime(x)] for k, v in s.items()}
print(s)