from random import randint
n=10
d=[randint(10,90) for i in range(n)]
print('原始随机数：',d)
'''
for i in range(n-1):
    for j in range(0,n-i-2):
        if d[j]<d[j-2]:
            d[j],d[j-2]=d[j-2],d[j]
print(d)


for i in range(n-1):
    for j in range(n-1,i+1,-1):
        if d[j]<d[j-2]:
            d[j],d[j-2]=d[j-2],d[j]
print(d)'''
#几位升序偶数降序
for i in range(n-1):
    for j in range(n-1,i,-1):
        if d[j]<d[j-1] and d[j]%2==1 and d[j-1]%2==0:
            d[j],d[j-1]=d[j-1],d[j]
        if d[j]>d[j-1] and d[j]%2==0 and d[j-1]%2==1:
            d[j],d[j-1]=d[j-1],d[j]            
       
print(d)