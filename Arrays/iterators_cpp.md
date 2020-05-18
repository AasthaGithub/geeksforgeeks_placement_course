## Iterating list:
---------------
void showlist(list <int> g) 

{
 
    list <int> :: iterator it;
 
    for(it = g.begin(); it != g.end(); ++it)
 
       cout << '\t' << *it;
 
    	cout << '\n'; 

} 
-----------------
// C++ code to demonstrate the working of
// iterator, begin() and end()

#include<iostream>
#include<iterator> // for iterators
#include<vector> // for vectors


using namespace std;


int main()
{

    vector<int> ar = { 1, 2, 3, 4, 5 };

    
    // Declaring iterator to a vector

    vector<int>::iterator ptr;

    
    // Displaying vector elements using begin() and end()

    cout << "The vector elements are : ";

    for (ptr = ar.begin(); ptr < ar.end(); ptr++)

        cout << *ptr << " ";

    
    return 0;
    
}
-----------------
vector<int> ar = { 1, 2, 3, 4, 5 };

    
    // Declaring iterator to a vector

    vector<int>::iterator ptr = ar.begin();

    
    // Using advance() to increment iterator position
 
   	// points to 4

    advance(ptr, 3);
    
    
	// Displaying iterator position

    cout << "The position of iterator after advancing is : ";

    cout << *ptr << " ";
-----------------

next() :- This function returns the new iterator that the iterator would point after advancing the positions mentioned in its arguments.
prev() :- This function returns the new iterator that the iterator would point after decrementing the positions mentioned in its arguments.

vector<int>::iterator ptr = ar.begin();

vector<int>::iterator ftr = ar.end();

   
   
    // Using next() to return new iterator

    // points to 4
    
auto it = next(ptr, 3);

    
    // Using prev() to return new iterator

    // points to 3
    
auto it1 = prev(ftr, 3);
-----------------------------
inserter() :- This function is used to insert the elements at any position in the container. It accepts 2 arguments, the container and iterator to position where the elements have to be inserted.

vector<int>::iterator ptr = ar.begin();

   
    // Using advance to set position

    advance(ptr, 3);

    
    // copying 1 vector elements in other using inserter()

    	// inserts ar1 after 3rd position in ar


    copy(ar1.begin(), ar1.end(), inserter(ar,ptr));
-------------------------------
