import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('dirtydata2 (1).csv')
df1 =pd.DataFrame(df)

print(df)

df.dropna(inplace = True)
df.drop_duplicates(inplace = True)
df['Date'] = pd.to_datetime(df['Date'])

mean_Duration = df['Duration'].median()
mean_Pulse = df['Pulse'].median()
mean_MaxPulse = df['Maxpulse'].median()
mean_Calories = df['Calories'].median()


filter_data = df['Date'].isnull()

filter_Duration = df['Duration'] >=2*mean_Duration
filter_Pulse = df['Pulse']>= 2*mean_Pulse
filter_Pulse1 = df['Pulse']<=mean_Pulse/2
filter_MaxPulse = df['Maxpulse']>= 2*mean_MaxPulse
filter_Calories = df['Calories']>= 2*mean_Calories


df.loc[filter_Duration==True,'Duration'] = mean_Duration
df.loc[filter_Pulse==True,'Pulse'] = mean_Pulse
df.loc[filter_Pulse1==True,'Pulse'] = mean_Pulse
df.loc[filter_MaxPulse==True,'Maxpulse'] = mean_MaxPulse
df.loc[filter_Calories==True,'Calories'] = mean_Calories


df['Duration'].fillna(mean_Duration, inplace = True)
df['Pulse'].fillna(mean_Pulse, inplace = True)
df['Maxpulse'].fillna(mean_MaxPulse, inplace = True)
df['Calories'].fillna(mean_Calories, inplace = True)




print(df)
