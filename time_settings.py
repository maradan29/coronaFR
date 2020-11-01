#!/usr/bin/env python
# coding: utf-8

# In[18]:


from datetime import datetime, date, time, timedelta


# In[19]:


today = date.today()
today = today.strftime("%Y-%m-%d")
quatorze_jours = date.today() - timedelta(days=30)
quatorze_jours = quatorze_jours.strftime("%Y-%m-%d")


# In[20]:


annee = date.today()
annee = annee.strftime("%Y")
mois = date.today()
mois = mois.strftime("%m")
jour = date.today()
jour = jour.strftime("%y%m%d")


# In[21]:


annee


# In[22]:


mois


# In[23]:


jour


# In[24]:


file_url = 'https://www.fr.ch/sites/default/files/' + annee + '-' + mois + '/' + jour + '_statistiques_situation_COVID_site_V2.xlsx'

