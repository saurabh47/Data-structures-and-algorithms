#include <iostream>
#include <string>
#include <vector>
template <class T>
void print(std::vector<T> data)
{
    for (int i = 0; i < data.size(); i++)
    {
        std::cout << data[i] << " ";
    }
    std::cout << "\n";
}

std::vector<int> circularArrayRotation(int rotation, std::vector<int> array)
{
    std::vector<int> vectorAfterRotation(array.size());
    int positionShift = rotation % array.size();
    for (int i = 0; i < array.size(); i++)
    {
        int index = (i + array.size() - positionShift) % array.size();
        vectorAfterRotation[i] = array[index];
    }
    // std::cout << "position shift by:" << positionShift << std::endl;
    return vectorAfterRotation;
}

int main()
{
    // int array[] = {1, 2, 3, 4, 5};
    int n;
    int input;
    int rotationCount; //= 5;
    std::vector<int> dArray;
    // dArray.insert(dArray.end(), {1, 2, 3, 4});
    // query.insert(query.end(), {0, 1, 2});
    std::cout << "enter size of vector:";
    std::cin >> n;
    std::cout << "enter elements into vector" << std::endl;
    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        dArray.push_back(input);
    }
    std::cout << "Generated int array=";
    print(dArray);
    std::cout << "enter number of rotations to perform:";
    std::cin >> rotationCount;
    std::cout << "after " << rotationCount << " rotations" << std::endl;
    std::vector<int> result = circularArrayRotation(rotationCount, dArray);
    std::cout << "vector after rotation=";
    print(result);
    return 0;
}