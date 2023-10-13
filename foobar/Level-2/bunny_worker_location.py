def solution(x, y):
    row = 1
    col = 0
    column_count = x + y + 1
    rows = []
    row_inc = 1
    row_result = 0

# Traverse first row until
    for i in range(1, column_count):
        row_result += row_inc
        row_inc+=1
        col += 1
        print("result={0} at ({1},{2})".format(row_result, row, col))

# Traverse up along the column until target row is reached
    while(row != y):
            col -= 1
            row += 1
            row_result -=1
            print("result={0} at ({1},{2})".format(row_result, row, col))

    row_inc -=1

# Traverse back along the row until target column is reached
    while(col != x):
        col -= 1
        row_result -= row_inc
        row_inc -=1
        if(row == y and col == x):
            break;

    return row_result;

print(solution(6,4))