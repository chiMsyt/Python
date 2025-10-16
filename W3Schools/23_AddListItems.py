'''
Append Items

To add an item to the end of the list, use the [append()] method
'''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

'''
Insert Items

To insert a list item at a specified index, use the insert() method.

'''
thislist2 = ["apple", "banana", "cherry"]
thislist2.insert(1, "orange") # Insert an item as the second position
print(thislist2)
# As a result of the examples above, the lists will now contain 4 items

'''
Extend List

To append elements from another list to the current list, use the extend() method.

'''
thislist3 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist3.extend(tropical) # Add the elements of tropical to thislist
print(thislist3)
# The elements will be added to the end of the list

'''
Add Any Iterable

The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

'''
thislist4 = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist4.extend(thistuple) # Add elements of a tuple to a list
print(thislist4)