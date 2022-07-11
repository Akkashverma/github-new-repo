#!/usr/bin/env python
# coding: utf-8

# In[11]:


import json


# In[12]:


json_file = open('D:\Redesign - Pipeline Test v03\Redesign - Pipeline Developer Test v03\CAWAPR-01-Input.json')


# In[13]:


x = json.load(json_file)


# In[15]:


## Sorting only one collection to understand the file in a better way

priorty = {i : idx for idx , i in enumerate(['V:/data/IO/' ,'V:/data/shot/', 'V:/data/editorial/'])}
sor_key = lambda x :(x['path'], priorty[('/'.join(x['path'].split('/')[0:3])+ '/')])
sorted_files = sorted(x['collection_04']['files'], key=sor_key , reverse = True)
seen = set()
new_l = []
for k in sorted_files:
    tuples = tuple(k.items())
    if ''.join(tuples[0][1].split('/')[3:]) not in seen:
        seen.add(''.join(tuples[0][1].split('/')[3:]))
        new_l.append(k)         


# In[17]:





# In[18]:


#Sorting the complete file, as per the desired output


priorites = {i:idx for idx, i in enumerate(['V:/data/shot/', 'V:/data/IO/', 'V:/data/editorial/'])}
sort_key= lambda x:(x['path'], priorites[('/'.join(x['path'].split('/')[0:3])+'/')])   
collection = {}
for collections in x:
    newFile = {}
    for file in x[collections]:
        sorted_files = sorted(x[collections][file], key=sort_key, reverse=True)
        seen = set()
        new_l = []
        for d in sorted_files:
            t = tuple(d.items())
            if ''.join(t[0][1].split('/')[3:]) not in seen:
                seen.add(''.join(t[0][1].split('/')[3:]))
                new_l.append(d)
       
        newFile.__setitem__('files', new_l)
    collection.__setitem__(collections, newFile)
# print(collection)
with open("CAWAPR-01-Ouput.json", "w") as outfile:
    json.dump(collection, outfile)


# In[20]:





# In[ ]:




