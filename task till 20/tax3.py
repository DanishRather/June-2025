def spiral_order(matrix):
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Left to Right (Top row)
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Top to Bottom (Right column)
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Right to Left (Bottom row)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Bottom to Top (Left column)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result




matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15,16]
]


print(spiral_order(matrix))
# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
