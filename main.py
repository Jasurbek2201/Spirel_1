def fill_spiral_clockwise(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, left = 0, 0
    bottom, right = n - 1, n - 1

    while top <= bottom and left <= right:
        # Tepadan chapdan o'ngga
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # O'ngdan yuqoridan pastga
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Pastdan o'ngdan chapga
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Chapdan pastdan yuqoriga
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# 7x7 matritsa
n = 7
matrix = fill_spiral_clockwise(n)
print_matrix(matrix)
