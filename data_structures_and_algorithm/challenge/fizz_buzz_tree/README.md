# Code Challenge

Conduct “FizzBuzz” on a k-ary tree while traversing through it to create a new tree.

Set the values of each of the new nodes depending on the corresponding node value in the source tree.

## Specifications

Read all of these instructions carefully. Name things exactly as described.
Do all your work in a public repository called data-structures-and-algorithms, with a well-formatted, detailed top-level README.md.
Create a new branch in your repo called fizzbuzz-tree.
Your top-level readme should contain a “Table of Contents” navigation to all of your challenges and implementations so far. (Don’t forget to update it!)
This assignment should be completed within the challenges subdirectory of the repository.
On your branch, create…
C#: a new .NET Core class library project named FizzBuzzTree.
JavaScript: a folder named fizzBuzzTree which contains a file called fizz-buzz-tree.js
Python: a folder named fizz_buzz_tree which contains a file called fizz_buzz_tree.py
Java: a file called FizzBuzzTree.java in your utilities package
Include any language-specific configuration files required for this challenge to become an individual component, module, library, etc.
NOTE: You can find an example of this configuration for your course in your class lecture repository.

## Feature Tasks

Write a function called FizzBuzzTree which takes a k-ary tree as an argument.
Without utilizing any of the built-in methods available to your language, determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:
If the value is divisible by 3, replace the value with “Fizz”
If the value is divisible by 5, replace the value with “Buzz”
If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
If the value is not divisible by 3 or 5, simply turn the number into a String.
Return a new tree

## summary

loop throght all nodes in the binary tree to check if :
1- node capable to division by 3, replace the value with Fizz
2- node capable to division by 5, replace the value with Buzz
3- node capable to division by 3 and 5, replace the value with FizzBuzz
4- node not capable to division by 3 or 5 , return the value
![img]("https://drive.google.com/file/d/1MlqwxYHlxvFwuv_FmZeG4r587JTnctaR/view?usp=sharing")
