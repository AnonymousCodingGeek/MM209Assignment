# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None

df=pd.read_csv("MM209_Project - Sheet1.csv")

df

#Code to add new metal
#User can uncomment the below line and add a new metal to the above existing data frame after 
#entering the required values
#df.loc[len(df.index)] =[Metal,Metal Oxide,DeltaH0,DeltaS0,Slope change T,New DeltaH0,New DeltaS0]

#Data for formation of water from H2 and 02
#2H2 + 02=2H20
DeltaH0=-495*1000
DeltaS0=-0.11*1000

#Accepting the temperature value
T=input("Enter the temperature: ")

#Calculation of equilibrium constant for the reaction 2H2 + O2= 2H20
T=int(T)
DeltaG0= DeltaH0 -T * DeltaS0
Kc=np.exp(-DeltaG0/(8.314*T))

df1=df[df['Slope change T'].isnull()] #DataFrame for metals with a linear DeltaG0
df2=df[~(df['Slope change T'].isnull())]#DataFrame for metals with a DeltaG0 whose slope changes
df1['DeltaG0']=df1['DeltaH0']-T*df1['DeltaS0']
df1.dropna(axis=1,inplace=True)
df2['DeltaG0']=0
for ind in df2.index:
    if T>=df2['Slope change T'][ind]:
        df2['DeltaG0'][ind]=df2['New DeltaH0'][ind]-T*df2['New DeltaS0'][ind]
    else:
        df2['DeltaG0'][ind]=df2['DeltaH0'][ind]-T*df2['DeltaS0'][ind]

df1['Kc']=np.exp(-df1['DeltaG0']*1000/(8.314*T))
df2['Kc']=np.exp(-df2['DeltaG0']*1000/(8.314*T))
#Kc=1/p02
df1['p02']=1/(df1['Kc'])
df2['p02']=1/(df2['Kc'])

#Kc for water formation = ((pH20/pH2)^2)/p02
df1['pH20/pH2']=np.sqrt(Kc*df1['p02'])
df2['pH20/pH2']=np.sqrt(Kc*df2['p02'])
df1['ln(pH20/pH2)']=np.log(np.sqrt(Kc*df1['p02']))
df2['ln(pH20/pH2)']=np.log(np.sqrt(Kc*df2['p02']))

#Final DataFrame for the first group of metals
df1

#Final Dataframe for the second group of metals
df2

#Joining the 2 we get our final dataframe which contains all the values
df3=pd.concat([df1.drop(['DeltaH0','DeltaS0'],axis=1),df2.drop(['DeltaH0','DeltaS0','Slope change T','New DeltaH0','New DeltaS0'],axis=1)])
df3.sort_index(inplace=True)
df3

#Dataframe showing the pH20/pH2 values clearly
df3[['Metal','Metal Oxide','pH20/pH2','ln(pH20/pH2)']]

from lets_plot import *
ggplot(df3) + geom_bar(aes(fill="pH20/pH2", x="Metal", y="pH20/pH2"), stat='identity')

from lets_plot import *
ggplot(df3) + geom_bar(aes(fill="ln(pH20/pH2)", x="Metal", y="ln(pH20/pH2)"), stat='identity')

from lets_plot import *
ggplot(df3) + geom_line(aes(color="ln(pH20/pH2)", x="Metal", y="ln(pH20/pH2)"))

