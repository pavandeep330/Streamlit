import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:/Users/Pavan Deep/Desktop/ipl_data/IPL Ball-by-Ball 2008-2020.csv")
df = pd.DataFrame(data, index = None)
#toss_importance = df.loc[df['toss_winner']==df['winner']]
#print(df.count())
full_dhoni = df.loc[(df["batsman"]=="MS Dhoni")]
raina_df = df.loc[(df["batsman"]=="MS Dhoni") & (df['batsman_runs']==6)]
ballsperboundary_df = df.loc[(df["batsman"]=="MS Dhoni")&(df['batsman_runs']==4)]
#total = raina_df['batsman_runs'].sum()
#print(total)
print(raina_df['batsman_runs'].count())
#toss_decision = toss_importance.loc[toss_importance['toss_decision']=="field"]
#print(toss_decision.count())
#mostwins_in_season = df.loc[(df['date']<"2021-01-25") & (df['date']>"2020-01-25")]
#print(mostwins_in_season['winner'].value_counts())
#print(df['city'].value_counts())
#bravo_df = df.loc[(df['bowler']=="DJ Bravo") & (df['extras_type']=="wides")]
#print(bravo_df.count())
#malinga_df = df.loc[(df['bowler']=="SL Malinga") & (df['extras_type']=="wides")]
#print(malinga_df.count())
#wides_df = df.loc[df['winner']=="Kolkata Knight Riders"]
#print(wides_df['bowler'].value_counts())
line = df.head(10)
#print(line.count())
count = 0
sum = 0
list = []
for x in full_dhoni['batsman_runs']:
    if (x<4):
        count = count + 1
    if(x>=4):
        list.append(count)
        sum = sum + count
        count = 0
avg_balls_for_boundary = sum/len(list)


print(df.count())
full_bowler = df.loc[(df["bowler"]=="Imran Tahir")]
count = 0
sum = 0
list = []
for x in full_bowler['is_wicket']:
    if (x==0):
        count = count + 1
    if(x==1):
        list.append(count)
        sum = sum + count
        count = 0
strike_rate = sum/len(list)
print(strike_rate)

total_wickets = df.loc[(df["bowler"]=="R Ashwin") & (df['is_wicket']==1) &(df['dismissal_kind']!="run out")]
print(total_wickets.count())
    










