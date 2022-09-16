#Write a python program to check if all items in the tuple are the same.

t1=(2,2,2,2)
comp=0
for e in t1:
    if t1[comp]==e:
        pass
    else:
        print("all elements are not same in tuple")
        break
else:
    print("all elements are same in tuple")    