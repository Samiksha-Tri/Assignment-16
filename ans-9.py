"""Write a python program to print the value 20 from given nested tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))"""

tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
for i in tuple1:
    for e in i:
        if e==20:
            print(e)

