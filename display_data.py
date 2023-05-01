import streamlit as st

def display(playerstats, selected_team, selected_pos):
    st.subheader('Display Player Stats of Selected Team(s)')
    # filtering
    df_selected_team_pos = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]
    # display shape of dataframe
    st.write('Data Dimension: ' + str(df_selected_team_pos.shape[0]) + ' rows and ' + str(df_selected_team_pos.shape[1]) + ' columns.')
    # display dataframe
    st.dataframe(df_selected_team_pos)
    
    return df_selected_team_pos