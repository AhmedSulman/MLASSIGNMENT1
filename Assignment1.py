#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Task 1.1 

nums = [3,5,7,8,12]
cubes = []
for i in nums:
    cubes.append(i**3)
print(cubes)


# In[26]:


# Task 1.2

dict = {}
dict['parrot'] = 2
dict['goat'] = 4
dict['spider'] = 8
dict['crab'] = 10
print(dict)
TOTAL_LEGS = 0;
for animal,legs in dict.items():
    print(f"{animal}, {legs}")
    TOTAL_LEGS = TOTAL_LEGS + legs;

print(TOTAL_LEGS)


# In[27]:


# Task 1.3

A = (3,9,4,[5,6])
A[3][0] = 8 
print(A)


# In[28]:


# Task 1.4
del A


# In[29]:


print(A)


# In[30]:


# Task 1.5
B = ('a','p','p','l','e')
count = B.count('p')
print(count)


# In[31]:


# Task 1.6
B = ('a','p','p','l','e')
index = B.index('l')
print(index)


# In[32]:


# Task 2.1
import numpy as np

A = np.array([[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]])
print(A)


# In[33]:


# Task 2.2
b = A[0:2,0:2]
print(b)


# In[34]:


# Task 2.3 
c = np.empty_like(A)
print(c)

# The exact content of C will be random, as np.empty() does not initialize the array entries. 


# In[35]:


# Task 2.4
z = np.array([1, 0, 1])
for i in range(A.shape[1]):
    c[:, i] = A[:, i] + z
print(c)


# In[36]:


X = np.array([[1,2],[3,4]])
Y = np.array([[5,6],[7,8]])
v = np.array([9,10])
# Task 2.5
Addition = X + Y
print(Addition)


# In[20]:


# Task 2.6
Multiplication = X*Y
print(Multiplication)


# In[37]:


# Task 2.7
Square_root = np.sqrt(Y)
print(Square_root)


# In[38]:


# Task 2.8
Dot_product = np.dot(X, v)
print(Dot_product)


# In[39]:


# Task 2.9
Sum = np.sum(X, axis=0)
print(Sum)


# In[40]:


# Task 3.1
def compute( distance, time):
    if time == 0:
        return "Time cannot be zero"
    velocity = distance/time
    return velocity
velocity = compute( 50, 0)
print(velocity)


# In[10]:


velocity = compute( 50, 10)
print(velocity)


# In[41]:


# Task 3.2
even_num = [2,4,6,8,10,12]
def mult(even_num):
    product = 1
    for num in even_num:
        product *= num
    return product

result = mult(even_num)
print(result)


# In[42]:


# Task 4
import pandas as pd
data =  {
    'C1': [1, 2, 3, 5, 5],
    'C2': [6, 7, 5, 4, 8],
    'C3': [7, 9, 8, 6, 5],
    'C4': [7, 5, 2, 8, 8]
}
df = pd.DataFrame(data)
print(df)


# In[43]:


# Task 4.1
print(df.head(2))


# In[44]:


# Task 4.2
print(df['C2'])


# In[49]:


# Task 4.3
df.rename(columns = { 'C3':'B3'})
print(df)


# In[54]:


# Task 4.4
df['Sum'] = 0
print(df)


# In[55]:


# Task 4.5
df['Sum'] = df.sum(axis = 1)
print(df)


# In[62]:


# Task 4.6
df_csv = pd.read_csv('hello_sample.csv')


# In[63]:


# Task 4.7
print(df_csv)


# In[64]:


# Task 4.8
print(df_csv.tail(2))


# In[65]:


# Task 4.9
df_csv.info()


# In[66]:


# Task 4.10
print(df_csv.shape)


# In[67]:


# Task 4.11
df_csv_sorted = df_csv.sort_values(by='Weight')
print(df_csv_sorted)


# In[68]:


# Task 4.12
df_csv.isnull()


# In[69]:


df_csv.dropna()


# In[ ]:




