#!/usr/bin/env python
# coding: utf-8


import json

json_file = open('D:\Redesign - Pipeline Test v03\Redesign - Pipeline Developer Test v03\CAWAPR-01-Input.json')

y = json.load(json_file)



## Sorting only one collection to understand the file in a better way

priorty = {i : idx for idx , i in enumerate(['V:/data/shot/', 'V:/data/IO/' , 'V:/data/editorial/'])}
sor_key = lambda y :(y['path'], priorty[('/'.join(y['path'].split('/')[0:3]) + '/')])
sorted_files = sorted(y['collection_04']['files'], key=sor_key , reverse = True)
seen = set()
new_l = []
for k in sorted_files:
    tuples = tuple(k.items())
    if ''.join(tuples[0][1].split('/')[3:]) not in seen:
        seen.add(''.join(tuples[0][1].split('/')[3:]))
        new_l.append(k)         
                     
                     
                     
                     
                     

                     
                     


# In[5]:


new_l


# In[9]:


# Sorting the complete file, as per the desired output



priorty = {i : idx for idx , i in enumerate(['V:/data/shot/', 'V:/data/IO/' , 'V:/data/editorial/'])}
sor_key = lambda y :(y['path'], priorty[('/'.join(y['path'].split('/')[0:3]) + '/')])
collection = {}
for i in y:
    new_c = {}
    for j in y[i]:
        sorted_files = sorted(y[i][j], key=sor_key , reverse = True)
        seen = set()
        new_l = []
        for k in sorted_files:
            tuples = tuple(k.items())
            if ''.join(tuples[0][1].split('/')[3:]) not in seen:
                seen.add(''.join(tuples[0][1].split('/')[3:]))
                new_l.append(k)
                
        
        
        new_c.__setitem__('files' , new_l)
        collection.__setitem__(i , new_c)


# print collection                    
                                                 
        



# In[11]:


collection


# In[ ]:




