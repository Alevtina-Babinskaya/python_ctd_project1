import streamlit as st  
import pandas as pd     
import numpy as np      
import plotly.express as px
import sqlite3  

with sqlite3.connect("weather_data.db") as conn:
    cursor = conn.cursor()
    query = """SELECT city, country, day_temp, night_temp, wind_speed, wind_direction, humidity, pressure FROM Weather"""
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["city", "country", "day_temp", "night_temp", 'wind_speed', 'wind_dir', 'humidity', 'pressure'])
    cursor.execute("""SELECT country, (city || ', '|| country) AS location, (day_temp || '/' || night_temp) AS temperature, (wind_speed || ' ' || wind_direction) AS wind, humidity FROM Weather""")
    data_to_show = cursor.fetchall()
    df_show = pd.DataFrame(data_to_show, columns=['country', 'Location', 'Temperature, F', 'Wind', 'Humidity'])
   

 



st.title('Weather Dashboard')
st.subheader("Humidity and Day Temperature in Different Cities")

hum_temp_chart = px.scatter(df, x='humidity', y='day_temp', color='country', title='Humidity and Day Temperature', labels={'humidity':'Humidity, %', 'day_temp':"Day Temperature,°F"})
st.plotly_chart(hum_temp_chart)

st.subheader("Wind speed and direction")
wind_chart = px.bar(
    df,
    x='wind_dir',
    y='wind_speed',
    color='wind_dir',
    title='Wind Speed by Direction',
    labels={
        'wind_dir': 'Wind Direction',
        'wind_speed': 'Wind Speed (mph)'
    }
)
st.plotly_chart(wind_chart)

selected_country = st.selectbox('Choose the country', df['country'])
filtered_df = df[df['country'] == selected_country]
filtered_df_show = df_show[df_show['country'] == selected_country]
st.dataframe(filtered_df_show[['Location', 'Temperature, F', 'Wind', 'Humidity']], hide_index=True)

st.subheader("Tempreture across cities")
bar_chart = px.bar(filtered_df, x='city', y=['day_temp', 'night_temp'], barmode='group', color_discrete_sequence=['orange', 'blue'], 
                   labels={'city': 'Cities', 'value': 'Temperature, °F'})
st.plotly_chart(bar_chart)


