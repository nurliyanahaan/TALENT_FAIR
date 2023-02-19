import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import time
from plotly import graph_objs as go
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
import base64

# ---- Config & setting page icon and title ----
app_icon = Image.open("logo.png")
st.set_page_config(page_title="Sales Forecasting", page_icon=app_icon, layout="centered")

# ---- Hiding the menu and streamlit footer note ----
hide_menu = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_menu, unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('2.jpg') 


# ---- Setting the header and tagline -----

st.markdown("<h1 style='text-align: center;'>--Sales Forecasting-- </h1>", unsafe_allow_html=True)



with st.form(key='form1'):

        st.markdown("<h4 style='text-align: left;'>Please Select The Category and Product You Want to Predict </h4>", unsafe_allow_html=True)

        option = st.selectbox(
        'Category-Product',
        ('A-A1', 'A-A2', 'B-B1','B-B2'))

        submit_button = st.form_submit_button(label = "Find Out")
if submit_button:
        # --- showing progress bar ---
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i+1)

        
        st.success(option)
        st.write('Your option is: ', option, '. Here you go ! The Sales Forcasting of the selected Category and Product:')

# ---- RESULTS CONDITION ----
if option == "A-A1": 
    
    forecast_A1 = pd.read_csv('data/Forecast A1.csv')
    
    st.markdown("<h4 style='text-align: center;'>Sales Forcasting Up To 14 Days - Category A Product A1</h4>", unsafe_allow_html=True)
    fig = go.Figure(
            data = go.Scatter(
                x = forecast_A1['Day'],
                y = forecast_A1['Sales'],
                name = "Forecast ARIMA"
                ))
    fig.layout.update(title_text="Sales Forecast", xaxis_rangeslider_visible=True, yaxis_title='Sales',xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("Please move the cursor towards the chart to see detailed data or you can drag the pointer on the day section. Details provide in table below.")
    st.markdown("<h5 style='text-align: left;'>Forecast Details :</h5>", unsafe_allow_html=True)
    
    gd = GridOptionsBuilder.from_dataframe(forecast_A1)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(forecast_A1, gridOptions=gridoption, height=250, reload_data=True)



    data_A1 = pd.read_csv('data/Data A1.csv')
    st.markdown("<h4 style='text-align: center;'> Data History - Category A Product A1</h4>", unsafe_allow_html=True)
    fig = go.Figure(
                data = go.Scatter(
                    x = data_A1['Day'],
                    y = data_A1['Sales'],
                    name = "Forecast ARIMA"
                    ))
    fig.layout.update(title_text="Data History", xaxis_rangeslider_visible=True, yaxis_title='Sales', xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("Please move the cursor towards the chart to see detailed data or you can drag the pointer on the day section. Details provide in table below.")
    st.markdown("<h5 style='text-align: left;'>History Details :</h5>", unsafe_allow_html=True)
    gd = GridOptionsBuilder.from_dataframe(data_A1)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(data_A1, gridOptions=gridoption, height=250, reload_data=True)
    st.write("History details are available in the last 90 days.")

#========================================================================

if option == "A-A2": 

    forecast_A2 = pd.read_csv('data/Forecast A2.csv')
    
    st.markdown("<h4 style='text-align: center;'>Sales Forcasting Up To 14 Days - Category A Product A2</h4>", unsafe_allow_html=True)
    fig = go.Figure(
            data = go.Scatter(
                x = forecast_A2['Day'],
                y = forecast_A2['Sales'],
                name = "Forecast ARIMA",
                line = {'color': 'green'}))
    fig.layout.update(title_text="Sales Forecast", xaxis_rangeslider_visible=True, yaxis_title='Sales',xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("Please move the cursor towards the chart to see detailed data or you can drag the pointer on the day section. Details provide in table below.")
    st.markdown("<h5 style='text-align: left;'>Forecast Details :</h5>", unsafe_allow_html=True)
    gd = GridOptionsBuilder.from_dataframe(forecast_A2)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(forecast_A2, gridOptions=gridoption, height=250, reload_data=True)



    data_A2 = pd.read_csv('data/Data A2.csv')
    st.markdown("<h4 style='text-align: center;'> Data History - Category A Product A2</h4>", unsafe_allow_html=True)
    fig = go.Figure(
                data = go.Scatter(
                    x = data_A2['Day'],
                    y = data_A2['Sales'],
                    name = "Forecast ARIMA",
                    line = {'color': 'green'}))
    fig.layout.update(title_text="Data History", xaxis_rangeslider_visible=True, yaxis_title='Sales', xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("Please move the cursor towards the chart to see detailed data or you can drag the pointer on the day section. Details provide in table below.")
    st.markdown("<h5 style='text-align: left;'>History Details :</h5>", unsafe_allow_html=True)
    gd = GridOptionsBuilder.from_dataframe(data_A2)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(data_A2, gridOptions=gridoption, height=250, reload_data=True)
#==============================================================================


if option == "B-B1": 
    
    forecast_B1 = pd.read_csv('data/Forecast B1.csv')
  
    st.markdown("<h4 style='text-align: center;'>Sales Forcasting Up To 14 Days - Category B Product B1</h4>", unsafe_allow_html=True)
    fig = go.Figure(
            data = go.Scatter(
                x = forecast_B1['Day'],
                y = forecast_B1['Sales'],
                name = "Forecast ARIMA",
                line = {'color': 'yellow'}))
    fig.layout.update(title_text="Sales Forecast", xaxis_rangeslider_visible=True, yaxis_title='Sales',xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("Please move the cursor towards the chart to see detailed data or you can drag the pointer on the day section. Details provide in table below.")
    st.markdown("<h5 style='text-align: left;'>Forecast Details :</h5>", unsafe_allow_html=True)
    gd = GridOptionsBuilder.from_dataframe(forecast_B1)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(forecast_B1, gridOptions=gridoption, height=250, reload_data=True)


    data_B1 = pd.read_csv('data/Data B1.csv')
    st.markdown("<h4 style='text-align: center;'> Data History - Category B Product B1</h4>", unsafe_allow_html=True)
    fig = go.Figure(
                data = go.Scatter(
                    x = data_B1['Day'],
                    y = data_B1['Sales'],
                    name = "Forecast ARIMA",
                    line = {'color': 'yellow'}))
    fig.layout.update(title_text="Data History", xaxis_rangeslider_visible=True, yaxis_title='Sales', xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("Please move the cursor towards the chart to see detailed data or you can drag the pointer on the day section. Details provide in table below.")
    st.markdown("<h5 style='text-align: left;'>History Details :</h5>", unsafe_allow_html=True)
    gd = GridOptionsBuilder.from_dataframe(data_B1)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(data_B1, gridOptions=gridoption, height=250, reload_data=True)

#===========================================================================================


if option == "B-B2": 
    
    forecast_B2 = pd.read_csv('data/Forecast B2.csv')
     
    st.markdown("<h4 style='text-align: center;'>Sales Forcasting Up To 14 Days - Category B Product B2</h4>", unsafe_allow_html=True)
    fig = go.Figure(
            data = go.Scatter(
                x = forecast_B2['Day'],
                y = forecast_B2['Sales'],
                name = "Forecast ARIMA",
                line = {'color': 'red'}))
    fig.layout.update(title_text="Sales Forecast", xaxis_rangeslider_visible=True, yaxis_title='Sales',xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("Please move the cursor towards the chart to see detailed data or you can drag the pointer on the day section. Details provide in table below.")
    st.markdown("<h5 style='text-align: left;'>Forecast Details :</h5>", unsafe_allow_html=True)
    gd = GridOptionsBuilder.from_dataframe(forecast_B2)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(forecast_B2, gridOptions=gridoption, height=250, reload_data=True)



    data_B2 = pd.read_csv('data/Data B2.csv')
    st.markdown("<h4 style='text-align: center;'> Data History - Category B Product B2</h4>", unsafe_allow_html=True)
    fig = go.Figure(
                data = go.Scatter(
                    x = data_B2['Day'],
                    y = data_B2['Sales'],
                    name = "Forecast ARIMA",
                    line = {'color': 'red'}))
    fig.layout.update(title_text="Data History", xaxis_rangeslider_visible=True, yaxis_title='Sales', xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("Please move the cursor towards the chart to see detailed data or you can drag the pointer on the day section. Details provide in table below.")
    st.markdown("<h5 style='text-align: left;'>History Details :</h5>", unsafe_allow_html=True)
    gd = GridOptionsBuilder.from_dataframe(data_B2)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(data_B2, gridOptions=gridoption, height=250, reload_data=True)    

