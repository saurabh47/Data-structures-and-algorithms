/*
 * File: between_sets.cpp
 * Project: None
 * File Created: Friday, 16th April 2021 5:34:47 pm
 * Author: Mahesh Jamdade
 * -----
 * Last Modified: Friday, 16th April 2021 5:36:47 pm
 * Modified By: Mahesh Jamdade
 * -----
 * Copyright 2021 - 2021 None
 */
#include <iostream>
#include <vector>

// prints the content of input vector
void print(std::vector<int> input)
{
  for (int i = 0; i < input.size(); i++)
  {
    std::cout << input[i] << " ";
  }
  std::cout << std::endl;
}

void print(int x)
{
  std::cout << x << std::endl;
}

void print(std::string x)
{
  std::cout << x << std::endl;
}

// gets in array of ints and returns
/// a vector
std::vector<int> input(int count)
{
  std::vector<int> v;
  int inputValue;
  for (int i = 0; i < count; i++)
  {
    std::cin >> inputValue;
    v.push_back(inputValue);
  }
  return v;
}

/// returns maximum from the vector
int max(std::vector<int> array)
{
  int size = array.size();
  if (size < 1)
  {
    return -1;
  }
  int max = array[0];
  for (int i = 0; i < size; i++)
  {
    if (array[i] > max)
    {
      max = array[i];
    }
  }
  return max;
}

/// gcd of two numbers
int gcd(int a, int b)
{
  if (b == 0)
    return a;
  return gcd(b, a % b);
}

/// gcd of array computed iteratively
/// as gcd(<recent gcd result>,arr[i])
int gcdOfArray(std::vector<int> array)
{
  int result = 0;
  int size = array.size();
  for (int i = 0; i < size; i++)
  {
    result = gcd(result, array[i]);
  }
  return result;
}

int lcmofArray(std::vector<int> inputArray)
{
  int result = inputArray[0];
  int size = inputArray.size();
  for (int i = 1; i < size; i++)
    result = ((inputArray[i] * result) / gcd(result, inputArray[i]));
  return result;
}

/// iterates vector and checks if target is isDivisible
/// by every number of the array
bool checkIfTargetDivides(std::vector<int> array, int target)
{
  int size = array.size();
  bool isDivisible = true;
  for (int i = 0; i < size; i++)
  {
    if (array[i] % target != 0)
    {
      isDivisible = false;
      break;
    }
  }
  return isDivisible;
}

int getInBetweenTwoSets(std::vector<int> arr1, std::vector<int> arr2)
{
  int count = 0;
  int lcmOfArray1 = lcmofArray(arr1);
  int target = lcmOfArray1;
  int maxArray2 = max(arr2);
  while (target <= maxArray2)
  {
    if (checkIfTargetDivides(arr2, target))
    {
      count += 1;
    }
    target += lcmOfArray1;
  }
  return count;
}

int main()
{
  int n1;
  int n2;
  printf("Enter size of first array:");
  std::cin >> n1;
  printf("Enter size of 2nd array:");
  std::cin >> n2;
  std::vector<int> array1 = input(n1);
  std::vector<int> array2 = input(n2);
  std::cout << "array1=";
  print(array1);
  std::cout << "array2=";
  print(array2);
  int count = getInBetweenTwoSets(array1, array2);
  std::cout << "In Between sets=" << count << std::endl;
  return 0;
}

/************************************ output ****************************
 * Enter size of first array:10
 * Enter size of 2nd array:10
 * 100 99 98 97 96 95 94 93 92 91
 * 1 2 3 4 5 6 7 8 9 10
 * array1=100 99 98 97 96 95 94 93 92 91 
 * array2=1 2 3 4 5 6 7 8 9 10 
 * In Between sets=0
 * 
 * ******************************** output 2 ****************************
 * 
 * Enter size of first array:2
 * Enter size of 2nd array:3
 * 2 4
 * 16 32 96
 * array1=2 4
 * array2=16 32 96
 * In Between sets=3
 ************************************************************************/