# Description: Counting Inversions and Significant Inversions in an array.
# An inversion is a pair of elements in an array that are out of order. We say a pair (a, b) is an inversion if a > b and a appears before b in the array.
# For example, in the array [2, 4, 1, 3, 5], there are three inversions: (4, 1), (4, 3), and (2, 1).
# The number of inversions in an array is the number of pairs of elements that are out of order.
# In the array [2, 4, 1, 3, 5], there are three inversions: (4, 1), (4, 3), and (2, 1).
# The number of inversions in an array is the number of pairs of elements that are out of order.
#
# A significant inversion is an inversion where a > 2*b. For example, in the array [1, 20, 6, 4, 5],
# there are five significant inversions: (20, 6), (20, 4), (20, 5), (6, 4), and (6, 5).
# The number of significant inversions in an array is the number of pairs of elements that are out of order and where a > 2*b.
#
class Inversions():
  def __init__(self , array):
    self.array = array
    self.length = len(array)

  def countInversions(self):
    length = len(self.array)
    start = 0
    end = length - 1
    mid = start + (end - start) // 2
    inversions, sorted_array = self.sortAndCount(self.array, start, end)
    print("Inversions = ", inversions[0], "Significant Inversions = ", inversions[1])

  def sortAndCount(self, arr, s, e):
    size = e - s + 1
    count = 0
    sigCount = 0
    if(size == 1):
        return [0,0], [arr[s]]
    else:
      start = s
      end = e
      mid = start + (end - start) // 2
      inv1 , sortedLeftHalf = self.sortAndCount(arr, start, mid)
      inv2 , sortedRightHalf = self.sortAndCount(arr, mid + 1, end)
      inv3 , sorted_array = self.mergeAndCountInversions(sortedLeftHalf,sortedRightHalf)
      count = inv1[0] + inv2[0] + inv3[0]
      sigCount = inv1[1] + inv2[1] + inv3[1]
    return [count, sigCount], sorted_array

  def mergeAndCountInversions(self, array1, array2):
    len1 = len(array1)
    len2 = len(array2)
    i = 0
    j = 0
    sorted_array = []
    count = 0
    sigCount = 0
    while(i < len1 and j < len2):
      if(array1[i] > array2[j]):
        count += (len1 - i)
        if(array1[i] > 2*array2[j]):
          sigCount += 1
        sorted_array.append(array2[j])
        j+=1
      else:
        sorted_array.append(array1[i])
        i+=1
    if(i < len1):
        while(i < len1):
          sorted_array.append(array1[i])
          i+=1
    if(j < len2):
      while(j < len2):
          sorted_array.append(array2[j])
          j+=1
    return [count, sigCount], sorted_array

if __name__ == '__main__':
  print("enter elements of array:")
  array = [int(x) for x in input().split()]
  # inversions = Inversions([5, 4, 3, 2, 1]) # 10
  # inversions = Inversions([2, 4, 1, 3, 5]) # 3
  # inversions = Inversions([1, 20, 6, 4, 5]) # 5
  inversions = Inversions(array)
  inversions.countInversions()

# enter elements of array:
# 4 1 5 2 3 7 6 2
# Inversions =  11 Significant Inversions =  3