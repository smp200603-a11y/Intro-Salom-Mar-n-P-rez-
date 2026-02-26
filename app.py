import streamlit as st 
from PIL import Image
st.title("Mi primera app")
st.header("Esta es mi pagina de presentación")

image=Image.open("snoopy-joe-cool-e1725621027692.jpg")
st.image(image,caption="snoopy-joe-cool-e1725621027692.jpg")
