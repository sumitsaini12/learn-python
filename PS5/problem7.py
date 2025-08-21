# can you change the  values inside a list which is contained in set my_set.

my_set = {8, 9, 7, 12, "Sumit", 123, False, (1, 2)}

"""  In Python, a set is unordered and mutable — you can add or remove elements, 
     but you cannot directly change a value (because sets do not allow indexing like lists).
"""


# change "banana" to "mango"
my_set.remove("Sumit")   # remove old
my_set.add("Sumit kumar")       # add new
my_set.update([1, 2, 93])  # add new values to the set

print("Updated set:", my_set)  # This will print the updated set with the new value.

