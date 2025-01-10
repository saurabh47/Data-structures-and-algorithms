### Word Subsets
### tags: string, counter

# Imagine you and your friends are planning to dine at a restaurant. Each friend has specific food preferences they want fulfilled. For example:
#
# Friend 1:
# - 2 Cheeseburgers
# - 3 Chocolate Croissants
# - 1 Margherita Pizza
#
# Friend 2:
#
# - 1 Grilled Chicken Sandwich
# - 2 Blueberry Muffins
#
# Each restaurant has a limit on the number of dishes they can prepare at any given time. For example:
#
# Restaurant A:
#
# Can prepare up to 5 Cheeseburgers, 6 Chocolate Croissants, 2 Margherita Pizzas, 3 Grilled Chicken Sandwiches, and 4 Blueberry Muffins.
#
# Restaurant B:
#
# Can prepare up to 3 Cheeseburgers, 4 Chocolate Croissants, 1 Margherita Pizza, 1 Grilled Chicken Sandwich, and 2 Blueberry Muffins.

# Your goal is to find the list of restaurants that can meet the full order of all your friends.
# Note each friend is served individually with everything they requested
#
# Solution: 
#
# Create an Imaginary Friend whose requirements are the maximum quantities of each dish requested by any of your friends. For example:
#
# Cheeseburgers: max(friendslist requesting Cheeseburgers)
# Chocolate Croissants: max(friendslist requesting Chocolate Croissants)
# Margherita Pizza: max(friendslist requesting Margherita Pizza)
#
# Now, Finally check with each restaurant if they can meet the Imaginary Friend's requirements
#

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        set_b = {}
        for word in words2:
            b = Counter(word)
            for k, v in b.items():
                if(k in set_b):
                    set_b[k] = max(set_b[k], v)
                else:
                    set_b[k] = v 
                
        result = []
        for i in range(len(words1)):
            isUniversal = True
            set_a = Counter(words1[i])
            for k , v in set_b.items():
                if(k not in set_a or set_b[k] > set_a[k]):
                    isUniversal = False
                    break
            if(isUniversal):
                result.append(words1[i])
        return result


