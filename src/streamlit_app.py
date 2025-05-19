import streamlit as st
import os
import interfaces as pg

# Page configuration
st.set_page_config(page_title="Machine Problem II", page_icon=":material/network_intelligence_history:", layout="wide", initial_sidebar_state="collapsed")

# Load custom CSS
with open("assets/css/styles.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# Define your pages
home = st.Page(page=pg.home_page, title='Home')
brute_force_algos = st.Page(page=pg.brute_force_page, title='Brute Force')
optimized_algos = st.Page(page=pg.optimized_page, title='Optimized ')
comparison = st.Page(page=pg.comparison, title='Comparison')
analysis = st.Page(page=pg.analysis, title='Analysis')

# Hide the default navigation but make pages available
pg = st.navigation([home, brute_force_algos, optimized_algos, comparison, analysis], position="hidden")

# Create a top navigation bar with right alignment
left_section, _, right_section = st.columns([2, 2, 6], gap='large', vertical_alignment='center')

with right_section:
    nav_cols = st.columns(5)
    with nav_cols[0]:
        st.page_link(home, label="Home")
    with nav_cols[1]:
        st.page_link(brute_force_algos, label="Brute Force")
    with nav_cols[2]:
        st.page_link(optimized_algos, label="Optimized")
    with nav_cols[3]:
        st.page_link(comparison, label="Comparison")
    with nav_cols[4]:
        st.page_link(analysis, label="Analysis")

pg.run()