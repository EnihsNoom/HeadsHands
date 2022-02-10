"""
Created on Thu Feb 10 16:42:11 2022

@author: Snezhana
"""

import random as rn
import numpy as np

def  arr_sort (n):
    max=10 #верхнее ограничение для всех чисел кода
    def arr_var(n): #array with various random integers of given size
        arr_s=[0]*n 
        for i in np.arange(0,n,1):
            arr_s[i]=rn.randint(2,max) #let minimum array size = 2
        while(len(arr_s)!=len(set(arr_s))):
            arr_s=set(arr_s)
            while (len(arr_s)!=n):
                arr_s.add(rn.randint(2,max)) 
        arr_s=list(arr_s)
        rn.shuffle(arr_s)
        return(arr_s)

    def rand_arr(a): #array of random numbers of given size
        r_arr=[0]*a
        for i in np.arange(0,a,1):
            b=rn.uniform(-max,max)
            b = float('{:.1f}'.format(b))
            r_arr[i]=b
        return(r_arr)

    if (str(n).isnumeric()==True and n>0 and n<max):
        arr_s=arr_var(n) #array sizes
        print('Размеры массивов: ',arr_s)
        result=[]
        for i in np.arange(0,n,1):
            if i%2!=0:
                a=rand_arr(arr_s[i])
                a.sort()
                result.append(a)
            else:
                a=rand_arr(arr_s[i])
                a.sort(reverse = True)
                result.append(a)
        return (result)
    else:
        print ('Error: The function accepts as input only a natural number less than', max)
        

    

