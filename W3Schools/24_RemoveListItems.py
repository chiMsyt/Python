'''
Remove Specified Item

The remove() method removes the specified item.

'''
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # Remove "banana"
print(thislist)
# If there are more than one item with the specified value, the remove() method removes the first occurrence
thislist2 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist2.remove("banana") # Remove the first occurrence of "banana"
print(thislist2)

'''
Remove Specified Index

The pop() method removes the specified index.

'''
thislist3 = ["apple", "banana", "cherry"]
thislist3.pop(1) # Remove the second item
print(thislist3)
# If you do not specify the index, the pop() method removes the last item
thislist3 = ["apple", "banana", "cherry"]
thislist3.pop() # Remove the last item
print(thislist3)
# The del keyword also removes the specified index
thislist3 = ["apple", "banana", "cherry"]
del thislist3[0] # Remove the first item
print(thislist3)
# The del keyword can also delete the list completely
thislist3 = ["apple", "banana", "cherry"]
del thislist3 # Delete the entire list

'''
Clear the List

The clear() method empties the list.

The list still remains, but it has no content.

'''
thislist4 = ["apple", "banana", "cherry"]
thislist4.clear() # Clear the list content
print(thislist4)