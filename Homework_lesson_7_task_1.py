class Matrix:
    def __init__(self, matrix_1):
        self.matrix_1 = matrix_1

    def __str__(self):
        r = [str(' '.join([str(a) for a in k])) for k in self.matrix_1]
        r = '\n'.join(r)
        return f"{r}"

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.matrix_1)):
            new_matrix.insert(i, [])
            for el in range(len(self.matrix_1[i])):
                new_matrix[i].append(self.matrix_1[i][el] + other.matrix_1[i][el])
        return Matrix(new_matrix)


first = Matrix([[17, 37, 77], [22, 33, 44], [45, 78, 88]])
second = Matrix([[18, 49, 65], [1, 2, 3], [66, 98, 23]])
print(f"Matrix 1:\n{first}\nMatrix 2:\n{second}")
print(f"Sum matrix 1 and 2:\n{first + second}")
