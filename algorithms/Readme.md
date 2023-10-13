## Algorithms

#### [Search Algorithms](search/)

- [Linear Search](search/linear.c)
- [Binary Search](search/binary.c)

#### [Sort Algorithms](sort/)

- [Bubble Sort](sort/bubble.c)
- [Selection Sort](sort/selection.c)

#### [Levenshtein Distance](levenshtein_distance.c)

#### [Moore's voting algorithm](moores-voting-algorithm.cpp)

### Advanced Algorithms (Problems from Algorithms: Design by Jon Kleinberg and Eva Tardos)

### [Stable Matching Problem](advanced/propose_reject.py)

The stable matching problem is a problem in combinatorial mathematics and computer science. It is a special case of the assignment problem. The problem is to find a stable matching between two equally sized sets of elements given an ordering of preferences for each element. A matching is a one-to-one mapping between the elements of the two sets. A matching is stable if no element prefers a partner in the matching to its current partner, and no element prefers its current partner to a partner in the matching. The stable matching problem is a special case of the stable marriage problem, which is a special case of the stable roommates problem.

### [Competition Scheduling Problem (Chapter 4, exercise 6 )](advanced/comp-scheduling.py)

Your friend is working as a camp counselor, and he is in charge of organizing activities for a set of junior-high-school-age
campers. One of his plans is the following mini-triathlon exercise: each contestant must swim 20 laps of a pool, then bike 10
miles, then run 3 miles. The plan is to send the contestants out in a staggered fashion, via the following rule: the contestants
must use the pool one at a time. In other words, first one contestant swims the 20 laps, gets out, and starts biking. As soon as
this first person is out of the pool, a second contestant begins swimming the 20 laps; as soon as he or she is out and starts
biking, a third contestant begins swimming . . . and so on.)

#Each contestant has a projected swimming time (the expected time it will take him or her to complete the 20 laps), a projected
biking time (the expected time it will take him or her to complete the 10 miles of bicycling), and a projected running time (the
time it will take him or her to complete the 3 miles of running). Your friend wants to decide on a schedule for the triathalon: an
order in which to sequence the starts of the contestants. Let’s say that the completion time of a schedule is the earliest time at
which all contestants will be finished with all three legs of the triathlon, assuming they each spend exactly their projected
swimming, biking, and running times on the three parts. (Again, note that participants can bike and run simultaneously, but at
most one person can be in the pool at any time.) What’s the best order for sending people out, if one wants the whole
competition to be over as early as possible? More precisely, give an efficient algorithm that produces a schedule whose
completion time is as small as possible.

### [Counting Inversions (Chapter 5, Exercise 2 )](advanced/inversions.py)

Counting Inversions and Significant Inversions in an array. An inversion is a pair of elements in an array that are out of order. We say a pair (a, b) is an inversion if a > b and a appears before b in the array.

For example, in the array [2, 4, 1, 3, 5], there are three inversions: (4, 1), (4, 3), and (2, 1).
The number of inversions in an array is the number of pairs of elements that are out of order.
In the array [2, 4, 1, 3, 5], there are three inversions: (4, 1), (4, 3), and (2, 1).
The number of inversions in an array is the number of pairs of elements that are out of order.

A significant inversion is an inversion where a > 2*b. For example, in the array [1, 20, 6, 4, 5],
there are five significant inversions: (20, 6), (20, 4), (20, 5), (6, 4), and (6, 5).
The number of significant inversions in an array is the number of pairs of elements that are out of order and where a > 2*b.

Time Complexity :- O(nlogn)

### [Genetic Algorithm](advanced/genetic.py)

Genetic Algorithm is a search-based optimization technique based on the principles of Genetics and Natural Selection. It is frequently used to find optimal or near-optimal solutions to difficult problems which otherwise would take a lifetime to solve.
Detailed explanation of this algotihm and the implementation can be found in this [blog post](https://maheshjamdade.medium.com/the-genetic-algorithm-and-the-travelling-salesman-problem-tsp-31dfa57f3b62)
