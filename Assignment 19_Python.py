#!/usr/bin/env python
# coding: utf-8

# Q1: Make a class called Thing with no contents and print it. Then, create an object called example
# from this class and also print it. Are the printed values the same or different?

# In[2]:


class Thing:
    pass
print(Thing)


# In[3]:


example = Thing()
print(example)


# Q2: Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters
# should be printed.

# In[4]:


class Thing2:
    letters = 'abc'
print(Thing2.letters)


# Q3: Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance
# (object) attribute called letters. Print letters. Do you need to make an object from the class to do
# this?

# In[5]:


class Thing3:
    def __init__(self):
        self.letters = 'xyz'


# In[6]:


print(Thing3.letters)


# In[7]:


something = Thing3()
print(something.letters)


# Q4: Create an Element class with the instance attributes name, symbol, and number. Create a class
# object with the values 'Hydrogen,' 'H,' and 1.

# In[8]:


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
hydrogen = Element('Hydrogen', 'H', 1)


# Q5: Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then,
# create an object called hydrogen from class Element using this dictionary.

# In[9]:


#Starting with the dictionary:
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}


# In[10]:


#Creating object called hydrogen from class Element using el_dict
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])


# In[11]:


hydrogen.name


# In[12]:


hydrogen = Element(**el_dict)
hydrogen.name


# Q6: For the Element class, define a method called dump() that prints the values of the object’s
# attributes (name, symbol, and number). Create the hydrogen object from this new definition and
# use dump() to print its attributes.

# In[13]:


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))
hydrogen = Element(**el_dict)
hydrogen.dump()


# Q7: Call print(hydrogen). In the definition of Element, change the name of method dump to __str__,
# create a new hydrogen object, and call print(hydrogen) again.

# In[14]:


print(hydrogen)


# In[15]:


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))

hydrogen = Element(**el_dict)
print(hydrogen)


# Q8: Modify Element to make the attributes name, symbol, and number private. Define a getter
# property for each to return its value.

# In[16]:


class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property    
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number
hydrogen = Element('Hydrogen', 'H', 1)


# In[17]:


hydrogen.name


# In[18]:


hydrogen.symbol


# In[19]:


hydrogen.number


# Q9: Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This
# should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from
# each and print what it eats.

# In[20]:


class Bear:
    def eats(self):
        return 'berries'
    
class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'
    
b = Bear()
r = Rabbit()
o = Octothorpe()


# In[21]:


print(b.eats())


# In[22]:


print(r.eats())


# In[23]:


print(o.eats())


# Q10: Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This
# returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that
# has one instance (object) of each of these. Define a does() method for the Robot that prints what its
# component objects do.

# In[24]:


class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'
    
class SmartPhone:
    def does(self):
        return 'ring'
    
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
        
    def does(self):
        return '''I have many attachments:
        My laser, to %s.
        My claw, to %s.
        My smartphone, to %s.''' % (self.laser.does(),self.claw.does(),self.smartphone.does() )


# In[25]:


robbie = Robot()


# In[26]:


print( robbie.does())


# In[ ]:




