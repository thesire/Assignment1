#!/usr/bin/env python
# coding: utf-8

# In[28]:


get_ipython().system('pip install plotly')


# In[29]:


import pandas as pd
import numpy as np


# In[30]:


unemployment_2019= pd.read_csv(r"C:\Users\CHIDERA NWOSU\Videos\Unemployment.csv")
unemployment_2019.head()


# In[31]:


import plotly


# In[32]:


import plotly.io as pio
import plotly.express as px
import plotly.graph_objs as go


# In[33]:


fig=px.bar(unemployment_2019, y = 'Unemployment Rates', x= 'State', orientation = 'v', color = 'Unemployment Rates')
fig.update_layout(uniformtext_minsize = 10, uniformtext_mode='hide')
fig.update_layout(
    title = {
        'text' : "THE UNEMPLOYMENT RATE, Q4 2020",
        'y':0.85,
        'x':0.45,
        'xanchor':'center',
        'yanchor':'top'},
    height = 900, width = 900)


# In[34]:


import json
import plotly.express as px


# In[35]:


with open (r"C:\Users\CHIDERA NWOSU\Documents\NBS_states.geojson") as f:
    geo_data = json.load(f)


# In[36]:


state_id_map={}
for feature in geo_data['features']:
    feature['id']=feature['properties']['OBJECTID']
    state_id_map[feature['properties']['OBJECTID']]= feature['id']


# In[37]:


nigeria_coordinates = {"lat": 9.0820, "lon":8.6753}


# In[38]:


fig = px.choropleth_mapbox(
    unemployment_2019,
    geojson= geo_data,
    locations= "State_No",
    color = "Unemployment Rates",
    center = nigeria_coordinates,
    zoom = 5,
    opacity = 0.5,
    hover_name="State",
    color_continuous_scale="agsunset",
    mapbox_style="carto-positron",
    labels = {"State_No":"UNEMPLOYMENT RATE"}
    
)
fig.update_layout(margin={"t":0,"b":0,"l":0,"r":0})
fig.show()


# In[ ]:




