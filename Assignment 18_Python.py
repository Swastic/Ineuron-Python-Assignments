#!/usr/bin/env python
# coding: utf-8

# Q1: Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'.
# Then, use the interactive interpreter to import the zoo module and call its hours() function.

# In[4]:


import zoo
zoo.hours()


# Q2: In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

# In[5]:


import zoo as menagerie
menagerie.hours()


# Q3: Using the interpreter, explicitly import and call the hours() function from zoo.

# In[6]:


from zoo import hours
hours()


# Q4: Import the hours() function as info and call it.

# In[7]:


from zoo import hours as info
info()


# Q5: Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.

# In[8]:


plain_dict = {'a': 1, 'b': 2, 'c': 3}
plain_dict


# Q6: Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the
# same order as plain?

# In[9]:


from collections import OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
fancy


# Q7: Make a default dictionary called dict_of_lists and pass it the argument list. Make the list
# dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print
# dict_of_lists['a'].

# In[10]:


from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
dict_of_lists['a']


# In[ ]:




