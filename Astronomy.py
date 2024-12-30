import streamlit as st
import requests


api_key=""
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"


request=requests.get(url)

data=request.json()

title=data["title"]
image_url=data["url"]
explaination=data["explanation"]

image_filepath="img.png"
request2=requests.get(image_url)

with open(image_filepath,"wb") as file:
    file.write(request2.content)

st.title(title)
st.image(image_filepath)
st.write(explaination)