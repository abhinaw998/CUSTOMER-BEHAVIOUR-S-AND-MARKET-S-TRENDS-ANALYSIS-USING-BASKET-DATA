#!/usr/bin/env python
# coding: utf-8

# # Libraries
# !pip install apyori
# !pip install wordcloud
# !pip install seaborn
# !pip install mlxtend
# !pip install matplotlib
# !pip install apyori

# In[19]:


# for basic operations
import numpy as np
import pandas as pd

# for visualizations
import matplotlib.pyplot as plt
import squarify
import seaborn as sns
plt.style.use('fivethirtyeight')

# for defining path
import os

# for market basket analysis
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


# In[20]:


# reading the dataset
data = pd.read_csv('Market_Basket_Optimisation.csv',header=None )
# let's check the shape of the dataset
data.shape# checking the head of the data


# In[21]:


# checking the head of the data
data.head()


# In[22]:


import matplotlib.pyplot as plt


# checkng the tail of the data
data.tail()


# In[23]:


# checking the random entries in the data
data.sample(8)


# In[24]:


# let's describe the dataset
data.describe()


# In[25]:


# looking at the frequency of most popular items 
plt.rcParams['figure.figsize'] = (18, 7)
color = plt.cm.copper(np.linspace(0, 1, 40))
data[0].value_counts().head(40).plot.bar(color = color)
plt.title('frequency of most popular items', fontsize = 20)
plt.xticks(rotation = 90 )
plt.grid()
plt.show()


# In[26]:


#import matplotlib.pyplot as plt
import seaborn as sns 
from wordcloud import WordCloud
plt. rcParams['figure.figsize']=(15,15)
wordcloud=WordCloud(background_color ='white', width = 1200, height = 1200, max_words= 121).generate(str(data[0]))
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Most Popular Items',fontsize=20)
plt.show()


# In[27]:



y = data[0].value_counts().head(50).to_frame()
y.index
#len(y)


# In[28]:


# plotting a tree map
import squarify
plt.rcParams['figure.figsize'] = (20, 20)
color = plt.cm.cool(np.linspace(0, 1, 50))
squarify.plot(sizes = y.values, label = y.index, alpha=.8, color = color)
plt.title('Tree Map for Popular Items')
plt.axis('off')
plt.show()


# In[29]:


data['food'] = 'Food'
food = data.truncate(before = -1, after = 15)
import networkx as nx

food = nx.from_pandas_edgelist(food, source = 'food', target = 0, edge_attr = True)


# In[30]:


import warnings
warnings.filterwarnings('ignore')

plt.rcParams['figure.figsize'] = (20, 20)
pos = nx.spring_layout(food)
color = plt.cm.Wistia(np.linspace(0, 15, 1))
nx.draw_networkx_nodes(food, pos, node_size = 15000, node_color = color)
nx.draw_networkx_edges(food, pos, width = 3, alpha = 0.6, edge_color = 'black')
nx.draw_networkx_labels(food, pos, font_size = 20, font_family = 'sans-serif')
plt.axis('off')
plt.grid()
plt.title('Top 15 First Choices', fontsize = 40)
plt.show()


# In[31]:


data['secondchoice'] = 'Second Choice'
secondchoice = data.truncate(before = -1, after = 15)
secondchoice = nx.from_pandas_edgelist(secondchoice, source = 'food', target = 1, edge_attr = True)


# In[32]:


import warnings
warnings.filterwarnings('ignore')

plt.rcParams['figure.figsize'] = (20, 20)
pos = nx.spring_layout(secondchoice)
color = plt.cm.Blues(np.linspace(0, 15, 1))
nx.draw_networkx_nodes(secondchoice, pos, node_size = 15000, node_color = color)
nx.draw_networkx_edges(secondchoice, pos, width = 3, alpha = 0.6, edge_color = 'brown')
nx.draw_networkx_labels(secondchoice, pos, font_size = 20, font_family = 'sans-serif')
plt.axis('off')
plt.grid()
plt.title('Top 15 Second Choices', fontsize = 40)
plt.show()


# data['thirdchoice'] = 'Third Choice'
# secondchoice = data.truncate(before = -1, after = 10)
# secondchoice = nx.from_pandas_edgelist(secondchoice, source = 'food', target = 2, edge_attr = True)
# 
# 

# In[16]:


import warnings
warnings.filterwarnings('ignore')

plt.rcParams['figure.figsize'] = (20, 20)
pos = nx.spring_layout(secondchoice)
color = plt.cm.Reds(np.linspace(0, 15, 1))
nx.draw_networkx_nodes(secondchoice, pos, node_size = 15000, node_color = color)
nx.draw_networkx_edges(secondchoice, pos, width = 3, alpha = 0.6, edge_color = 'pink')
nx.draw_networkx_labels(secondchoice, pos, font_size = 20, font_family = 'sans-serif')
plt.axis('off')
plt.grid()
plt.title('Top 10 Third Choices', fontsize = 40)
plt.show()


# In[33]:


# making each customers shopping items an identical list
trans = []
for i in range(0, 7501): # because total record is 7501
    trans.append([str(data.values[i,j]) for j in range(0, 20)])
    # j denotes the totoal column that is 20
    #print(trans[i])


# In[ ]:


#from mlxtend.frequent_patterns import apriori

from apyori import apriori

#Now, let us return the items and itemsets with at least 5% support:
association_Rules=apriori(trans, min_support = 0.005, min_confidence = 0.25, min_lift =3,min_length = 2)
associationResults=list(association_Rules)
#for i in associationResults:
print(associationResults[0])
print('')
print(len(associationResults))


# In[24]:


for item in associationResults:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    if(item[1]>=0.0057):
        print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
        print("Support: " + str(item[1]))
        #third index of the list located at 0th
        #of the third index of the inner list\
        print("Confidence: " + str(item[2][0][2]))
        print("Lift: " + str(item[2][0][3]))
        print("=====================================")
pair = item[0] 
items = [x for x in pair]
items


# In[35]:


#from mlxtend.frequent_patterns import apriori

from apyori import apriori

#Now, let us return the items and itemsets with at least 5% support:
association_Rules=apriori(trans, min_support = 0.005, min_confidence = 0.25, min_lift =3,min_length = 2)
associationResults=list(association_Rules)
#for i in associationResults:
print(associationResults[0])
print('')
print(len(associationResults))


# In[ ]:




