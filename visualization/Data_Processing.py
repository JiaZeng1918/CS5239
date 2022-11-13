#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import plotly
import seaborn as sns
covid_data = pd.read_csv('owid-covid-data.csv')


# In[ ]:


chn_data['date'] = pd.to_datetime(chn_data['date'])
sg_data['date'] = pd.to_datetime(sg_data['date'])
usa_data['date'] = pd.to_datetime(usa_data['date'])

chn_data = chn_data.drop('index', axis=1)
sg_data = sg_data.drop('index', axis=1)
usa_data = usa_data.drop('index', axis=1)


# In[ ]:


chn_data = chn_data[(chn_data['date']>= '2020-01-23') & (chn_data['date']<= '2022-09-30')].reset_index()
sg_data = sg_data[(sg_data['date']>= '2020-01-23') & (sg_data['date']<= '2022-09-30')].reset_index()
usa_data = usa_data[(usa_data['date']>= '2020-01-23') & (usa_data['date']<= '2022-09-30')].reset_index()


# In[ ]:


testing_policy = pd.read_csv('covid-19-testing-policy.csv')
contact_tracing = pd.read_csv('covid-contact-tracing.csv')
face_covering = pd.read_csv('face-covering-policies-covid.csv')
internal_movement = pd.read_csv('internal-movement-covid.csv')
international_travel = pd.read_csv('international-travel-covid.csv')
public_events = pd.read_csv('public-events-covid.csv')
public_gathering = pd.read_csv('public-gathering-rules-covid.csv')
school_closure = pd.read_csv('school-closures-covid.csv')
workplace_closure = pd.read_csv('workplace-closures-covid.csv')
stay_home = pd.read_csv('stay-at-home-covid.csv')


# In[ ]:


testing_policy['Day'] = pd.to_datetime(testing_policy['Day'])
contact_tracing['Day'] = pd.to_datetime(contact_tracing['Day'])
face_covering['Day'] = pd.to_datetime(face_covering['Day'])
internal_movement['Day'] = pd.to_datetime(internal_movement['Day'])
international_travel['Day'] = pd.to_datetime(international_travel['Day'])
public_events['Day'] = pd.to_datetime(public_events['Day'])
public_gathering['Day'] = pd.to_datetime(public_gathering['Day'])
school_closure['Day'] = pd.to_datetime(school_closure['Day'])
workplace_closure['Day'] = pd.to_datetime(workplace_closure['Day'])
stay_home['Day'] = pd.to_datetime(stay_home['Day'])


# In[ ]:


testing_policy = testing_policy[(testing_policy['Day']>= '2020-01-23') & (testing_policy['Day']<= '2022-09-30')]
contact_tracing = contact_tracing[(contact_tracing['Day']>= '2020-01-23') & (contact_tracing['Day']<= '2022-09-30')]
face_covering = face_covering[(face_covering['Day']>= '2020-01-23') & (face_covering['Day']<= '2022-09-30')]
internal_movement = internal_movement[(internal_movement['Day']>= '2020-01-23') & (internal_movement['Day']<= '2022-09-30')]
international_travel = international_travel[(international_travel['Day']>= '2020-01-23') & (international_travel['Day']<= '2022-09-30')]
public_events = public_events[(public_events['Day']>= '2020-01-23') & (public_events['Day']<= '2022-09-30')]
public_gathering = public_gathering[(public_gathering['Day']>= '2020-01-23') & (public_gathering['Day']<= '2022-09-30')]
school_closure = school_closure[(school_closure['Day']>= '2020-01-23') & (school_closure['Day']<= '2022-09-30')]
workplace_closure = workplace_closure[(workplace_closure['Day']>= '2020-01-23') & (workplace_closure['Day']<= '2022-09-30')]
stay_home = stay_home[(stay_home['Day']>= '2020-01-23') & (stay_home['Day']<= '2022-09-30')]


# In[ ]:


df_list = [testing_policy, contact_tracing, face_covering, internal_movement, international_travel,
          public_events, public_gathering, school_closure, workplace_closure, stay_home]

feature_list = ['testing_policy', 'contact_tracing', 'facial_coverings', 'restrictions_internal_movements', 
                'international_travel_controls','cancel_public_events', 'restriction_gatherings', 'school_closures', 
                'workplace_closures', 'stay_home_requirements']

for x in range(10):
    df = df_list[x]
    chn_data[feature_list[x]] = df[df['Entity'] == 'China'].reset_index()[feature_list[x]]
    sg_data[feature_list[x]] = df[df['Entity'] == 'Singapore'].reset_index()[feature_list[x]]
    usa_data[feature_list[x]] = df[df['Entity'] == 'United States'].reset_index()[feature_list[x]]


# In[ ]:


population = chn_data[chn_data['date']=='2020-05-03']['population'].values[0]
print(population)
chn_data.loc[101,'new_cases_per_million'] = round((5/population)*1000000, 3)
chn_data.loc[102,'new_cases_per_million'] = round((7/population)*1000000, 3)


# In[ ]:


diff = chn_data.loc[85,'total_deaths_per_million'] - chn_data.loc[84,'total_deaths_per_million']
chn_data.loc[85,'new_deaths_per_million'] = 0 if diff < 0 else diff

diff = chn_data.loc[548,'total_deaths_per_million'] - chn_data.loc[547,'total_deaths_per_million']
chn_data.loc[548,'new_deaths_per_million'] = 0 if diff < 0 else diff

diff = chn_data.loc[818,'total_deaths_per_million'] - chn_data.loc[817,'total_deaths_per_million']
chn_data.loc[818,'new_deaths_per_million'] = 0 if diff < 0 else diff


# In[ ]:


sg_data.fillna({'total_deaths_per_million':0, 'new_deaths_per_million':0}, inplace=True)


# In[ ]:


diff = usa_data.loc[889,'total_deaths_per_million'] - usa_data.loc[888,'total_deaths_per_million']
usa_data.loc[889,'new_deaths_per_million'] = 0 if diff < 0 else diff

diff = usa_data.loc[942,'total_deaths_per_million'] - usa_data.loc[941,'total_deaths_per_million']
usa_data.loc[942,'new_deaths_per_million'] = 0 if diff < 0 else diff


# In[ ]:


usa_data.fillna({'total_deaths_per_million':0, 'new_deaths_per_million':0}, inplace=True)


# In[ ]:


chn_data = chn_data.drop('index', axis=1)
sg_data = sg_data.drop('index', axis=1)
usa_data = usa_data.drop('index', axis=1)


# In[ ]:


chn_data = chn_data.drop('people_vaccinated_per_hundred', axis=1)
sg_data = sg_data.drop('people_vaccinated_per_hundred', axis=1)
usa_data = usa_data.drop('people_vaccinated_per_hundred', axis=1)


# In[ ]:


chn_data = chn_data.drop('people_fully_vaccinated_per_hundred', axis=1)
sg_data = sg_data.drop('people_fully_vaccinated_per_hundred', axis=1)
usa_data = usa_data.drop('people_fully_vaccinated_per_hundred', axis=1)


# In[ ]:


chn_data = chn_data.drop('population', axis=1)
sg_data = sg_data.drop('population', axis=1)
usa_data = usa_data.drop('population', axis=1)


# In[ ]:


chn_data.to_csv('China_data.csv',header=True, index=False)
sg_data.to_csv('SG_data.csv',header=True, index=False)
usa_data.to_csv('USA_data.csv',header=True, index=False)


# In[ ]:


chn_data['lag_7_new_cases'] = chn_data.new_cases_per_million.shift(-7)
chn_data['lag_7_death_cases'] = chn_data.new_deaths_per_million.shift(-7)
chn_data['lag_14_new_cases'] = chn_data.new_cases_per_million.shift(-14)
chn_data['lag_14_death_cases'] = chn_data.new_deaths_per_million.shift(-14)


# In[ ]:


sg_data['lag_7_new_cases'] = sg_data.new_cases_per_million.shift(-7)
sg_data['lag_7_death_cases'] = sg_data.new_deaths_per_million.shift(-7)
sg_data['lag_14_new_cases'] = sg_data.new_cases_per_million.shift(-14)
sg_data['lag_14_death_cases'] = sg_data.new_deaths_per_million.shift(-14)


# In[ ]:


usa_data['lag_7_new_cases'] = usa_data.new_cases_per_million.shift(-7)
usa_data['lag_7_death_cases'] = usa_data.new_deaths_per_million.shift(-7)
usa_data['lag_14_new_cases'] = usa_data.new_cases_per_million.shift(-14)
usa_data['lag_14_death_cases'] = usa_data.new_deaths_per_million.shift(-14)


# In[ ]:


chn_data.to_csv('China_lagged_data.csv',header=True, index=False)
sg_data.to_csv('SG_lagged_data.csv',header=True, index=False)
usa_data.to_csv('USA_lagged_data.csv',header=True, index=False)

