#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("""This is a python script that will take a certain number of premises 
and thier forms and a conclusion to show their truth table.
Inspired by the sixth chapter of Understanding Arguments: An Introduction to informal logic
by Walter Simmott-Armstrong and Robert Fogelin

14/07/2020
Ahmed Alrabiah""")


# In[43]:


import re
from tabulate import tabulate
print('''These are the different ways to enter the premises:
1. p
2. ~p
3. p&q
4. p or q
5. if p then q
and their combinations\n\n''')

premises = input("Enter all the premises comma separated (with a space after each comma): \n")
con = input("Enter the conclusion: \n")

pre = {}
for i in ''.join(re.split(' or |&|if | then |~| |, ',premises)):#To add the single variables in the pre dictionary
    if ((ord(i) >= ord('A')) & (ord(i) <= ord('Z'))) or ((ord(i) >= ord('a') and ord(i) <= ord('z'))):
        pre[i] = ''
    
    
pre.pop('', None)
premises = premises.split(', ')

for i,k in zip(pre.keys(), range(len(pre))): #Write the truth values of the single variables
    counter = 0
    values = ''
    while counter < 2**len(pre):
        for j in range(2**len(pre)//2**(k+1)):
            values = values + 'T, '
            counter += 1
        for j in range(2**len(pre)//2**(k+1)):
            values = values + 'F, '
            counter += 1
        pre.update({i: values[:-2]})



for i in premises: #To add the negated single variables to the dictionary pre
    for j,k in zip(i, range(len(i))):
        if j == '~' and (((ord(j) >= ord('A')) & (ord(j) <= ord('Z'))) or ((ord(j) >= ord('a') and ord(j) <= ord('z')))):
            pre[j+i[k+1]] = ''

for i in premises: #To take what is in the premises
    for j in range(len(i)):
        flag = False
        if i[j] == '(':
            x = j+1
            flag = True
        if i[j] == ')':
            pre[i[x:j:]] = ''
    if flag == False:
        pre[i] = ''
            

for i in pre.keys(): #The truth values of the negated variables
    if '~' == i[:-1]:
        for key, value in pre.items():
            if key == i[1:]:
                pre[i] = value[::-1]


# In[44]:


for key, value in pre.items(): #add 
    if value == '':
        pass

for i in premises: #Add the premises to the dictionary
    if i not in pre:
        pre[i] = ''


# In[45]:


print(pre)


# In[ ]:





# In[ ]:




