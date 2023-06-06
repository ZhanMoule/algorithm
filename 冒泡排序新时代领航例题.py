# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:54:55 2023
新时代领航作业本例题
@author:Moule
"""
#对奇数偶数位置进行升序
a=[8,1,2,6,3,4,7,5];n=len(a)
for i in range((n+1)//2):
    for j in range(n-1,i*2,-1):
        if a[j]<a[j-2]:
            a[j],a[j-2]=a[j-2],a[j]
    print(a)
#要求对奇数和偶数进行生序排序，奇数在前偶数在后  
'''      
for i in range(len(a)):
    for j in range(len(a)-1,i,-1):
        if a[j]%2==a[j-1]%2 and a[j]<a[j-1] or a[j]%2>a[j-1]%2:
            a[j],a[j-1]=a[j-1],a[j]
'''
        
        
        
