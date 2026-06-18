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
    df = pd.DataFrame(data, columns=["City", "Country", "Day Temperature, F", "Night Temperature, F", 'Wind Speed, mph', 'Wind Direction', 'Humidity', 'Pressure'])
   

 



st.title('Weather Dashboard')
selected_country = st.selectbox('Choose the country', df['Country'])
filtered_df = df[df['Country'] == selected_country]
column_data = filtered_df.drop('Country', axis=1)
st.dataframe(column_data, hide_index=True)
# st.write(column_data)

#col1, col2 = st.columns(2)
#with col1:
#     st.metric('Sales', f'${filtered_df['Sales'].values[0]:,}')
# with col2:
#     st.metric('Profit', f'${filtered_df['Profit'].values[0]:,}')

st.subheader("Tempreture across cities")
bar_chart = px.bar(filtered_df, x='City', y=['Day Temperature, F', 'Night Temperature, F'], barmode='group', color_discrete_sequence=['orange', 'blue'])
st.plotly_chart(bar_chart)

