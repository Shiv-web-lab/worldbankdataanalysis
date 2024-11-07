#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "education_data_set.csv"
data = pd.read_csv(file_path)



# In[5]:


# Display the first few rows to understand the structure
data.head()


# In[6]:


# Check for missing values
missing_values = data.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Optionally, fill or drop missing values
data = data.fillna(method='ffill')  # Forward fill missing values as an example

# Verify data types
data.info()


# In[7]:


# Display summary statistics
data.describe()

# Calculate correlations between years
correlations = data.iloc[:, 1:].corr()
correlations


# In[18]:


import matplotlib.pyplot as plt

def plot_histogram(year):
    plt.figure(figsize=(10, 6))
    plt.hist(data[year].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of Education Data for {year}')
    plt.xlabel('Education Data')
    plt.ylabel('Frequency')
    plt.show()
plot_histogram('2010')   


# In[12]:


def plot_bar_chart():
    country_means = data.set_index('Country Name').mean(axis=1)
    
    plt.figure(figsize=(12, 6))
    country_means.plot(kind='bar', color='coral')
    plt.title('Average Education Data by Country (2010-2021)')
    plt.xlabel('Country')
    plt.ylabel('Average Education Data')
    plt.xticks(rotation=90)
    plt.show()


# In[19]:


def plot_line(country_name):
    years = data.columns[1:]
    values = data[data['Country Name'] == country_name].iloc[0, 1:]
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, values, marker='o', color='green')
    plt.title(f'Education Data Trend for {country_name} (2010-2021)')
    plt.xlabel('Year')
    plt.ylabel('Education Data')
    plt.grid()
    plt.show()
plot_bar_chart()


# In[20]:


def plot_scatter(year1, year2):
    plt.figure(figsize=(8, 6))
    plt.scatter(data[year1], data[year2], color='purple', alpha=0.6)
    plt.title(f'Scatter Plot of Education Data: {year1} vs. {year2}')
    plt.xlabel(f'Education Data {year1}')
    plt.ylabel(f'Education Data {year2}')
    plt.grid(True)
    plt.show()
plot_line('Afghanistan')


# In[21]:


def plot_heatmap():
    correlations = data.iloc[:, 1:].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlations, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap of Education Data (2010-2021)')
    plt.show()
plot_heatmap()


# In[22]:


def plot_box():
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data.iloc[:, 1:], palette='Set2')
    plt.title('Box Plot of Education Data Across Years')
    plt.xlabel('Year')
    plt.ylabel('Education Data')
    plt.show()
plot_box()


# In[ ]:




