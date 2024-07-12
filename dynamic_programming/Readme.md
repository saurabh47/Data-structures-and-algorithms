### Dynamic Programming

Dynamic Programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions. The next time the same subproblem occurs, instead of recomputing its solution, one simply looks up the previously computed solution, thereby saving computation time.

Steps to solve DP problems:

1. Define the objective function f(n): (What is input and output?)
2. Identify the base cases
3. Write down a recurrence relation for the optimized objective function by idenifying the patterns in the base cases
4. Order of Computation: Top Down or Bottom Up
5. Location of the answer: Return f(n)

There are two types of Dynamic Programming problems

1. Combinatorial Problems: These problems are solved by generating all possible combinations of the solution and then selecting the best one. For example, the knapsack problem.
2. Optimization Problems: These problems are solved by finding the best solution from all possible solutions. For example, the Fibonacci sequence.

#### Dynamic Programming Problems

1. [Sum of N numbers](../dynamic_programming/sum_n.py)
2. [Fibonacci Series](../leetcode/problem_509.py)
3. [Climbing Staircase](../leetcode/problem_70.py)
4. [Min Cost to climb stairs](../leetcode/problem_746.py)
5. [Counting bits](../leetcode/problem_338.py)

### Dynamic Programming Problems by Patterns

source: github: educative-io-contents
/Grokking Dynamic Programming Patterns for Coding Interviews.md

#### Pattern 1: 0/1 Knapsack

1. 0/1 Knapsack Problem
2. Equal Subset Sum Partition
3. Subset Sum
4. Minimum Subset Sum Difference
5. Count of subset sum
6. Target Sum (Leetcode)

Pattern 2: Unbounded Knapsack

1. Unbounded Knapsack
2. Rod Cutting
3. Coin Change
4. Minimum Coin Change
5. Maximum Ribbon Cut

#### Pattern 3: Fibonacci Numbers

1. Fibonacci Number
2. [Climbing Staircase](../leetcode/problem_70.py)
3. Number divisors - // TODO
4. Minimum jumps to reach end
5. Minimum jumps with fee - // TODO
6. House Thief

#### Pattern 4: Palindromic Subsequence

1. Longest Pallindromic Subsequence
2. Longest Pallindromic Substring
3. Count of Pallindromic Substrings
4. Minimum deletions to make a string pallindrome
5. Pallindromic Partitioning

#### Pattern 5: Longest Common Substring

1. Longest Common Substring
2. Longest Common Subsequence
3. Minimum Deletions and Insertions to Transform a String into another
4. Longest Increasing Subsequence
5. Maximum Sum Increasing Subsequence
6. Shortest Common Supersequence
7. Minimum deletions to make sequence sorted
8. Longest repeating subsequence
9. Subsequence Pattern Matching - // TODO
10. Longest Bitonic Subsequence
11. Longest Alternating Subsequence
12. Edit Distance
13. String Interleaving
    ​
