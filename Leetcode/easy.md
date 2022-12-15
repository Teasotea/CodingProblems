Maximum Nesting Depth of the Parentheses 

Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

My solution:

```
def count_par(string):
    max=0
    counter = 0
    
    for p in string:
        If p is in open_par:
            counter = counter +1
        else:
            counter = counter - 1

        If counter > max:
            max = counter
    return max
```
Complexity: O(n) - both time and space
