#!/usr/bin/env python
# coding: utf-8

# Q1: Create a list called years_list, starting with the year of your birth, and each year thereafter until
# the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list =
# [1980, 1981, 1982, 1983, 1984, 1985].

# In[1]:


years_list = [1996,1997,1998,1999,2000,2001]


# Q2: In which year in years_list was your third birthday? Remember, you were 0 years of age for your
# first year.

# In[2]:


years_list[2]


# Q3: In the years list, which year were you the oldest?

# In[3]:


years_list[-1]


# Q4: Make a list called things with these three strings as elements: "mozzarella", "cinderella",
# "salmonella".

# In[4]:


things = ['mozzarella','cinderella','salmonella']
things


# Q5: Capitalize the element in things that refers to a person and then print the list. Did it change the
# element in the list?

# In[5]:


things_cap = things.copy()
things_cap[1].capitalize()


# Q6: Make a surprise list with the elements "Groucho," "Chico," and "Harpo."

# In[6]:


surprise = ['Groucho', 'Chico', 'Harpo']
surprise


# Q7: Lowercase the last element of the surprise list, reverse it, and then capitalize it.

# In[8]:


surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1].capitalize()


# Q8: Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is
# chien, cat is chat, and walrus is morse.

# In[9]:


e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
e2f


# Q9: Write the French word for walrus in your three-word dictionary e2f.

# In[10]:


e2f['walrus']


# Q10: Make a French-to-English dictionary called f2e from e2f. Use the items method.

# In[11]:


f2e = {}
for english, french in e2f.items():
 f2e[french] = english
f2e


# Q11: Print the English version of the French word chien using f2e.

# In[12]:


f2e['chien']


# Q12: Make and print a set of English words from the keys in e2f.

# In[13]:


set(e2f.keys())


# Q13: Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants',
# and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and
# 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'.
# Make all the other keys refer to empty dictionaries.

# In[14]:


life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],'octopi': {},'emus': {}},'plants': {},'other': {}}
life


# Q14: Print the top-level keys of life.

# In[15]:


print(life.keys())


# Q15: Print the keys for life['animals'].

# In[16]:


print(life['animals'].keys())


# Q16: Print the values for life['animals']['cats']

# In[ ]:


print(life['animals']['cats'])

