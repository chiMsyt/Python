'''
Change List Items

Change Item Value

To change the value of a specific item, refer to the index number

'''
# Example:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # changes the second item
print(thislist) # ['apple', 'blackcurrant', 'cherry']

'''
Change a Range of Item Values

To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

'''
# Example:
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist2[1:3] = ["blackcurrant", "watermelon"] # changes the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
print(thislist2) # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# if you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] # change the second value by replacing it with two new values
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']

# the length of the list will change when the number of items inserted does not match the number of items replaced

# if you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] # change the second and third value by replacing it with one value
print(thislist) # ['apple', 'watermelon']

'''
Insert Items

To insert a new list item, without replacing any of the existing values, we can use the [insert()] method

The [insert()] method inserts an item at the specified index:

'''
# Example:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # insert "watermelon" as the third item
print(thislist) # ['apple', 'banana', 'watermelon', 'cherry']
# as a result of the example above, the list will now contain 4 items