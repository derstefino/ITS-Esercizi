def sum_primary_diagonal(matrix:list[list]) -> int:
    
    sum=0

    for row in matrix:
        
        sum += row[matrix.index[row]]

    return sum






def sum_secondary_diagonal(matrix:list[list]) -> int:

    sum=0
    index = -1

    for row in matrix:

        sum+=row[index]
        index -= 1
    
    return sum


