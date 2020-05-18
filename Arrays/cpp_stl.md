Vector
Vector in C++ STL is a class that represents a dynamic array. The advantages of vector over normal arrays are,
	No need to pass size, ability to resize itself automatically
	Vectors have many in-built functions for erasing an element, inserting an element etc.
	Vectors support dynamic sizes, we do not have to initially specify the size of a vector. We can also resize a vector.
	Placed in contiguous storage,accessed and traversed using iterators
	Inserting at the end takes differential time, as sometimes there may be a need of extending the array. 
	Removing the last element takes only constant time because no resizing happens. 
	Inserting and erasing at the beginning or in the middle is linear in time.

To use the Vector class, include the below header file in your program:
#include< vector >

Declaring Vector:
vector< Type_of_element > vector_name;

Here, Type_of_element can be any valid C++ data type,
or can be any other container also like Pair, List etc.

Some important and commonly used functions of Vector class are:
---------------------------------------------------------------
begin() – Returns an iterator pointing to the first element in the vector.
end() – Returns an iterator pointing to the theoretical element that follows the last element in the vector.
size() – Returns the number of elements in the vector.
capacity() – Returns the size of the storage space currently allocated to the vector expressed as number of elements.
empty() – Returns whether the container is empty.
push_back() – It push the elements into a vector from the back.
pop_back() – It is used to pop or remove elements from a vector from the back.
insert() – It inserts new elements before the element at the specified position.
erase() – It is used to remove elements from a container from the specified position or range.
swap() – It is used to swap the contents of one vector with another vector of same type and size.
clear() – It is used to remove all the elements of the vector container.
emplace() – It extends the container by inserting new element at position.
emplace_back() – It is used to insert a new element into the vector container, the new element is added to the end of the vector.

## List
Lists are sequence containers that allow non-contiguous memory allocation. List in C++ STL implements a doubly linked list and not arrays. As compared to vector, list has slow traversal, but once a position has been found, insertion and deletion are quick. Normally, when we say a List, we talk about doubly linked lists. For implementing a singly linked list, we can use forward_list class in C++ STL.

To use the List class, include the below header file in your program:
#include< list >

Declaring List:
list< Type_of_element > list_name;

Here, Type_of_element can be any valid C++ data type,
or can be any other container also like Pair, List etc.


Some important and commonly used functions of List are:
---------------------------------------------------------
front() – Returns the value of the first element in the list.
back() – Returns the value of the last element in the list.
push_front(g) – Adds a new element ‘g’ at the beginning of the list.
push_back(g) – Adds a new element ‘g’ at the end of the list.
pop_front() – Removes the first element of the list, and reduces the size of the list by 1.
pop_back() – Removes the last element of the list, and reduces the size of the list by 1.
begin() and end() – begin() function returns an iterator pointing to the first element of the list.
empty() – Returns whether the list is empty(1) or not(0).
insert() – Inserts new elements in the list before the element at a specified position.
reverse() – Reverses the list.
size() – Returns the number of elements in the list.
sort() – Sorts the list in increasing order.

