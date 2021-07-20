import streamlit as st
from streamlit import *
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from PIL import Image
st.title("IPL Analytics")
image = Image.open(r'C:\Users\Pavan Deep\Desktop\html\ipl.jpg')
st.image(image)
st.markdown("The Indian Premier League (IPL) is a professional Twenty20 cricket league played in India")
st.sidebar.title("Visualization Selector")

def load_data():
    data=pd.read_csv(r"C:\Users\Pavan Deep\Desktop\ipl_data\IPL Matches 2008-2020.csv")
    return data

matches_df=load_data()
def load_data():
    data=pd.read_csv(r"C:\Users\Pavan Deep\Desktop\ipl_data\IPL Ball-by-Ball 2008-2020.csv")
    return data

ball2ball_df=load_data()
toss_importance = matches_df.loc[matches_df['toss_winner']==matches_df['winner']]
toss_decision = toss_importance.loc[toss_importance['toss_decision']=="field"]
if st.sidebar.button('Toss importance'):
    st.write('51.3% of the matches , team that wins the toss , wins the match')
#st.write("the number of times , a team that won the toss , won the match is :")
a = toss_importance['winner'].count()

#st.write("the number of times , a team that won the toss , choose to bat and won the match is :")
b = toss_decision['winner'].count()

#st.write("the number of times , a team that won the toss ,choose to bowl and won the match is :")
c = a-b


if st.sidebar.button('Toss decision importance'):
    st.write("57.3% of the matches , team that wins the toss , wins the match")




#first option
select = st.sidebar.selectbox('Select a Team',matches_df['winner'].unique())
#get the state selected in the selectbox
team_data = matches_df[matches_df['winner'] == select]
new = team_data[['toss_winner','toss_decision','winner', 'player_of_match','result_margin']].copy()
st.subheader('Toss-win relational dataframe')
st.dataframe(new)

bar_data = team_data[:30]
st.subheader('winning margin ')
#Bar Chart
st.bar_chart(bar_data['result_margin'])
#line chart
df = pd.DataFrame(matches_df[:200], columns = ["result_margin"])
st.line_chart(df)

wides_df = ball2ball_df.loc[(ball2ball_df['bowling_team']==select) & (ball2ball_df['extras_type']=="wides")]
line = wides_df.head(20)
st.bar_chart(line['total_runs'])
st.sidebar.title("select batsman and bowler")
select1 = st.sidebar.selectbox('Select a batsman',ball2ball_df['batsman'].unique())
select2 = st.sidebar.selectbox('Select a bowler',ball2ball_df['bowler'].unique())
#get the state selected in the selectbox
raina_df = ball2ball_df.loc[(ball2ball_df["batsman"]==select1) & (ball2ball_df['bowler']==select2)]
wickets_df = ball2ball_df.loc[(ball2ball_df["batsman"]==select1) & (ball2ball_df['bowler']==select2) & (ball2ball_df['is_wicket']==1)]
total = raina_df['batsman_runs'].sum()
sixes_df = raina_df.loc[raina_df['batsman_runs']==6]
shepherd = select2
fours_df = raina_df.loc[raina_df['batsman_runs']==4]
string_in_string = "sixes hit against {}.".format(shepherd)
#st.write(string_in_string)
sixes = sixes_df['batsman_runs'].count()
#st.button(label=string_in_string, key=None, help=None)
st.title("batsman and bowler stats")
if st.button(string_in_string):
    st.write(str(sixes))
string_in_string = "fours hit against {}.".format(shepherd)
fours = fours_df['batsman_runs'].count()
if st.button(string_in_string):
    st.write(str(fours))
#st.write(string_in_string)
#st.write(fours_df['batsman_runs'].count())
shepherd = select2
string_in_string = "total runs scored against {}.".format(shepherd)
if st.button(string_in_string):
    st.write(str(total))
#st.write(string_in_string)
#st.write(total, width=300,height = 300)
string_in_string = "outs against {}.".format(shepherd)
wickets = wickets_df['batsman_runs'].count()
if st.button(string_in_string):
    st.write(str(wickets))

st.sidebar.title("boundary stats")
select3 = st.sidebar.selectbox('Select batsman',ball2ball_df['batsman'].unique())

ballsperboundary1_df = ball2ball_df.loc[(ball2ball_df["batsman"]==select3)&(ball2ball_df['batsman_runs']==6)]
ballsperboundary2_df = ball2ball_df.loc[(ball2ball_df["batsman"]==select3)&(ball2ball_df['batsman_runs']==4)]
shepherd1 = select3
string_in_string = "total boundaries scored{}.".format(shepherd1)
boundaries = ballsperboundary1_df['batsman_runs'].count() + ballsperboundary2_df['batsman_runs'].count()
st.title("boundary stats")
if st.button(string_in_string):
    st.write(str(boundaries))

st.sidebar.title("Balls per boundary")
select4 = st.sidebar.selectbox('batsman',ball2ball_df['batsman'].unique())

individual = ball2ball_df.loc[ball2ball_df['batsman']==select4]
count = 0
sum = 0
list = []
for x in individual['batsman_runs']:
    if (x<4):
        count = count + 1
    if(x>=4):
        list.append(count)
        sum = sum + count
        count = 0
avg_balls_for_boundary = sum/len(list)
st.title("Balls per boundary")
if st.button("balls per boundary"):
    st.write(str(avg_balls_for_boundary))

st.sidebar.title("bowler's strike rate")
select5 = st.sidebar.selectbox('bowler',ball2ball_df['bowler'].unique())

