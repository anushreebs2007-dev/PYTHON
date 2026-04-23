n = int(input("Enter number: "))
if n > 1 and all(n % i != 0 for i in range(2, n)):
    print("Prime")
else:
    print("Not Prime")
def fact(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f
print("Factorial:", fact(n))
print("Sum of digits:", sum(map(int, str(n))))
a, b = 5, 10
a, b = b, a
print("Swapped:", a, b)
terms = int(input("Terms: "))
a, b = 0, 1
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a+b