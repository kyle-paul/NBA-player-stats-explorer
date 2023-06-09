import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from load_data import load_data
from side_bar import header, selection
from display_data import display
from download_file import filedownload
from heatmap import heatmap

st.title('NBA Player Stats Explorer')

st.markdown("""
This app performs simple webscraping of NBA player stats data!
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")

selected_year = header()

# Web scraping of NBA player stats
playerstats = load_data(selected_year)

# side_bar
selected_team, selected_pos = selection(playerstats)

# Display data
df_selected_team_pos = display(playerstats, selected_team, selected_pos)

# Download NBA player stats data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
st.markdown(filedownload(df_selected_team_pos), unsafe_allow_html=True)

# Heatmap
if st.button('Intercorrelation Heatmap'):
    heatmap(df_selected_team_pos)
