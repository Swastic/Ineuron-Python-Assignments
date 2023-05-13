#!/usr/bin/env python
# coding: utf-8

# Q1:How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the
# number of seconds in a minute (60) by the number of minutes in an hour (also 60).

# In[1]:


60*60


# Q2: Assign the result from the previous task (seconds in an hour) to a variable called
# seconds_per_hour.

# In[2]:


seconds_per_hour = 3600


# Q3: How many seconds do you think there are in a day? Make use of the variables seconds per hour
# and minutes per hour.

# In[3]:


seconds_per_hour*24


# Q4: Calculate seconds per day again, but this time save the result in a variable called seconds_per_day

# In[4]:


seconds_per_day = seconds_per_hour*24
seconds_per_day


# Q5: Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.

# In[5]:


seconds_per_day / seconds_per_hour


# Q6: Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree
# with the floating-point value from the previous question, aside from the final .0?

# In[6]:


seconds_per_day // seconds_per_hour


# Q7: Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to
# its next() method: 2, 3, 5, 7, 11, ...

# In[ ]:


def genPrimes():
    
    primes = [ 2, 3, 5, 7, 11 ]
    
    def isPrimeNumber(n):
        if n in primes:
            return True
        
        for elem in primes:
            if n % elem == 0:
                return False
                
        primes.append(n)
        return True
    num = 1
    while True:
        num += 1
        if isPrimeNumber(num):
            next = num
            yield next
            num = next
primeNumber = genPrimes()

for i in range(189):
    print(primeNumber.__next__())

