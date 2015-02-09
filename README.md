#data-structures

###This repository holds sample code for a number of data structures implemented with python.

*Feb 4th, 2015* - Added a Linked List structure in Python. Has classes for each node, as well as the structure itself.
                  The linked list is a data structure that utilizes how each node points to another as its mode for
                  identifying location. For example, instead of saying ti is the second item, we would say it is the one that
                  follows the first. Or, instead of saying the last item, we say it is the one that doesn't have anything
                  after it. This structure includes functionality for:
                      <ul>
                      <li>insert(value): Inserts the given value at the front of the list</li>
                      <li>pop(): Removes the front value from the list and returns that to the user</li>
                      <li>size(): Returns the size (number of nodes) in a list</li>
                      <li>search(value): Searches a list for a given value, if found, returns the node</li>
                      <li>remove(node): If the given node exists, removes it from the list.</li>
                      <li>display(): Displays the string formatted list as a tuple.</li>
                      <li>__repr__: Same as display, but can be called by just inputting the name of the list</li>
                      </ul>
                  <p>Each of these functions has tests to ensure they are working as expected.</p>
*Feb 5th, 2015* - Added a stack structure in Python. Has a class for an element of the stack, as well as the stack stucture itself.
                  The stack is a data structure that focuses on working off the top of the stack. That is
                  to say that if you are adding an element, it goes to the top, thus pushing an element that was
                  already there below it. This allows us to base our functionality off of a node NOT having a node
                  come before it, thus assuming that it is the top of the stack. Includes functionality for:
                      <ul>
                      <li>push(value): Adds the value at to top of the stack</li>
                      <li>pop(): Removes the top element from the stack and returns it.</li>
                      </ul>
                  <p>Each of these functions has tests to ensure they are working as expected.</p>
*Feb 6th, 2015* - Added the "Proper Parenthetics" Interview Challenge. We went about this with a loop
                  that goes over each item, adding 1 for "(", subtracting 1 for every ")" and passing
                  over any other character. Ours functions in a way that if it ever becomes negative, it
                  indicates a broken string, if it returns 0, it is balanced, and if it any number over 0,
                  it translates to there being too many "(" thus being an open string. This has the functionality to:
                      <ul>
                      <li>Return 1 if a string has unclosed parentheticals</li>
                      <li>Return 0 if a string is balanced - All parenthases closed</li>
                      <li>Return -1 if a string has closed parenthases that were not opened</li>
                      </ul>
*Feb 9th, 2015* - Added a queue data structure in Python. This structure functions similarly to a stack, though
                  instead of only focusing on the top of the data structure, we have to keep track of both front
                  and back, so as to add items to the back, and remove from the front. This includes functionality for:
                      <ul>
                      <li>enqueue(value): Ads the given value to the back of the queue</li>
                      <li>dequeue(): Removes the item in the front of the queue and returns its value</li>
                      <li>size(): returns the number of items in the current queue</li>
                      </ul>


Collaborations:
Constantine Hatzis and Nick Becker


Resources:
<ul>
<li>Cris Ewing</li>
<li>Mark Ableidinger</li>
<li>stackoverflow.com</li>
<li>tutorialspoint.com/python</li>
<li>docs.python.org</li>
</ul>
