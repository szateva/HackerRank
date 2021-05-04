n = int(input("type how many sts are there? "))
matrix = []
for i in range(n):
    name = input()
    score = float(input())
    matrix.append([name, score])

lowest_score = matrix[0][1]

for row in range(len(matrix)):
    if matrix[row][1] < lowest_score:
        lowest_score = matrix[row][1]
to_delete = []
for row in range(len(matrix)):
    if matrix[row][1] == lowest_score:
        to_delete.append( 

second_lowest = matrix[0][1]
for row in range(len(matrix)):
    if matrix[row][1] < second_lowest:
        second_lowes = matrix[row][1]

names = []
for row in range(len(matrix)):
    if matrix[row][1] == second_lowest:
        names.append(matrix[row][0])
names.sort()
for n in names:
    print(n)