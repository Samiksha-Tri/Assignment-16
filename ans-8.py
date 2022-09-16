"""Write a python program to Sort a tuple of tuples by the second item.
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))"""
from operator import itemgetter

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
SortedTuple = tuple(sorted(tuple1, key=itemgetter(1)))
print(SortedTuple)
