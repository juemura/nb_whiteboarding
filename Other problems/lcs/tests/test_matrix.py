matrix = [[(0, '') if i==0 or j==0 else None for j in range(5)] for i in range(4)]

print('\n'.join([''.join(['{:10}'.format(str(item)) for item in row]) for row in matrix]))

print(matrix[0][0][0])
print(matrix[0][0][1])