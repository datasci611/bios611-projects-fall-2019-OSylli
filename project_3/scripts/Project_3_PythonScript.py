#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 2: The relationship between duration of stay at UMD and clients' gender and race
import pandas as pd
client = pd.read_csv('https://raw.githubusercontent.com/datasci611/bios611-projects-fall-2019-OSylli/master/project_3/data/CLIENT_191102.tsv',sep='\t')
client = client.loc[:,['Client ID', 'Client Gender', 'Client Primary Race']]
client.head()


# In[2]:


import pandas as pd
entry_exit = pd.read_csv('https://raw.githubusercontent.com/datasci611/bios611-projects-fall-2019-OSylli/master/project_3/data/ENTRY_EXIT_191102.tsv',sep='\t')
entry_exit = entry_exit.loc[:,['Client ID', 'Entry Date', 'Exit Date']]
entry_exit.head()


# In[3]:


import pandas as pd

record=pd.concat([client, entry_exit],axis=1)
record['Entry Date'] = pd.to_datetime(record['Entry Date'],format='%m/%d/%Y')
record['Exit Date'] = pd.to_datetime(record['Exit Date'],format='%m/%d/%Y')
record['Duration (Days)'] = record['Exit Date']-record['Entry Date']

record['Duration (Days)'] = record['Duration (Days)'].map(lambda x: x.days)

record = record.dropna(axis = 0, how ='any')

record.head()


# In[4]:


# Relationship between the duration of stay at UMD and Client Gender
gender_record = {'Gender':[], 'Count':[], 'AVE_duration':[]}

for value, sub_df in record.groupby('Client Gender'):
    tmp_ave = sub_df['Duration (Days)'].mean()
    gender_record['Gender'].append(value)
    gender_record['Count'].append(sub_df['Duration (Days)'].count())
    gender_record['AVE_duration'].append(tmp_ave)
    
gender_record = pd.DataFrame(gender_record)
gender_record


# In[7]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig

plt.bar(gender_record['Gender'],gender_record['Count'])
plt.title('Relationship between the total number of entry and client gender')
savefig("Q2_Relationship between the total number of entry and client gender.png")


# In[8]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig

plt.bar(gender_record['Gender'],gender_record['AVE_duration'])
plt.title('Relationship between the average time of stay at UMD and client gender')
savefig("Q2_Relationship between the average time of stay at UMD and client gender.png")


# In[9]:


# Relationship between the duration of stay at UMD and Client Race
race_record = {'Race':[], 'Count':[], 'AVE_duration':[], 'Number':[]}

for value, sub_df in record.groupby('Client Primary Race'):
    tmp_ave = sub_df['Duration (Days)'].mean()
    race_record['Race'].append(value)
    race_record['Count'].append(sub_df['Duration (Days)'].count())
    race_record['AVE_duration'].append(tmp_ave)
    
race_record["Number"] = [0,1,2,3,4,5,6,7]
race_record = pd.DataFrame(race_record)
race_record = race_record.drop(5,axis=0) # drop the row in which "Data not collected" is recorded
race_record = race_record.drop(4,axis=0) # drop the row in which "Client refused" is recorded
race_record = race_record.drop(3,axis=0) # drop the row in which "Client doesn't know" is recorded

race_record


# In[10]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig

LABELS = ["American Indian or Alaska Native","Asian","Black or African American","Native Hawaiian or Other Pacific Islander","White"]

plt.bar(race_record['Number'],race_record['Count'])
plt.title('Relationship between the total number of entry and clients\' race')
plt.xticks(race_record['Number'],LABELS,rotation=90)

savefig("Q2_Relationship between the total number of entry and clients\' race.png", bbox_inches = 'tight')


# In[11]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
#race = [0,1,2,6,7]

LABELS = ["American Indian or Alaska Native","Asian","Black or African American","Native Hawaiian or Other Pacific Islander","White"]


plt.bar(race_record['Number'],race_record['AVE_duration'])
plt.title('Relationship between the average time of stay at UMD and clients\' race')
plt.xticks(race_record['Number'],LABELS,rotation=90)

savefig("Q2_Relationship between the average time of stay at UMD and clients\' race.png", bbox_inches = 'tight')


# In[ ]:



