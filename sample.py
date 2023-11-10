from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

#load assets

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_iv4dsx3q.json")
img_front = Image.open("C:/Users/pooja/PycharmProjects/pythonProject1/image_py/Screenshot (57).png")
img_lottie_animation = Image.open("C:/Users/pooja/PycharmProjects/pythonProject1/image_py/Screenshot (59).png")

st.set_page_config(
    page_title="ed4all",
    page_icon="💾",
    layout="wide"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css.txt")

with st.container():
    st.title("Let us learn together")
    st.header("Education for all")
    st.write("We are experts in e-learning")
    st.write("[Learn more :)](http://www.google.com/)")

with st.container():
    st.write("Trusted coaching with experts")
    st.write("Learn the skills you need to take the next step — and every step after. Log in now to save on courses.")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Python")
        st.write("For beginners")
        st.write("level0-level4")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who I AM")
        st.write("##")
        st.write("Take one of ed4all’s range of Python courses and learn how to code using this incredibly useful language. Its simple syntax and readability makes Python perfect for Flask, Django, data science, and machine learning. You’ll learn how to build everything from games to sites to apps. Choose from a range of courses that will appeal to")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Hey")
        st.write("##")
#--Projects--

with st.container():
    st.write("---")
    st.header("ed4all")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Upskill your team with ed4all")
        st.write("""Unlimited access to 22,000+ top Udemy courses, anytime, anywhere
        International course collection in 14 languages
        Top certifications in tech and business
                 """)
        st.markdown("[watch video..](https://www.youtube.com/watch?v=UeRgJ99aGGw)")
with st.container():
    st.header("upskill your learning with ed4all")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_front)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write("""Learn How to use Lottie files in Streamlit! 
        Animations make our website engaging and fun
                 """)
        st.markdown("[watch video..](https://www.youtube.com/watch?v=UeRgJ99aGGw)")

with st.container():
    st.write("---")
    st.header("Connect with us")
    st.write("##")

    #Docs "https://formsubmit.co/" !! Change Email Address!!
    contact_form = """
    <form action = "https://formsubmit.co/poojapandian07@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "your name" required>
        <input type="email" name="email" placeholder = "Your email" required>
        <textarea name = "message" placeholder = "Your message here" required></textarea>
        <button type="submit">Send</button>
     </form>"""
    left_column, right_column = st.columns(2)
    with left_column:
         st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
         st.empty()
