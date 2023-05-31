import streamlit as st
from PIL import Image

img = Image.open('assets/dataset-card.jpg')

st.image(img,width=200)

if st.checkbox("Show/Hide"):
    st.text("Showing the widget")
    st.image(img,width=50)

status = st.radio("Select Gender : ", ('Computer', 'English', 'Business'))
st.success(status)