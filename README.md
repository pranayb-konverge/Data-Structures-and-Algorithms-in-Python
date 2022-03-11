# Data-Structures-and-Algorithms-in-Python

## Youtube video
<a href="https://www.youtube.com/watch?feature=player_embedded&v=pkYVOmU3MgA
" target="_blank"><img src="http://img.youtube.com/vi/pkYVOmU3MgA/0.jpg" 
alt="Python for everyone - full course" width="240" height="180" border="10" /></a>

## The Method to solved a problem
Upon reading the problem, you may get some ideas on how to solve it and your first instinct might be to start writing code. This is not the optimal strategy and you may end up spending a longer time trying to solve the problem due to coding errors, or may not be able to solve it at all.

### Here's a systematic strategy we'll apply for solving problems:

1. State the problem clearly. Identify the input & output formats.
2. Come up with some example inputs & outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using example inputs. Fix bugs, if any.
5. Analyze the algorithm's complexity and identify inefficiencies, if any.
6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
7. "Applying the right technique" is where the knowledge of common data structures and algorithms comes in handy.

## Generic Binary Search
Here is the general strategy behind binary search, which is applicable to a variety of problems:

1. Come up with a condition to determine whether the answer lies before, after or at a given position
2. Retrieve the midpoint and the middle element of the list.
3. If it is the answer, return the middle position as the answer.
4. If answer lies before it, repeat the search with the first half of the list
5. If the answer lies after it, repeat the search with the second half of the list.

