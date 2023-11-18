import streamlit as st


st.title("Weather Forecast for the Next Days")
place = st.text_input(label='Place')
days = st.slider(label='Forecast Days',min_value=1,max_value=5,
                 step=1,help='select no of forecasted days')
option = st.selectbox('Select data to view',
                      ('Temperature','Sky'))

st.subheader(f'{option} for the next {days} days in {place}')