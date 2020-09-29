# Challenge Summary

Binary Trees can be in many shapes but are most useful when balanced. Walking Binary Trees in depth-first order is done the same as walking Binary Search Trees which can be done in pre-order, in-order or post-order. Binary Trees, like Binary Search Trees, can also be walked in depth-first order.

## Challenge Description

Write a function named tree_intersection which takes two trees and returns a set with the intersection of values in both trees. Write tests for the function.

## Approach & Efficiency

The challenge is broken into two functions: tree_intersection and walk. The tree_intersection is the main function which uses the walk function as a helper for walking a Binary Tree recursively. At each recursive step of the walk a value is either added to a union set of the two trees in tree_intersection or added to an intersection set of the two trees. Time and space complexity of tree_intersection is O(1). Time and space complexity of walk is O(N) where N is the number of nodes in a tree.

## Solution
<!-- Embedded whiteboard image -->