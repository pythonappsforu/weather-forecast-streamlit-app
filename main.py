import streamlit as st
import plotly.express as px
from api_processor import get_data


st.title("Weather Forecast for the Next Days")
place = st.text_input(label='Place')
days = st.slider(label='Forecast Days',min_value=1,max_value=5,
                 step=1,help='select no of forecasted days')
option = st.selectbox('Select data to view',
                      ('Temperature','Sky'))

st.subheader(f'{option} for the next {days} days in {place}')

if place:
    filtered_data,status = get_data(place,days)
    if status == "200":
        if option == "Temperature":
            temp_list = [data['main']['temp']-273.15 for data in filtered_data]
            dates = [data['dt_txt'] for data in filtered_data]
            figure = px.line(x=dates, y=temp_list,
                             labels={'x': 'Dates', 'y': 'temp'})
            st.plotly_chart(figure)

        elif option == "Sky":
            sky_list = [data['weather'][0]['main'] for data in filtered_data]

            filepaths = [f'images/{sky.lower()}.png' for sky in sky_list]
            st.image(filepaths,width=115)


    else:
        st.info(filtered_data)
