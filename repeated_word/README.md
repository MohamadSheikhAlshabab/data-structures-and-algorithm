# Challenge Summary

We want to return the first word repeated in a paragraph.

## Challenge Description

We have existing solution for this problem please refer Find the first repeated word in a string link. We can solve this problem quickly in python using Dictionary data structure. Approach is simple,

First split given string separated by space.
Now convert list of words into dictionary using collections.Counter(iterator) method. Dictionary contains words as key and it’s frequency as value.
Now traverse list of words again and check which first word has frequency greater than 1.

## Approach & Efficiency

- Time complexity: O(n)
- Space complexity: O(1)

## Solution
<!-- Embedded whiteboard image -->