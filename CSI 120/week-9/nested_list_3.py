#create a 2 d matrix
matrix =[
    [1, 2, 3,4,5,6],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[1][2]=10
#use two loops to read and display each item
print("Reading and displaying each item")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"Element at [{i}][{j}] is  {matrix[i][j]}")
        