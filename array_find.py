def clockwise(matrix):
    up = 0
    down = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    size = (len(matrix)) * (len(matrix[0]))
    list_clockwise = []
    while len(list_clockwise) < size:
        list_clockwise += matrix[up][left:right + 1]
        up += 1

        list_clockwise += [col[right] for col in matrix[up:down + 1]]
        right -= 1

        if down >= up:
            t = matrix[down][left:right + 1]
            t.reverse()
            list_clockwise += t
            down -= 1

        if left <= right:
            t = [col[left] for col in matrix[up:down + 1]]
            t.reverse()
            list_clockwise += t
            left += 1

    return list_clockwise


print(clockwise([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
print(clockwise([[1, 2, 3, 4], [5, 6, 7, 8]]))
print(clockwise([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]))
print(clockwise([[1, 2, 3, 4]]))
print(clockwise([[1], [2], [3], [4]]))
print(clockwise([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))


