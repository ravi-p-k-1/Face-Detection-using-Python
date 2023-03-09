import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image
from main import *
from webcam import *
import base64

with st.sidebar:
    ch=option_menu(
        menu_title="Main Menu",
        options=["Home","Attendance","About Us","Feedback"],
        icons=['house','file-earmark-spreadsheet-fill','people-fill','pencil-square'],
        styles={
                    "container": {"padding": "5!important","background-color": "#E3E4FA"},
                    "icon": {"color": "White", "font-size": "25px"}, 
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#4d4d4d"},
                    "nav-link-selected": {"background-color": "#4d4d4d"},
                }
    )

with open("aboutus.html",'r') as f:
   aboutus=f.read()
def abtus():
    components.html(aboutus,height=1400,scrolling=True)
    
    
with open("feedback.html",'r') as f:
   feedback=f.read()
def fdb():
    components.html(feedback,width=700,height=600)

if ch=="Home":
    st.markdown("<h1 style='text-align: center'>WELCOME TO FACE RECOGNITION</h1>", unsafe_allow_html=True)
    # image=Image.open("C:\\Users\\MOKSHIL\\Desktop\\MINeD\\Home_img.png")
    # st.image(image)
    file_ = open("mlxN1G.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="Face recognition gif">',
        unsafe_allow_html=True,
        )
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        col4,col5=st.columns([0.85,1])
        with col4:
            if st.button("FACE DETECTION USING CCTV"):
                fdr()
        with col5:
            if st.button("FACE DETECTION USING WEBCAM"):
                wcam()

    with col3:
        st.write("")
    
    
elif ch=="Attendance":
    st.markdown("<h1 style='text-align: center'>ATTENDANCE REPORT</h1>", unsafe_allow_html=True)
    df=pd.read_csv("Attendance.csv")
    st.dataframe(df)

elif ch=="About Us":
    st.markdown("<h1 style='text-align: center'>ABOUT US</h1>", unsafe_allow_html=True)
    abtus()
    
elif ch=="Feedback":
    st.markdown("<h1 style='text-align: center'>RATINGS</h1>", unsafe_allow_html=True)
    fdb()
