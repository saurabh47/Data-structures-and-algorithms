if __name__ == "__main__":
  # input from the user
  inputs = [int(part) for part in input("Enter no of nodes (separated by comma):").split(',')]
  length = len(inputs)
  matrix = [[0 for x in range(length)] for y in range(length)]
  for row in range(length):
    for col in range(length):
        if row == col:
            matrix[row][col] = 0
        else:
            connected = input("Is {} connected to {}? (y/n)".format(inputs[row], inputs[col]))
            matrix[row][col] = 1 if connected == "y" else 0
  
  # print the matrix
  for row in range(length):
    for col in range(length):
        print(matrix[row][col], end=" ")
    print()