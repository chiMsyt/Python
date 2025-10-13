'''
Access Items

List items are indexed and you can access them by referring to their index number:

'''

# Example:
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # banana, since it has index of 1
# the first item has index 0

'''
Negative Indexing

Means starting from the end
-1 refers to the last item, -2 refers to the second last item, etc.

'''
print(thislist[-1]) # cherry

'''
Range of Indexes

You can specify a range of indexes by specifying where to start and wher to end the range.
When specifying a range, the return value will be a new list with the specified items.

'''
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5]) # ['cherry', 'orange', 'kiwi']
# note that it's n-1 for the end index, so in this example, it's until the 4th only
# by leaving out the start value, the range will start at the first item
print(thislist2[:4]) # ['apple', 'banana', 'cherry', 'orange']
# by leaving out the end value, the range will go on to the end of the list
print(thislist2[2:]) # ['cherry', 'orange', 'kiwi', 'melon', 'mango']

'''
Range of Negative Indexes

Specify negative indexes if you want to start the search from the end of the list

'''
# Example:
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[-4:-1]) # ['orange', 'kiwi', 'melon']
# this example returns the items from "orange" (-4) to, but NOT including "mango" (-1)

'''
Check if Item Exists

To determine if a specified item is present in a list, use the [in] keyword

'''
# Example:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")