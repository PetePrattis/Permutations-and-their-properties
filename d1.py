# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

'''
Π15120 Παναγιώτης Πράττης
Η εργασία δημιουργεί μια μετάθεση η οποία έχει τυχαίο μήκος n, κάνοντας ανακάτεμα
μια λίστας με αριθμούς απο 1 έως n και στην συνέχεια υπολογίζει κα ιεμφανίζει τα ζητούμενα
'''
    

#Main
print("Θα δημιουργηθεί μια μετάθεση τυχαίου μήκους.")
m = []
m1=[]
m2=[]

l = random.randint(5,15)
print("Ερώτημα i):")
print("Το μήκος της μετάθεσης ειναι: ", l)
for i in range(l):
    m1.append(i+1)
    m2.append(i+1)
    
random.shuffle(m2)
print("Η μετάθεση είναι η εξής:")
print(m1)
print(m2)

zip_pairs = zip(m2, m1)

reverse_m1 = [i for _, i in sorted(zip_pairs)]
reverse_m2 = []
for i in range(l):
    reverse_m2.append(i+1)
    
print("Ερώτημα ii):")
print("Η αντίστροφη της μετάθεσης:")
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
print("Ερώτημα iii):")   
print("Η μετάθεση ως γινόμενο ξένων κύκλων είναι η εξής:")
print(c)
n = len(c)
nc = []
for i in range(n):
    if len(c[i]) == 2:
        nc.append(c[i])
    elif len(c[i]) > 2:
        for j in range(len(c[i]) - 1):
            nc.append([c[i][0],c[i][j+1]])

print("Ερώτημα iv):")
print("Η μετάθεση ως γινόμενο αντιμεταθέσεων είναι η εξής:")
print(nc)
s = len(nc)
sgn = 0
if s % 2 == 0:
    sgn = 1
else:
    sgn = -1

print("Ερώτημα v):")
if sgn == 1:
    print("Η μετάθεση είναι άρτια διότι έχει άρτιο πλήθος αντιμεταθέσεων,", s, ".")
else:
    print("Η μετάθεσή μου είναι περιττή διότι έχει περιττό πλήθος αντιμεταθέσεων,", s, ".")
                    
        
    

    
    

