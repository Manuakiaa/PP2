A=int(input())
B=[]
B = list(map(int, input().split()))
C=[]
for i in range(1,A+1):
    C.append(-1)
    
for i in range(1,A):
    for j in range(0,i+1):
        if B[i] > B[j]:
            C[i] = B[j]
          
print(*C)


#5
# 2 1 5 8 3
#-1 -1 1 5 1 