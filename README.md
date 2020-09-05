
# Trees

- the binary tree is a tree dtat structure each node has most two children.
which referes to as the left and the right child.
- from the root to the leaf(the last child in the tree has not any child), it's called the depth.
- from the leaf to the root(the first node in the tree has not any parent), it's called the height.


## Challenge

implement the binary tree using classes and Data strcuture.
like that:

                5
               /  \
              3    9
             / \    \
            1   4    10

## Approach & Efficiency

the worst case scenario for space, access, search, insertion, and deletion, it's O(n).

## API

pre_order method : present the the tree :this is the first mode of depth of tree,fill the tree starting from :
         ROOT -->> LEFT -->> RIGHT.
         
in_order method : present the the tree :this is the second mode of depth of tree,fill the tree starting from :
         LEFT -->> ROOT -->> RIGHT.
     
post_order method : present the the tree :this is the third mode of depth of tree,fill the tree starting from :
         LEFT -->>  RIGHT -->> ROOT.

