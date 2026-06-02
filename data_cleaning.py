import pandas as pd

weather_df = pd.read_csv('weather_data.csv')
weather_df['Location'] = weather_df['Location'].str.replace('Weather in ', '') # remove Weather in
weather_df['Temperature'] = weather_df['Temperature'].str.replace('Forecast:', '') # leave only digits with /
weather_df['Temperature'] = weather_df['Temperature'].str.replace('°F', '')
weather_df['Day Temperature, °F'] = weather_df['Temperature'].str.split("/").str[0].str.strip() # split tempreture into to data columns for day and night
weather_df['Night Temperature, °F'] = weather_df['Temperature'].str.split("/").str[1].str.strip()
weather_df['Day Temperature, °F'] = weather_df['Day Temperature, °F'].astype(int)
weather_df['Night Temperature, °F'] = weather_df['Night Temperature, °F'].astype(int) #make columns integer
weather_df['Description'] = weather_df['Description'].replace('.', '')
weather_df['Wind'] = weather_df['Wind'].str.replace(' ↑ ', ', ')
weather_df['Wind speed, mph'] = weather_df['Wind'].str.split(",").str[0].str.strip() # split wind into to data columns for speed and direction
weather_df['Wind direction'] = weather_df['Wind'].str.split(",").str[1].str.strip()
weather_df['Wind speed, mph'] = weather_df['Wind speed, mph'].str.replace("mph", '').str.strip()
weather_df['Wind speed, mph'] = weather_df['Wind speed, mph'].replace({'No wind': 0})
weather_df['Wind speed, mph'] = weather_df['Wind speed, mph'].astype(float)
weather_df = weather_df.drop(columns=['Temperature','Wind'])
#weather_df['Date'] = pd.to_datetime(weather_df['Date'], errors='coerce')
weather_df['Visibility'] = weather_df['Visibility'].str.replace('mi', '')
weather_df['Pressure'] = weather_df['Pressure'].str.replace('"Hg', '')
weather_df['Humidity'] = weather_df['Humidity'].str.replace('%', '')
weather_df['Dew point'] = weather_df['Dew point'].str.replace('°F', '')
print(weather_df)