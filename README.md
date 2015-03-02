#data-structures

###This repository holds sample code for a number of data structures implemented with python.

*Feb 4th, 2015* - Add a Linked List structure in Python. Has classes for each node, as well as the structure itself.
                  The linked list is a data structure that utilizes how each node points to another as its mode for
                  identifying location. For example, instead of saying ti is the second item, we would say it is the one that
                  follows the first. Or, instead of saying the last item, we say it is the one that doesn't have anything
                  after it. This structure includes functionality for:

                      1. insert(value): Inserts the given value at the front of the list
                      2. pop(): Removes the front value from the list and returns that to the user
                      3. size(): Returns the size (number of nodes) in a list
                      4. search(value): Searches a list for a given value, if found, returns the node
                      5. remove(node): If the given node exists, removes it from the list.
                      6. display(): Displays the string formatted list as a tuple.
                      7. __repr__: Same as display, but can be called by just inputting the name of the list

                  Each of these functions has tests to ensure they are working as expected.


*Feb 5th, 2015* - Added a stack structure in Python. Has a class for an element of the stack, as well as the stack stucture itself.
                  The stack is a data structure that focuses on working off the top of the stack. That is
                  to say that if you are adding an element, it goes to the top, thus pushing an element that was
                  already there below it. This allows us to base our functionality off of a node NOT having a node
                  come before it, thus assuming that it is the top of the stack. Includes functionality for:

                      1. push(value): Adds the value at to top of the stack
                      2. pop(): Removes the top element from the stack and returns it.

                  Each of these functions has tests to ensure they are working as expected.


*Feb 6th, 2015* - Added the "Proper Parenthetics" Interview Challenge. We went about this with a loop
                  that goes over each item, adding 1 for "(", subtracting 1 for every ")" and passing
                  over any other character. Ours functions in a way that if it ever becomes negative, it
                  indicates a broken string, if it returns 0, it is balanced, and if it any number over 0,
                  it translates to there being too many "(" thus being an open string. This has the functionality to:

                      1. Return 1 if a string has unclosed parentheticals
                      2. Return 0 if a string is balanced - All parenthases closed
                      3. Return -1 if a string has closed parenthases that were not opened


*Feb 9th, 2015* - Added a queue data structure in Python. This structure functions similarly to a stack, though
                  instead of only focusing on the top of the data structure, we have to keep track of both front
                  and back, so as to add items to the back, and remove from the front. This includes functionality for:

                      1. enqueue(value): Ads the given value to the back of the queue
                      2. dequeue(): Removes the item in the front of the queue and returns its value
                      3. size(): returns the number of items in the current queue

                   Each of these functions has tests to ensure they are working as expected.


*Feb 10th, 2015* - Added a doubly linked list structure. This structure has functionality similar to that of
                   all of our previous data structures. Like the linked list, each node will point to the next,
                   but in this case, it points both forwards and back. Similar to the queue, it works in that we add
                   from one side and remove from the other, but in this case we can use both ends for removing and adding.
                   Has the functionality for:

                      1. insert(value): Adds a node with a given value to the head of the DLL
                      2. append(value): Adds a node with a given value to the tail of the DLL
                      3. pop(): Removes and returns the value at the head position
                      4. shift(): Removes and returns the value at the tail position
                      5. remove(value): Removes a given value from the DLL

                   Each of these functions has tests to ensure they are working as expected.


*Feb 11th, 2015* - Added a binary heap data strucutre. The binary heap functions similary to a tree that branches, though
                   the topmost value must be the highest,and descend down (meaning that every parent has 2 children that are
                   each lower than its parent). We needed to be able to make it a self sorting list such that if we added a
                   child that was higher than its parent it would swap places such that the structure remains intact. This
                   structure has the functionality for:

                     1. push(value): Adds a value to the bottom most left most portion of the stack
                     2. pop(): Removes the topmost value and the organizes the list the remain intact
                     3. __promote(): Starts with a child, and swaps it for the parent if it is larger
                     4. __demote(): Starts with a parent and swaps it for the child if it's lower


*Feb 11th, 2015* - Added a priority queue data structure. This structure takes in a value as well as another
                   value that you set as a "priority value". The queue will sort itself such that it retains
                   the order of the items, but it arranges it such that it groups together things of the same
                   priority. In addition to this, it keeps the highest priority group at the front and the
                   lowest at the back. This structure has functionality for:

                     1. insert(value, priority): Adds a value to the back of the queue, and then moves it ahead based on its priority
                     2. pop(): Removes the topmost value, which is to say the oldest item with the highest priority
                     3. peek(): Looks at the value at the front of the list which is the oldest item of highest priority


*Feb 16th, 2015* - Added a graph data structure. This structure creads nodes that have a value and a pointer to another node
                   Additionally, we can create an edge between any two nodes that will make a pointer from the first given
                   node to the second. Note, this does not make the second point back to the first. The data structure has
                   the functionality for:

                     1. add_node(value): Adds a node with the assigned value.
                     2. nodes(): Lists all nodes in the graph.
                     3. add_edge(val1, val2): Adds an edge (pointer) that goes from val1 to val2.
                     4. del_edge(val1, val2): Deletes an edge (pointer) that goes from val1 to val2.
                     5. edges(): Displays all edges as a tuple pair (A, B) where A points to B.
                     6. del_node(node): Removes the given node from the graph.
                     7. has_node(node): Returns True if the node is in the graph, and False if it is not.
                     8. neighbors(node): Returns a list of all nodes that the given node points to (has an edge towards).
                     9. adjacent(node1, node2): Returns True if node1 points to node2 and False otherwise. Raises appropriate
                        errors if neither or only one exists.

                    Each of these functions has tests to ensure they are working as expected.


*March 2nd, 2015* - Added weight for each of our edges in our graph. Not a ot of functionality yet, but this will change tomorrow
                    when we add traversal based on weight.



Collaborations:
Constantine Hatzis and Nick Becker


Resources:

1. Cris Ewing
2. Mark Ableidinger
3. stackoverflow.com
4. tutorialspoint.com/python
5. docs.python.org

[![Build Status](https://travis-ci.org/constanthatz/data-structures.svg?branch=master)](https://travis-ci.org/constanthatz/data-structures)
