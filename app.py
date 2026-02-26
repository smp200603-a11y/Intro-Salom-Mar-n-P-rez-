import streamlit as st 
from PIL import Image
st.title("Mi primera app")
st.header("Esta es mi pagina de presentación")

Image=Image.open("myimagen.snoopy-joe-cool-e1725621027692")
st.image(image,caption="Esta es mi imagen")
