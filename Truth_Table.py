#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("""This is a python script that will take a certain number of premises 
and thier forms and a conclusion to show their truth table.
Inspired by the sixth chapter of Understanding Arguments: An Introduction to informal logic
by Walter Simmott-Armstrong and Robert Fogelin

14/07/2020
Ahmed Alrabiah""")


# In[2]:


import re
from tabulate import tabulate
print('''These are the different ways to enter the premises:
1. p
2. ~p
3. p&q
4. p or q
5. if p then q
and their combinations with parenthesis\n\n''')

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
            values = values + 'T'
            counter += 1
        for j in range(2**len(pre)//2**(k+1)):
            values = values + 'F'
            counter += 1
        pre.update({i: values})


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
            flag = True
    if flag == False:
        pre[i] = ''



for i in pre.keys(): #The truth values of the negated variables
    if '~' == i[:-1]:
        for key, value in pre.items():
            if key == i[1:]:
                pre[i] = value[::-1]
                
for i in premises: #If a parentheses is negated, this will add it
    for j in range(len(i)):
        if i[j] == '~' and i[j+1] == "(":
            for k in range(j,len(i)):
                if i[k] == ')':
                    pre[i[j:k+1:]] = ''
                    break


# In[3]:


#Now the truth values of the single charecters are already added and also the the single negated charecters are added

#The next part will add the truth values of the connected propositions

for key, value in pre.items(): #add the truth values of the propositions of pre without the last premises
    if value == '':
        #Adding the truth values of the connected propositions
        truths = ''
        if key[:2:] == 'if':
            for i,j in zip(pre[key[3:4:]], pre[key[-1::]]):
                if i == 'T' and j == 'F':
                    truths += 'F'
                elif i == 'T' or i == 'F':
                    truths += 'T'
        
        elif key[:1:] in pre:
            for i,j in zip(pre[key[:1:]], pre[key[-1::]]):
                if key[1:2:] == '&':
                    #and truth values
                    if i == 'T' and j == 'T':
                        truths += 'T'
                    elif i == 'T' or i == 'F':
                        truths += 'F'
                if key[2:4:] == 'or':
                    #or truth values
                    if i == 'F' and j == 'F':
                        truths += 'F'
                    elif i == 'T' or i == 'F':
                        truths += 'T'
        
        for i in range(len(key)): #This loop adds the truth values of a negated connected proposition
            if key[i] == '~' and key[i + 1] == "(":
                for j in range(i, len(key)):
                    if key[j] == ")":
                        if key[i+2:j:] in pre.keys():
                            for k in pre[key[i+2:j:]]:
                                if k == 'T':
                                    truths += 'F'
                                elif k == 'F':
                                    truths += 'T'
        pre[key] = truths
        
#The next part will add the premises and the truth values of the premises
for key in premises: #Add the premises to the dictionary
    if key not in pre:
        truths = ''
        for i in range(len(key)):
            if key[i] == '&' and key[i - 1] == ')':
                for j,k in zip(pre[key[0:i:]], pre[key[i+1::]]):
                    if j == 'T' and k == 'T':
                        truths += 'T'
                    elif j == 'T' or j == 'F':
                        truths += 'F'
            elif key[i-1:i+3:] == ' or ' and key[i - 2] == ')':
                for j,k in zip(pre[key[0:i-1:]], pre[key[i+3::]]):
                    if j == 'F' and k == 'F':
                        truths += 'F'
                    elif j == 'T' or j == 'F':
                        truths += 'T'
            pre[key] = truths


# In[4]:


#Now dealing with the conclusion:


# In[5]:


print(tabulate(pre, headers="keys"))


# In[ ]:


input()

