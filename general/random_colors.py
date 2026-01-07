"""
You’re given a bag with a number of balls with different colors. There can be multiple balls with the same color. 
Write a program to pick a color at random. 
The probability of picking a color should be proportional to its ball count.  

Input: [‘blue’, ‘blue’, ‘red’, ‘red’, ‘green’]
Expected output: ‘blue’ in 40% cases, ‘red’ in 40% cases and ‘green’ in 20% cases
"""

from collections import Counter
import random

def getRandomColor(colors):
    freq = Counter(colors)
    #{'blue': 2,'red':2, 'green': 1 }
    count = len(colors)
    for key, value in freq.items():
        freq[key] = value/count
    cum = []
    prob = 0
    for key, val in freq.items():
        prob += val
        cum.append([prob, key])
    # [[0.4, 'blue'], [0.8, 'red'], [1.0, 'green']]
    
    r = random.random()
    for prob, color in cum:
        if(r < prob):
            return color

print(getRandomColor(['blue', 'blue', 'red', 'red', 'green']))