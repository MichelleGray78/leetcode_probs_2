# leetcode_probs_2
Solving leetcode problems
## EASY
### arithmetic_prog_from_seq:
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same. Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
### Happy_Number:
Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy. Return true if n is a happy number, and false if not. **Solved using Floyds cycle-finding algorithm**
### string_swap_string_equal: 
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false. 