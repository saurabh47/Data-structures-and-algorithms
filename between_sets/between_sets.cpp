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
void
print (std::vector < int >input)
{
  for (int i = 0; i < input.size (); i++)
    {
      std::cout << input[i] << " ";
    }
  std::cout << std::endl;
}

void
print (int x)
{
  std::cout << x << std::endl;
}

void
print (std::string x)
{
  std::cout << x << std::endl;
}

// gets in array of ints and returns 
/// a vector
std::vector < int >
input (int count)
{
  std::vector < int >v;
  int inputValue;
  for (int i = 0; i < count; i++)
    {
      std::cin >> inputValue;
      v.push_back (inputValue);
    }
  return v;
}

/// returns minimum from the vector
int min (std::vector < int >array)
{
  int size = array.size();
  if (size < 1)
    {
      return -1;
    }
  int min = array[0];
  for (int i = 0; i < size; i++)
    {
      if (array[i] < min)
	{
	  min = array[i];
	}
    }
  return min;
}

/// returns maximum from the vector
int max (std::vector < int >array)
{
  int size = array.size ();
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

/// iterates vector and checks if target is isDivisible
/// by every number of the array
bool checkIfTargetDivisible (std::vector <int>array, int target)
{
  int size = array.size ();
  bool isDivisible = true;
  for (int i = 0; i < size; i++)
    {
      if (target % array[i] != 0)
	 {
	      isDivisible = false;
	      break;
 	 }
  }
  return isDivisible;
}

/// iterates vector and checks if target is isDivisible
/// by every number of the array
bool checkIfTargetDivides (std::vector <int>array, int target)
{
  int size = array.size ();
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

int lcm (std::vector < int >inputArray, int minLCM)
{
  while (1)
    {
      if (checkIfTargetDivisible (inputArray, minLCM))
	{
	  return minLCM;
	}
      minLCM++;
    }
  return 0;
}


int getInBetweenTwoSets (std::vector <int>arr1, std::vector <int>arr2)
{
  int count = 0;
  int lcmOfArray1 = lcm (arr1, max(arr1));
  std::cout << "lcm of array1=" << lcmOfArray1 << std::endl;
  int target = lcmOfArray1;
  int maxArray2 = max(arr2);
//   int minArray2 = min(arr2);
  while(target<=maxArray2){
      if(checkIfTargetDivides(arr2, target)){
         std::cout<<"found="<<target<<std::endl;
         count+=1;
      }
       target+=lcmOfArray1;
  }
  return count;
}

int main ()
{
  int n1;
  int n2;
  printf ("Enter size of first array:");
  std::cin >> n1;
  printf ("Enter size of 2nd array:");
  std::cin >> n2;
  std::vector < int >array1 = input (n1);
  std::vector < int >array2 = input (n2);
  int count = getInBetweenTwoSets (array1, array2);
  std::cout << "In Between sets=" << count << std::endl;
  return 0;
}
