def create_matrix(size):
    matrix = (('a' + str(i + 1) + str(j + 1) for j in range(size)) for i in range(size))
    return matrix

def det(matrix):
    if len(matrix) == 2:
        return (matrix[0][0] + ' * ' + matrix[1][1], ' - ' + matrix[1][0] + ' * ' + matrix[0][1])
    result = tuple()
    for i in range(len(matrix)):
        a = matrix[0][i]
        new_matrix = ((matrix[y][z] for z in range(len(matrix)) if z != i) for y in range(1, len(matrix)))
        result += (' - ' if i % 2 == 1 else ' + ' + a + ' * ' + x for x in det(new_matrix))
    return result

print(*det(create_matrix(3)), sep='')