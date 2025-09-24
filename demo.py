import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder

df=pd.read_csv(r'C:/Users/Manisha/OneDrive/Desktop/Projects/zomato.csv')
df.sample(10)
#to get the information about the dataset like no of rows,columns,datatypes and memory usage
df.info()
#to check for missing values
df.isna().sum()
df.dropna(subset=['Cuisines'],inplace=True)
#to check for duplicates
df.duplicated().sum()

#dropping unnecessary columns
df.drop(['Address','Is delivering now','Switch to order menu'],axis=1,inplace=True)
#making the unique column as index for easy access
df.set_index('Restaurant ID',inplace=True)
#checking for unique values in each column
def uniqueness(column):
    print(df[column].value_counts())
uniqueness(df.columns)

#Ordinal Encoding

cols=['Restaurant Name','Country Code','City','Locality','Locality Verbose','Cuisines','Rating color','Rating text','Has Table booking','Has Online delivery']
scale=OrdinalEncoder()
df[cols]=scale.fit_transform(df[cols])

#checking correlation
df[cols].corr()
#Visualization

plt.figure(figsize=(10,10))
sns.heatmap(df[cols].corr(),annot=True)

fig = px.scatter_mapbox(
    df.reset_index(),
    lat="Latitude",
    lon="Longitude",
    hover_name="Restaurant ID",
    mapbox_style="open-street-map",
    zoom=10,
    height=600
)
fig.show()

fig = px.sunburst(df, path=['Country Code', 'City', 'Restaurant Name'], values='Votes')
fig.show()

fig = px.scatter(df.reset_index(), x="Longitude", y="Latitude", hover_name="Restaurant ID", size="Votes",  title="Restaurant Locations")
fig.show()
