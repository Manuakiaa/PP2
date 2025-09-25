# A
# a = int(input())  #6
# Llist = list(map(int, input().split()))   #1 2 90 32 2 2
# b = int (input())  #10
# A = Llist[0]         
# for i in range(0, a):
#     if abs(b - Llist[i]) < abs(b - A):
#         A = Llist[i]
# B = None
# for i in range(a-1, -1, -1):
#     if Llist[i] == A:
#         B = i
# print(B)



# B
# a, b = map(int, input().split())  #5 2
# Llist = list(map(str, input().split()))   #the show must go on
# Answer = []
# for i in range(b, a):
#     Answer.append(Llist[i]) 
# print(*(Answer + Llist [:b]))  #must go on the show 



# C
# a = int(input())  #5
# b = list(map(int, input().split()))   #1 2 3 4 5
# for i in range(0, int(a/2)):
#     b.pop(i+1)
# print(*b)  #1 3 5



# D
# a = int(input())  # количество чисел
# b = list(map(int, input().split()))   # сами числа

# c = set(b)  # уникальные числа
# b.sort()    # можно и не сортировать, но пусть будет

# Rep = 0            # максимальная частота
# Answer = []        # список всех мод

# for i in c:
#     v = b.count(i)
#     if v > Rep:        # нашли новую максимальную частоту
#         Rep = v
#         Answer = [i]   # сброс списка
#     elif v == Rep:     # та же частота, добавляем
#         Answer.append(i)

# # сортировка по убыванию
# Answer.sort(reverse=True)

# print(*Answer)

        
        
# E
# a = int(input())
# b = []


# for i in range(a):
#     b.append(str(input()))
# c = set(b)


# print(f"All in all: {len(c)}")
# print("Students:")
# for i in c:
#     print(i)



A = int(input())
B = list(map(int, input().split()))
C = [-1] * A  

for i in range(A):
    for j in range(i - 1, -1, -1): 
        if B[j] < B[i]:            
            C[i] = B[j]
            break                  
print(*C)
    
    

    