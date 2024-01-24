def transpose(A, B):

	for i in range(N):
		for j in range(M):
			B[i][j] = A[j][i]

M = int(input("Enter the number of rows:"))
N = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")

for i in range(M):		 
	a =[]
	for j in range(N):	
		a.append(int(input()))
	matrix.append(a)
	
B = [[0 for x in range(M)] for y in range(N)]

print("Original matrix is")
for i in range(M):
	for j in range(N):
		print(matrix[i][j], end = " ")
	print()
	
transpose(matrix, B)
print("Transpose of matrix is")
for i in range(N):
	for j in range(M):
		print(B[i][j], " ", end='')
	print()	
