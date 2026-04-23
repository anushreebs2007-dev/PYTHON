print("enter the table:")
n=int(input("enter the value of n: "))
def multiplication_table(n, upto=10):
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")

multiplication_table(n)