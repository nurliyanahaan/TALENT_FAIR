import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import pickle
import time
from plotly import graph_objs as go
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from streamlit_option_menu import option_menu

# ---- Config & setting page icon and title ----
app_icon = Image.open("logo.png")
st.set_page_config(page_title="Sales Forecasting - Kalbe", page_icon=app_icon, layout="centered")

# ---- Hiding the menu and streamlit footer note ----
hide_menu = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_menu, unsafe_allow_html=True)


# ---- Setting the header and tagline -----

st.title("Sales Forecasting - Kalbe")
title_alignment="""
<style>
#Sales Forecasting {
text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

background = Image.open("logo.png")
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(background, use_column_width=True)

with st.form(key='form1'):

        st.write('''
            ### Please Choose Category and Product
            ''')
        
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
        st.write('Your option: ', option, 'Here you go ! The Sales Forcasting of Selected Category:')

# ---- RESULTS CONDITION ----
if option == "A-A1": 
    def data_upload():
        forecast_A1 = pd.read_csv('D:\TECH_FAIR\kalbe\data\Forecast A1.csv')
        forecast_A1 = forecast_A1.drop(columns='Unnamed: 0')
        return forecast_A1

    forecast_A1 = data_upload()
        
        
    st.markdown("<h4 style='text-align: center;'>Sales Forcasting Up To 14 Days - Category A Product A1</h4>", unsafe_allow_html=True)
    fig = go.Figure(
            data = go.Scatter(
                
                y = forecast_A1['Sales'],
                name = "Forecast ARIMA"
                ))
    fig.layout.update(title_text="Forecast", xaxis_rangeslider_visible=True, yaxis_title='Sales',xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("Forecast Result")
    gd = GridOptionsBuilder.from_dataframe(forecast_A1)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(forecast_A1, gridOptions=gridoption, height=250, reload_data=True)



    data_A1 = pd.read_csv('D:\TECH_FAIR\kalbe\data\Data A1.csv')
    st.markdown("<h4 style='text-align: center;'> Data History - Category A Product A1</h4>", unsafe_allow_html=True)
    fig = go.Figure(
                data = go.Scatter(
                    x = data_A1['Day'],
                    y = data_A1['Sales'],
                    name = "Forecast ARIMA"
                    ))
    fig.layout.update(title_text="History", xaxis_rangeslider_visible=True, yaxis_title='Sales', xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("History Result")
    gd = GridOptionsBuilder.from_dataframe(data_A1)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(data_A1, gridOptions=gridoption, height=250, reload_data=True)
#========================================================================

if option == "A-A2": 
    def data_upload():
        forecast_A2 = pd.read_csv('D:\TECH_FAIR\kalbe\data\Forecast A2.csv')
        forecast_A2 = forecast_A2.drop(columns='Unnamed: 0')
        return forecast_A2

    forecast_A2 = data_upload()
        
        
    st.markdown("<h4 style='text-align: center;'>Sales Forcasting Up To 14 Days - Category A Product A2</h4>", unsafe_allow_html=True)
    fig = go.Figure(
            data = go.Scatter(
                
                y = forecast_A2['Sales'],
                name = "Forecast ARIMA",
                line = {'color': 'green'}))
    fig.layout.update(title_text="Forecast", xaxis_rangeslider_visible=True, yaxis_title='Sales',xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("Forecast Result")
    gd = GridOptionsBuilder.from_dataframe(forecast_A2)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(forecast_A2, gridOptions=gridoption, height=250, reload_data=True)



    data_A2 = pd.read_csv('D:\TECH_FAIR\kalbe\data\Data A2.csv')
    st.markdown("<h4 style='text-align: center;'> Data History - Category A Product A2</h4>", unsafe_allow_html=True)
    fig = go.Figure(
                data = go.Scatter(
                    x = data_A2['Day'],
                    y = data_A2['Sales'],
                    name = "Forecast ARIMA",
                    line = {'color': 'green'}))
    fig.layout.update(title_text="History", xaxis_rangeslider_visible=True, yaxis_title='Sales', xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("History Result")
    gd = GridOptionsBuilder.from_dataframe(data_A2)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(data_A2, gridOptions=gridoption, height=250, reload_data=True)
#==============================================================================


if option == "B-B1": 
    def data_upload():
        forecast_B1 = pd.read_csv('D:\TECH_FAIR\kalbe\data\Forecast B1.csv')
        forecast_B1 = forecast_B1.drop(columns='Unnamed: 0')
        return forecast_B1

    forecast_B1 = data_upload()
        
        
    st.markdown("<h4 style='text-align: center;'>Sales Forcasting Up To 14 Days - Category B Product B1</h4>", unsafe_allow_html=True)
    fig = go.Figure(
            data = go.Scatter(
                
                y = forecast_B1['Sales'],
                name = "Forecast ARIMA",
                line = {'color': 'yellow'}))
    fig.layout.update(title_text="Forecast", xaxis_rangeslider_visible=True, yaxis_title='Sales',xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("Forecast Result")
    gd = GridOptionsBuilder.from_dataframe(forecast_B1)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(forecast_B1, gridOptions=gridoption, height=250, reload_data=True)


    data_B1 = pd.read_csv('D:\TECH_FAIR\kalbe\data\Data B1.csv')
    st.markdown("<h4 style='text-align: center;'> Data History - Category B Product B1</h4>", unsafe_allow_html=True)
    fig = go.Figure(
                data = go.Scatter(
                    x = data_B1['Day'],
                    y = data_B1['Sales'],
                    name = "Forecast ARIMA",
                    line = {'color': 'yellow'}))
    fig.layout.update(title_text="History", xaxis_rangeslider_visible=True, yaxis_title='Sales', xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("History Result")
    gd = GridOptionsBuilder.from_dataframe(data_B1)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(data_B1, gridOptions=gridoption, height=250, reload_data=True)

#===========================================================================================


if option == "B-B2": 
    def data_upload():
        forecast_B2 = pd.read_csv('D:\TECH_FAIR\kalbe\data\Forecast B2.csv')
        forecast_B2 = forecast_B2.drop(columns='Unnamed: 0')
        return forecast_B2

    forecast_B2 = data_upload()
        
        
    st.markdown("<h4 style='text-align: center;'>Sales Forcasting Up To 14 Days - Category B Product B2</h4>", unsafe_allow_html=True)
    fig = go.Figure(
            data = go.Scatter(
                
                y = forecast_B2['Sales'],
                name = "Forecast ARIMA",
                line = {'color': 'red'}))
    fig.layout.update(title_text="Forecast", xaxis_rangeslider_visible=True, yaxis_title='Sales',xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("Forecast Result")
    gd = GridOptionsBuilder.from_dataframe(forecast_B2)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(forecast_B2, gridOptions=gridoption, height=250, reload_data=True)



    data_B2 = pd.read_csv('D:\TECH_FAIR\kalbe\data\Data B2.csv')
    st.markdown("<h4 style='text-align: center;'> Data History - Category B Product B2</h4>", unsafe_allow_html=True)
    fig = go.Figure(
                data = go.Scatter(
                    x = data_B2['Day'],
                    y = data_B2['Sales'],
                    name = "Forecast ARIMA",
                    line = {'color': 'red'}))
    fig.layout.update(title_text="History", xaxis_rangeslider_visible=True, yaxis_title='Sales', xaxis_title='Day')
    st.plotly_chart(fig)
    st.write("History Result")
    gd = GridOptionsBuilder.from_dataframe(data_B2)
    gd.configure_pagination(enabled=True)
    gridoption = gd.build()
    AgGrid(data_B2, gridOptions=gridoption, height=250, reload_data=True)    

