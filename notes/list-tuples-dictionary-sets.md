### list
* **strings and lists**
* 'str' object does not support item assignment
*  example: Create an empty list
            myList = []
            Append values to this list
            myList.append('a')
            myList.append('3')
            myList.append('a')
            Print this list
            print(myList)
            ['a', '3', 'a']
            Change the value of a list member
            To show that lists are mutable
            myList[1] = (48)
            print(myList)
            ['a', 48, 'a']
            
            
* **Python list methods**
* append(): Adds an element at the end of the list
* clear(): Removes all the elements from the list
* copy(): Returns a copy of the list
* count(): Returns the number of elements with the specified value
* extend(): Add the elements of a list (or any iterable), to the end of the current list
* index(): Returns the index of the first element with the specified value
* insert(): Adds an element at the specified position
* pop(): Removes the element at the specified position
* remove(): Removes the first item with the specified value
* reverse(): Reverses the order of the list
* sort(): Sorts the list
* example: 
*append()
myList.append(65.98)
print(myList)
['a', 48, 'a', 65.98, 65.98]

*copy()
myCopy = myList.copy()
print(myCopy)
['a', 48, 'a', 65.98, 65.98]

*clear()
myCopy.clear()
print(myCopy)
[]
count()
myList.count('a')
2

*extend()
We will make a copy again and extend that copy
myCopy = myList.copy()
print(myCopy)
myCopy.extend(['a',5,"Hi"])
print(myCopy)
['a', 48, 'a', 65.98, 65.98]
['a', 48, 'a', 65.98, 65.98, 'a', 5, 'Hi']

index()
myCopy.index(5)
6

insert()
We will insert a a new element at position 5. Keep in mind that this is the sixth position because indexing in Python starts at 0.
myCopy.insert(5, "I'm new!")
print(myCopy)
['a', 48, 'a', 65.98, 65.98, "I'm new!", 'a', 5, 'Hi']

pop()
Let's remove the element that we just added. That means we want to remove the 6th element indexed by 5
myCopy.pop(5)
print(myCopy)
['a', 48, 'a', 65.98, 65.98, 'a', 5, 'Hi']

remove()
If I remove 'a', it will remove the first of the three occurence of 'a'
myCopy.remove('a')
print(myCopy)
[48, 'a', 65.98, 65.98, 'a', 5, 'Hi']

reverse()
myCopy.reverse()
print(myCopy)
['Hi', 5, 'a', 65.98, 65.98, 'a', 48]

sort()
We have to be careful with sort(). This function does not support mixed data types that we have for our list.
So we will create a new list of the same data type (either numeric or string, etc.)
l = [20, 3.5, 7, 6, 4, 8.0, 7, 6.98, 19]
print(l)
l.sort()
print(l)
[20, 3.5, 7, 6, 4, 8.0, 7, 6.98, 19]
[3.5, 4, 6, 6.98, 7, 7, 8.0, 19, 20]

### Tuples
Tuples are like lists, except that they are immutable
Why or when would we use tuples
When you have a collection of unchangeable values like days of a week or months in a year, etc.
When to want more efficiency
Tuples are used for grouping data

Tuple methods
count(): Returns the number of times a specified value occurs in a tuple
index(): Searches the tuple for a specified value and returns the position of where it was found


### Dictionaries
A dictionary is mutable container type
It that can store any number of Python objects, including other container types.
Dictionaries consist of pairs (called items) of keys and their corresponding values

Dictionary methods
clear(): Removes all the elements from the dictionary
copy(): Returns a copy of the dictionary
fromkeys(): Returns a dictionary with the specified keys and values
get(): Returns the value of the specified key
items(): Returns a list containing a tuple for each key value pair
keys(): Returns a list containing the dictionary's keys
pop(): Removes the element with the specified key
popitem(): Removes the last inserted key-value pair
setdefault(): Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update(): Updates the dictionary with the specified key-value pairs
values(): Returns a list of all the values in the dictionary

### Sets
Sets are unordered collection of unique elements.
Set operations are shown below:
len(s): cardinality of sets
x in s: test x for membership in s
x not in s: test x for non-membership in s
s.issubset(t): (equivalent, s<=t), test whether every element insis int
s.issuperset(t): (equivalent, s>=t), test whether every element intis ins
s.intersection(t): (equivalent, s&t), new set with elements common tosandt
s.difference(t): (equivalent, s-t), new set with elements insbut not int
s.symmetric_difference(t): (equivalent, s^t), new set with elements in eithersortbut not both
s.copy(): new set with a shallow copy of s

### Numpy arrays
Numpy is now the standars library for scientific computing in Python.
The primary object in Numpy is the array
Numpy is high performance and provide tools to create and manipulate arrays.
* **Arrays**
Numpy arrays are obects
Essentially its a grid of values
All values have to be the same type
The array is indexed by a tuple of nonnegative integers
The number of dimensions is the rank of the array
the shape of an array is a tuple of integers giving the size of the array along each dimension.
