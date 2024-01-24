MAX = 100

def isSparse(matrix,M, N) :	
	counter = 0
	for i in range(0,M) :
		for j in range(0,N) :
			if (matrix[i][j] == 0) :
				counter = counter + 1

	return (counter >
			((M * N) // 2))

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


if (isSparse(matrix,M, N)) :
	print("Yes the entered matrix is a sparse matrix")
else :
	print("Not a sparse matrix")