#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly


# In[4]:


chn_data = pd.read_csv('China_data.csv')
sg_data = pd.read_csv('SG_data.csv')
usa_data = pd.read_csv('USA_data.csv')

chn_data['date'] = pd.to_datetime(chn_data['date'])
sg_data['date'] = pd.to_datetime(sg_data['date'])
usa_data['date'] = pd.to_datetime(usa_data['date'])


# ### China Cases, Deaths and Policy Stringency (Matplotlib)

# In[5]:


fig, ax = plt.subplots(3, 1)

ax[0].plot(chn_data['date'], chn_data['new_cases_per_million'], label='Daily New Cases (per Million)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

ax[1].plot(chn_data['date'], chn_data['new_deaths_per_million'], label='Daily New Deaths (per Million)', color='r')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Daily New Deaths (per Million)', color='r')

ax[2].plot(chn_data['date'], chn_data['stringency_index'], label='Stringency Index', color='b')
ax[2].set_xlabel('Date')
ax[2].set_ylabel('Stringency Index', color='b')
ax[2].set_ylim([0, 100])

fig.suptitle('China\'s Daily New Cases, Deaths and Policy Stringency Over Time', fontsize=14)
fig.set_size_inches(12, 14)
fig.legend()
plt.show()


# ### China Cases, Deaths and Policy Stringency (Seaborn)

# In[7]:


fig, axs = plt.subplots(3, 1)

sns.lineplot(x='date', y='value', color='green', label='Daily New Cases (per Million)', 
             data=pd.melt(chn_data[['date','new_cases_per_million']], ['date']), ax=axs[0])
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Daily New Cases (per Million)', color='g')


sns.lineplot(x='date', y='value', color='red', label='Daily New Deaths (per Million)', 
             data=pd.melt(chn_data[['date','new_deaths_per_million']], ['date']), ax=axs[1])
axs[1].set_xlabel('Date')
axs[1].set_ylabel('Daily New Deaths (per Million)', color='r')

sns.lineplot(x='date', y='value', color='blue', label='Stringency Index', 
             data=pd.melt(chn_data[['date','stringency_index']], ['date']), ax=axs[2])
axs[2].set_xlabel('Date')
axs[2].set_ylabel('Stringency Index', color='b')
axs[2].set_ylim([0, 100])

fig.suptitle('China\'s Daily New Cases, Deaths and Policy Stringency Over Time', fontsize=14)
fig.set_size_inches(12, 14)


# ### Singapore Cases, Deaths and Policy Stringency

# In[9]:


fig, ax = plt.subplots(3, 1)

ax[0].plot(sg_data['date'], sg_data['new_cases_per_million'], label='Daily New Cases (per Million)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

ax[1].plot(sg_data['date'], sg_data['new_deaths_per_million'], label='Daily New Deaths (per Million)', color='r')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Daily New Deaths (per Million)', color='r')

ax[2].plot(sg_data['date'], sg_data['stringency_index'], label='Stringency Index', color='b')
ax[2].set_xlabel('Date')
ax[2].set_ylabel('Stringency Index', color='b')
ax[2].set_ylim([0, 100])

fig.suptitle('Singapore\'s Daily New Cases, Deaths and Policy Stringency Over Time', fontsize=12)
fig.set_size_inches(12, 14)
fig.legend()
plt.show()


# ### USA Cases, Deaths and Policy Stringency

# In[10]:


fig, ax = plt.subplots(3, 1)

ax[0].plot(usa_data['date'], usa_data['new_cases_per_million'], label='Daily New Cases (per Million)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

ax[1].plot(usa_data['date'], usa_data['new_deaths_per_million'], label='Daily New Deaths (per Million)', color='r')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Daily New Deaths (per Million)', color='r')

ax[2].plot(usa_data['date'], usa_data['stringency_index'], label='Stringency Index', color='b')
ax[2].set_xlabel('Date')
ax[2].set_ylabel('Stringency Index', color='b')
ax[2].set_ylim([0, 100])

fig.suptitle('USA\'s Daily New Cases, Deaths and Policy Stringency Over Time', fontsize=12)
fig.set_size_inches(12, 14)
fig.legend()
plt.show()


#  ### China, Singapore and USA's Policy Stringency over Time

# In[11]:


ax[0] = plt.plot(chn_data['date'], chn_data['stringency_index'], 'r', label = 'China')
ax[1] = plt.plot(sg_data['date'], sg_data['stringency_index'], 'b', label = 'Singapore')
ax[2] = plt.plot(usa_data['date'], usa_data['stringency_index'], 'g', label = 'USA')

# show the plot
plt.title('China, Singapore and USA\'s Policy Stringency over Time')
plt.legend()
plt.gcf().set_size_inches(14, 7)


# ### China, Singapore and USA's Daily New Cases over Time

# In[12]:


ax[0] = plt.plot(chn_data['date'], chn_data['new_cases_per_million'], 'r', label = 'China')
ax[1] = plt.plot(sg_data['date'], sg_data['new_cases_per_million'], 'b', label = 'Singapore')
ax[2] = plt.plot(usa_data['date'], usa_data['new_cases_per_million'], 'g', label = 'USA')

# show the plot
plt.title('China, Singapore and USA\'s Daily New Cases over Time')
plt.legend()
plt.gcf().set_size_inches(14, 7)


# ### China, Singapore and USA's Daily New Deaths over Time

# In[13]:


ax[0] = plt.plot(chn_data['date'], chn_data['new_deaths_per_million'], 'r', label = 'China')
ax[1] = plt.plot(sg_data['date'], sg_data['new_deaths_per_million'], 'b', label = 'Singapore')
ax[2] = plt.plot(usa_data['date'], usa_data['new_deaths_per_million'], 'g', label = 'USA')

# show the plot
plt.title('China, Singapore and USA\'s Daily New Deaths over Time')
plt.legend()
plt.gcf().set_size_inches(14, 7)


# ### Data set with lags

# In[15]:


China_lagged_data = pd.read_csv('China_lagged_data.csv')
SG_lagged_data = pd.read_csv('SG_lagged_data.csv')
USA_lagged_data = pd.read_csv('USA_lagged_data.csv')

China_lagged_data['date'] = pd.to_datetime(China_lagged_data['date'])
SG_lagged_data['date'] = pd.to_datetime(SG_lagged_data['date'])
USA_lagged_data['date'] = pd.to_datetime(USA_lagged_data['date'])


# ### China Policy Correlation 

# In[18]:


china_selected = China_lagged_data[['new_cases_per_million','lag_7_new_cases','lag_14_new_cases','hospital_beds_per_thousand',
                   'testing_policy','contact_tracing','facial_coverings','restrictions_internal_movements',
                  'international_travel_controls','cancel_public_events','restriction_gatherings','school_closures',
                   'workplace_closures','stay_home_requirements']]
china_corr = china_selected.corr()

ax = plt.axes()
sns.heatmap(china_corr, cmap="Blues", ax = ax)
ax.set_title('China Policy Correlation HeatMap')


# In[19]:


china_corr


# ### Singapore Policy Correlation

# In[21]:


sg_selected = SG_lagged_data[['new_cases_per_million','lag_7_new_cases','lag_14_new_cases','hospital_beds_per_thousand',
                   'testing_policy','contact_tracing','facial_coverings','restrictions_internal_movements',
                  'international_travel_controls','cancel_public_events','restriction_gatherings','school_closures',
                   'workplace_closures','stay_home_requirements']]
sg_corr = sg_selected.corr()

ax = plt.axes()
sns.heatmap(sg_corr, cmap="Blues", ax = ax)
ax.set_title('Singapore Policy Correlation HeatMap')


# In[22]:


sg_corr


# ### USA Policy Correlation

# In[23]:


usa_selected = USA_lagged_data[['new_cases_per_million','lag_7_new_cases','lag_14_new_cases','hospital_beds_per_thousand',
                   'testing_policy','contact_tracing','facial_coverings','restrictions_internal_movements',
                  'international_travel_controls','cancel_public_events','restriction_gatherings','school_closures',
                   'workplace_closures','stay_home_requirements']]
usa_corr = usa_selected.corr()

ax = plt.axes()
sns.heatmap(usa_corr, cmap="Blues", ax = ax)
ax.set_title('USA Policy Correlation HeatMap')


# In[24]:


usa_corr


# China
# w/o lagged values
# China top 5 policies based on correlation:
# 1. Facial coverings 0.310618
# 2. International travel controls -0.231562
# 3. School closures 0.138218
# 4. Workplace closures 0.126051
# 5. Stay home requirements 0.085646
# 
# with 7 day lagged values
# 1. Facial coverings 0.296924
# 2. International travel controls -0.230635
# 3. School closures 0.134532
# 4. Workplace closures 0.091537
# 5. Restrictions internal movements 0.059222
# 
# With 14 day lagged values
# 1. Facial coverings 0.277643
# 2. International travel controls  -0.211300
# 3. School closures 0.128296
# 4. Stay home requirements  -0.083454
# 5. Restriction gatherings 0.047025
# 
# SG
# w/o lagged values
# SG top 5 policies based on correlation:
# 1. International travel controls -0.530886
# 2. Testing policy 0.328634
# 3. Workplace closures -0.231974
# 4. Stay home requirements -0.188876
# 5. Cancel public events -0.174157
# 
# with 7 day lagged values
# 1. International travel controls -0.517021
# 2. Testing policy 0.332092
# 3. Workplace closures -0.257619
# 4. Stay home requirements -0.188827
# 5. Cancel public events -0.179562
# 
# with 14 day lagged values
# 1. International travel controls -0.499263
# 2. Testing policy 0.335571
# 3. Workplace closures -0.281445
# 4. Stay home requirements -0.190409
# 5. Cancel public events -0.185291
# 
# US
# w/o lagged values
# US top 5 policies based on correlation:
# 1. International travel controls -0.193599
# 2. restriction_gatherings 0.165790
# 3. testing_policy 0.162607
# 4. Workplace closures -0.127455
# 5. restrictions_internal_movements -0.093459
# 
# with 7 day lagged values
# 1. Testing policy 0.163877
# 2. Restriction gatherings 0.146951
# 3. International travel controls -0.135408
# 4. Workplace closures -0.127127
# 5. School closures 0.062473
# 
# with 14 day lagged values
# 1. Testing policy 0.164217
# 2. Workplace closures -0.126893
# 3. Restriction gatherings 0.115117
# 4. School closures 0.064146
# 5. International travel controls -0.054773

# ### China's Daily New Cases and 5 Policy Indexes Over Time (with lag)

# In[25]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(China_lagged_data['date'], China_lagged_data['lag_7_new_cases'], label='Daily New Cases (lagged 7)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

# ax[1].plot(China_lagged_data['date'], China_lagged_data['lag_14_new_cases'], label='Daily New Cases (lagged 14)', color='orange')
# ax[1].set_xlabel('Date')
# ax[1].set_ylabel('Daily New Cases (per Million)', color='orange')

ax[1].plot(China_lagged_data['date'], China_lagged_data['facial_coverings'], label='Facial Coverings Category', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Facial coverings', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('China\'s Daily New Cases and Facial coverings Policy \n Over Time (with lag)', fontsize=12)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# In[26]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(China_lagged_data['date'], China_lagged_data['lag_7_new_cases'], label='Daily New Cases (lagged 7)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

# ax[1].plot(China_lagged_data['date'], China_lagged_data['lag_14_new_cases'], label='Daily New Cases (lagged 14)', color='orange')
# ax[1].set_xlabel('Date')
# ax[1].set_ylabel('Daily New Cases (per Million)', color='orange')

ax[1].plot(China_lagged_data['date'], China_lagged_data['international_travel_controls'], label='International Travel Controls', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('International Travel Controls', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('China\'s Daily New Cases and International Travel Controls Policy \n Over Time (7 days lagged)', fontsize=10)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# In[27]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(China_lagged_data['date'], China_lagged_data['lag_7_new_cases'], label='Daily New Cases (lagged 7)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

# ax[1].plot(China_lagged_data['date'], China_lagged_data['lag_14_new_cases'], label='Daily New Cases (lagged 14)', color='orange')
# ax[1].set_xlabel('Date')
# ax[1].set_ylabel('Daily New Cases (per Million)', color='orange')

ax[1].plot(China_lagged_data['date'], China_lagged_data['school_closures'], label='School Closures', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('School Closures', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('China\'s Daily New Cases and School Closures Policy \n Over Time (with lags)', fontsize=10)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# In[28]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(China_lagged_data['date'], China_lagged_data['lag_7_new_cases'], label='Daily New Cases (lagged 7)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

# ax[1].plot(China_lagged_data['date'], China_lagged_data['lag_14_new_cases'], label='Daily New Cases (lagged 14)', color='orange')
# ax[1].set_xlabel('Date')
# ax[1].set_ylabel('Daily New Cases (per Million)', color='orange')

ax[1].plot(China_lagged_data['date'], China_lagged_data['workplace_closures'], label='Workplace Closures', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Workplace Closures', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('China\'s Daily New Cases and Workplace Closures Policy \n Over Time (with lags)', fontsize=10)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# In[29]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(China_lagged_data['date'], China_lagged_data['lag_7_new_cases'], label='Daily New Cases (lagged 7)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

# ax[1].plot(China_lagged_data['date'], China_lagged_data['lag_14_new_cases'], label='Daily New Cases (lagged 14)', color='orange')
# ax[1].set_xlabel('Date')
# ax[1].set_ylabel('Daily New Cases (per Million)', color='orange')

ax[1].plot(China_lagged_data['date'], China_lagged_data['restrictions_internal_movements'], label='Restrictions Internal Movements', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Restrictions Internal Movements', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('China\'s Daily New Cases and Workplace Closures Policy \n Over Time (with lags)', fontsize=10)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# ### USA's Daily New Cases and 5 Policy Indexes Over Time (with lag)

# In[30]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(USA_lagged_data['date'], USA_lagged_data['lag_7_new_cases'], label='Daily New Cases (lagged 7)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

# ax[1].plot(USA_lagged_data['date'], USA_lagged_data['lag_14_new_cases'], label='Daily New Cases (lagged 14)', color='orange')
# ax[1].set_xlabel('Date')
# ax[1].set_ylabel('Daily New Cases (per Million)', color='orange')

ax[1].plot(USA_lagged_data['date'], USA_lagged_data['testing_policy'], label='Testing Policy Category', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Testing Policy', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('USA\'s Daily New Cases and Testing Policy \n Over Time (7 days lagged)', fontsize=12)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# In[31]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(USA_lagged_data['date'], USA_lagged_data['lag_7_new_cases'], label='Daily New Cases (per Million)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

# ax[1].plot(USA_lagged_data['date'], USA_lagged_data['lag_14_new_cases'], label='Daily New Cases (lagged 14)', color='orange')
# ax[1].set_xlabel('Date')
# ax[1].set_ylabel('Daily New Cases (per Million)', color='orange')

ax[1].plot(USA_lagged_data['date'], USA_lagged_data['restriction_gatherings'], label='Restriction Gatherings Category', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Restriction Gatherings', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('USA\'s Daily New Cases and Restriction Gatherings \n Over Time (7 days lagged)', fontsize=12)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# In[32]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(USA_lagged_data['date'], USA_lagged_data['lag_7_new_cases'], label='Daily New Cases (per Million)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

# ax[1].plot(USA_lagged_data['date'], USA_lagged_data['lag_14_new_cases'], label='Daily New Cases (lagged 14)', color='orange')
# ax[1].set_xlabel('Date')
# ax[1].set_ylabel('Daily New Cases (per Million)', color='orange')

ax[1].plot(USA_lagged_data['date'], USA_lagged_data['restriction_gatherings'], label='International Travel Controls', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('International Travel Controls', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('USA\'s Daily New Cases and International Travel Controls \n Over Time (7 days lagged)', fontsize=12)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# In[33]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(USA_lagged_data['date'], USA_lagged_data['lag_7_new_cases'], label='Daily New Cases (per Million)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

ax[1].plot(USA_lagged_data['date'], USA_lagged_data['workplace_closures'], label='Workplace Closures Category', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Workplace Closures', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('USA\'s Daily New Cases and Workplace Closures \n Over Time (7 days lagged)', fontsize=10)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# In[34]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(USA_lagged_data['date'], USA_lagged_data['lag_7_new_cases'], label='Daily New Cases (per Million)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

ax[1].plot(USA_lagged_data['date'], USA_lagged_data['school_closures'], label='School Closures Category', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('School Closures', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('USA\'s Daily New Cases and Workplace Closures \n Over Time (7 days lagged)', fontsize=10)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# ### SG's Daily New Cases and 5 Policy Indexes Over Time (with lag)

# In[36]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(SG_lagged_data['date'], SG_lagged_data['lag_7_new_cases'], label='Daily New Cases (lagged 7)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

ax[1].plot(SG_lagged_data['date'], SG_lagged_data['international_travel_controls'], label='International Travel Controls Category', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('International Travel Controls', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('SG\'s Daily New Cases and International Travel Controls \n Over Time (7 days lagged)', fontsize=9)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# In[37]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(SG_lagged_data['date'], SG_lagged_data['lag_7_new_cases'], label='Daily New Cases (lagged 7)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

ax[1].plot(SG_lagged_data['date'], SG_lagged_data['testing_policy'], label='Testing Policy Category', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Testing Policy', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('SG\'s Daily New Cases and Testing Policy \n Over Time (7 days lagged)', fontsize=10)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# In[38]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(SG_lagged_data['date'], SG_lagged_data['lag_7_new_cases'], label='Daily New Cases (lagged 7)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

ax[1].plot(SG_lagged_data['date'], SG_lagged_data['workplace_closures'], label='Workplace Closures Category', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Workplace Closures', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('SG\'s Daily New Cases and Workplace Closures \n Over Time (7 days lagged)', fontsize=10)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# In[39]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(SG_lagged_data['date'], SG_lagged_data['lag_7_new_cases'], label='Daily New Cases (lagged 7)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

ax[1].plot(SG_lagged_data['date'], SG_lagged_data['stay_home_requirements'], label='Stay Home Requirements Category', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Stay Home Requirements', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('SG\'s Daily New Cases and Stay Home Requirements \n Over Time (7 days lagged)', fontsize=10)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# In[40]:


fig, ax = plt.subplots(2, 1)

ax[0].plot(SG_lagged_data['date'], SG_lagged_data['lag_7_new_cases'], label='Daily New Cases (lagged 7)', color='g')
ax[0].set_xlabel('Date')
ax[0].set_ylabel('Daily New Cases (per Million)', color='g')

ax[1].plot(SG_lagged_data['date'], SG_lagged_data['cancel_public_events'], label='Cancel Public Events Category', color='b')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Cancel Public Events', color='b')
ax[1].set_ylim([0, 5])

fig.suptitle('SG\'s Daily New Cases and Cancel Public Events \n Over Time (7 days lagged)', fontsize=10)
fig.set_size_inches(10, 10)
fig.legend()
plt.show()


# ### Radar Chart for Policy Indexes of China, Singapore and USA

# In[42]:


import plotly.graph_objects as go
import numpy as np

categories = ['facial_coverings', 'international_travel_controls','school_closures','workplace_closures',
              'restrictions_internal_movements', 'testing_policy', 'stay_home_requirements',
              'cancel_public_events', 'restriction_gatherings']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[np.average(China_lagged_data['facial_coverings']), np.average(China_lagged_data['international_travel_controls']), 
         np.average(China_lagged_data['school_closures']), np.average(China_lagged_data['workplace_closures']), 
         np.average(China_lagged_data['restrictions_internal_movements']), np.average(China_lagged_data['testing_policy']),
         np.average(China_lagged_data['stay_home_requirements']), np.average(China_lagged_data['cancel_public_events']), 
         np.average(China_lagged_data['restriction_gatherings'])
        ],
      theta=categories,
      fill='toself',
      name='China Government Policy'
))

fig.add_trace(go.Scatterpolar(
      r=[np.average(SG_lagged_data['facial_coverings']), np.average(SG_lagged_data['international_travel_controls']), 
         np.average(SG_lagged_data['school_closures']), np.average(SG_lagged_data['workplace_closures']), 
         np.average(SG_lagged_data['restrictions_internal_movements']), np.average(SG_lagged_data['testing_policy']),
         np.average(SG_lagged_data['stay_home_requirements']), np.average(SG_lagged_data['cancel_public_events']), 
         np.average(SG_lagged_data['restriction_gatherings'])
        ],
      theta=categories,
      fill='toself',
      name='Singapore Government Policy'
))

fig.add_trace(go.Scatterpolar(
      r=[np.average(USA_lagged_data['facial_coverings']), np.average(USA_lagged_data['international_travel_controls']), 
         np.average(USA_lagged_data['school_closures']), np.average(USA_lagged_data['workplace_closures']), 
         np.average(USA_lagged_data['restrictions_internal_movements']), np.average(USA_lagged_data['testing_policy']),
         np.average(USA_lagged_data['stay_home_requirements']), np.average(USA_lagged_data['cancel_public_events']), 
         np.average(USA_lagged_data['restriction_gatherings'])
        ],
      theta=categories,
      fill='toself',
      name='USA Government Policy'
))


fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=True,
  title='Radar Chart for Policy Indexes of China, Singapore and USA'
)

fig.show()


# In[ ]:




