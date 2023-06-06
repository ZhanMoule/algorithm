from random import randint
n=10
d=[randint(10,90) for i in range(n)]
print('原始随机数：',d)

i=0
while i<n:
    for j in range(n-1):
        if d[j] < d[j - 1]:
                d[j],d[j - 1]=d[j - 1],d[j]
    i+=1
print(d)
                                                          
