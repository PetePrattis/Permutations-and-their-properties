# ! /usr/bin/env python
# -*- coding: utf-8 -*-

#Author Παναγιώτης Πράττης/Panagiotis Prattis

'''
Write a program that receives an input with a permutation μ of [n] in the list format from natural numbers 
separated by the space character (eg 7 10 9 11 2 1 3 5 6 8 4) and prints some properties of the permutation μ.
'''

import random

#Main
print("A random length permutation will be created.")
m = []
m1=[]
m2=[]

l = random.randint(5,15)
print("Exercise 1):")
print("The length of μ is: ", l)
for i in range(l):
    m1.append(i+1)
    m2.append(i+1)
    
random.shuffle(m2)
print("The permutation μ is:")
print(m1)
print(m2)

zip_pairs = zip(m2, m1)

reverse_m1 = [i for _, i in sorted(zip_pairs)]
reverse_m2 = []
for i in range(l):
    reverse_m2.append(i+1)
    
print("Exercise 2):")
print("The reverse of μ is:")
print(reverse_m1)
print(reverse_m2)
    
completed = False
first = True
c1=[]
c2 =[]
c=[]
x = 0
while completed == False:
    if m1[x] not in c1:
        c1.append(m1[x])
        c2.append(m1[x])
        x = m2[x]            
    else:
        x = -1
        first = True
        for i in range(l):
            if m1[i] not in c1 and first == True:
                first = False
                x = i
        if x == -1:
            completed = True
            c.append(c2)
            c1.append(m1[x])
            c2 = []
        else:
            c.append(c2)
            c1.append(m1[x])
            c2 = []
            c2.append(m1[x])
            x = m2[x]
    for i in range(l):
        if m1[i] == x:
            x = i
print("Exercise 3):")   
print("The μ as the product of cycles is:")
print(c)
n = len(c)
nc = []
for i in range(n):
    if len(c[i]) == 2:
        nc.append(c[i])
    elif len(c[i]) > 2:
        for j in range(len(c[i]) - 1):
            nc.append([c[i][0],c[i][j+1]])

print("Exercise 4):")
print("The μ as a product  of transpositions is:")
print(nc)
s = len(nc)
sgn = 0
if s % 2 == 0:
    sgn = 1
else:
    sgn = -1

print("Exercise 5):")
if sgn == 1:
    print("The parity of μ is even because it has an even number of transpositions,", s, ".")
else:
    print("The parity of μ is odd because it has an odd number of transpositions,", s, ".")
                    
        
    

    
    

