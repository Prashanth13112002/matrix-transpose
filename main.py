class solution :
    def matrix_transpose(self,a):
        row=len(a)
        col=len(a[0])
        b=[[0 for _ in range(row)]for _ in range (col)]
        for i in range (row):
            for j in range (col):
                b[j][i]=a[i][j]

        return b
a1=solution()
row =int(input())
arr=[]
for i in range (row):
    col=list(map(int,input().split()))
    arr.append(col)
print(a1.matrix_transpose(arr))
