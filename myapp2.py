import streamlit as st
from multiapp import MultiApp
from apps import home, data, training

app = MultiApp()

st.write(
'''
# Streamlit Tutorial

'''

)


app.add_app("Home", home.app, 'house-fill')

app.add_app("Data", data.app, 'bar-chart-line-fill')

app.add_app("Training", training.app, 'clock-fill')

app.run()