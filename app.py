import streamlit as st 
from PIL import Image
st.title("Mi primera app")
st.header("Esta es mi pagina de presentación")

image=Image.open("snoopy-joe-cool-e1725621027692.jpg")
st.image(image,caption="snoopy-joe-cool-e1725621027692.jpg")

texto=st.text_input("Ingresa texto","texto inicial")
st.write("El texto que has escrito es",texto)
if st.button("presiona el boton")
   st.write("has presionado")
