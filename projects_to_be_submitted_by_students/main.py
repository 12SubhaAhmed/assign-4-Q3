import streamlit as st

st.set_page_config(page_title='My First Website',page_icon="🌍", layout='centered')
st.title('Welcome to my first website')

st.sidebar.title('Navigation')
page= st.sidebar.radio('Go to',['Home','About Us', 'Contact Us'])

if page == 'Home':
    st.header('Home page')
    st.write('This is a simple home page')
    name = st.text_input('Enter your name: ')
    if name:
        st.success(f'Hello {name}! Thak you for visiting.')

elif page == 'About Us':
    st.header("About Us")
    st.write("This is about us page build with Python and Streamlit.")

elif page == 'Contact Us':
    st.header('Contact Us')
    email = st.text_input("Your Email: ")
    message = st.text_input("Write your message: ")
    if st.button("Submit"):
        st.success("Thanks for contacting us!")



