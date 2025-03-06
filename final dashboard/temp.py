import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu
from introduction_page_module import introduction_page
from data_collection_module import data_collection_page
from interactive_data_analysis_page_module import interactive_data_analysis_page
from insights_page_module import insights_page
from contributor_page_module import contributor_page
from dashboard_page_module import dashboard_page
from PIL import Image
import folium
from streamlit_folium import folium_static
st.set_page_config(layout="wide")


@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    df1 = data.filter(
        [
            "Chlorophyll",
            "Dissolved Oxygen",
            "Dissolved Oxygen Matter",
            "Salinty",
            "Temperature",
            "Turbidity",
            "pH",
            "Suspended Matter",
        ]
    )
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Date"] = pd.to_datetime(data["Date"]).dt.date
    data["Year"] = pd.to_datetime(data["Date"]).dt.strftime("%Y")
    data["Month"] = pd.to_datetime(data["Date"]).dt.strftime("%m")
    data["Day"] = pd.to_datetime(data["Date"]).dt.strftime("%d")
    return data, df1

with open("styles.css", "r") as source_style:
 st.markdown(f"<style>{source_style.read()}</style>", 
             unsafe_allow_html = True)

st.header("Monitoring the Water Quality in Bhopal Region using Satellite Imagery and GIS Techniques")
# image = Image.open(r'logo.png')
# st.image(image)

header_project = st.container()
data_collection = st.container()
data_analysis = st.container()



data_df, df1 = load_data("merged_data.csv")

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=[
            "Project Information",
            "Data Collection",            
            "Interactive Data Analysis",
            "Insights",
            "Dashboards",
            "Contributors"
        ],
        default_index=0,
    )


if selected == "Project Information":

    with header_project:
        introduction_page()
        
if selected == "Data Collection":
    with data_collection:
        data_collection_page()

if selected =='Insights':      
    insights_page()

if selected == "Interactive Data Analysis":
    interactive_data_analysis_page()

if selected == "Contributors":
    contributor_page()

if selected == "Dashboards":
    dashboard_page()