from collections import deque

n = int(input().strip())
students = input().strip()

s_queue = deque()
k_queue = deque()

 
for i, ch in enumerate(students):
    if ch == 'S':
        s_queue.append(i)
    else:
        k_queue.append(i)

# Симуляция
while s_queue and k_queue:
    s = s_queue.popleft()
    k = k_queue.popleft()
    if s < k:
        s_queue.append(s + n)  
    else:
        k_queue.append(k + n)  

 
if s_queue:
    print("SAKAYANAGI")
else:
    print("KATSURAGI")
