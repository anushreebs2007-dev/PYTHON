numbers=[1,2,3,4,5,6,7]
leftmost_even = next((x for x in numbers if x % 2 == 0), None)
if leftmost_even is not None:
    print("Leftmost even number:", leftmost_even)
else:
    print("No even number found in the list")