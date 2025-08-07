import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

st.title("Hello, Streamlit !")
st.write(":100: This is your first streamlit app")
st.text(" Lets get started ")

#conditional logic with widgets

num = st.text_input("Enter your number:")
if num:
    num_int = int(num)
    if num_int > 0:
        st.write("Number is positive")
    elif num_int < 0:
        st.write("Number is negative")
    else:
        st.write("Number is zero")

#Displaying Data and charts

df= pd.DataFrame(np.random.randn(10,2), columns =['A','B'])
st.line_chart(df) 
st.bar_chart(df)

#Media layout and advanced widget
st.sidebar.title("Navigation")
st.image("https://th.bing.com/th/id/OIP.GhhZk37U4KMIgOZIbUrEFgHaEw?w=238&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3", caption="Sample Image")
st.video("https://www.youtube.com/watch?v=VqgUkExPvLY")

#File uploading and caching topics
upload_file = st.file_uploader("upload a csv", type = 'csv')
if upload_file:
    df=pd.read_csv(upload_file)
    st.dataframe(df)

st.title("Text and Markdown Demo")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**,*Italic*,`Code`,[Link](https://streamlit.io)")
st.code("for i in range(5): print(i)",language="python")

st.text_input("What's your name?")
st.text_area("Write something....")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range",0,100)
st.selectbox("Select a fruit",["Apple","Banana","Mango"])
st.multiselect("Choose toppings",["Cheese","Tomato","Olives"])
st.radio("Pick one",["Option A","Option B"])
st.checkbox("I agree to the terms")

# View Chart
if st.button("click Me"):
    st.success("Button Clicked!")

if st.checkbox("Show Details"):
    st.info("Here are more details...")

option = st.radio("Choose view", ["Show Chart","Show Table"])
if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

#login form

with st.form ("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password",type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        st.succcess(f"Welcome, {username}!")

col1 , col2 = st.columns(2)

with col1:
    st.button ("Press me in Column 1")
with col2:
    st.button("Press me in Column 2")

audio_file = open ("example.mp3", "rb")
st.audio(audio_file.read(),format="audio/mp3")

fig, ax = plt.subplots()
ax.plot([1,2,3],[1,4,9])
st.pyplot(fig)

import plotly.express as px

df= px.data.iris()
fig = px.scatter(df,x ="sepal_width", y = "sepal_length")
st.plotly_chart(fig)