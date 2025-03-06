import streamlit as st
import json
from streamlit_lottie import st_lottie
from PIL import Image
import requests

# Load Lottie Animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load assets
lottie_coding = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_w51pcehl.json")

# Page Configurations
st.set_page_config(page_title="My Digital Footprint", page_icon="📌", layout="wide")

# Sidebar for Profile Customization
st.sidebar.header("Customize Profile")
name = st.sidebar.text_input("Full Name", "MUNYANEZA Emmanuel")
bio = st.sidebar.text_area("Short Bio", "Final Year Computer Science Student @ INES Ruhengeri")
location = st.sidebar.text_input("Location", "Musanze, Rwanda")
resume_file = st.sidebar.file_uploader("Upload Resume (PDF)", type=["pdf"])


# Navigation Menu
menu = ["Home", "Projects", "Skills", "Testimonials", "Timeline", "Contact"]
choice = st.sidebar.radio("Go to", menu)

# Home Section
if choice == "Home":
    st.title("👋 Welcome to My Digital Footprint")
    st_lottie(lottie_coding, height=300)
    st.image('profile.jpeg', caption='Profile Picture', width=150)
    st.subheader(f"Hi, I'm {name}!")
    st.write(f"📍 {location}")
    st.write(f"📖 {bio}")
    
    
    if resume_file:
        st.download_button(label="📄 Download Resume", data=resume_file, file_name="Resume.pdf", mime="application/pdf")

# Projects Section
elif choice == "Projects":
    st.title("🚀 My Projects")
    st.write("Here are some projects I have worked on:")
    
    project_filter = st.selectbox("Filter by:", ["All", "Year 1", "Year 2", "Year 3", "Final Year Project"])
    
    projects = [
        {"title": "To-Do List App", "year": "Year 1", "desc": "A Java-based to-do list application.", "github": "https://github.com"},
        {"title": "Student Management System", "year": "Year 2", "desc": "This is a project that I have worked on during my second year at INES-Ruhengeri. It is a web application that helps students to manage their academic information such as courses, grades, attendance, etc. It is built using HTML, CSS, JavaScript, Node.js, Express.js, and MongoDB.", "github": "https://github.com"},
        {"title": "E-commerce Website", "year": "Year 3", "desc": "This is a project that I have worked on during my third year at INES-Ruhengeri. It is a web application that allows users to buy and sell products online. It is built using HTML, CSS, JavaScript, Node.js, Express.js, and MongoDB.", "github": "https://github.com"},
        {"title": "Blog Website", "year": "Final Year Project", "desc": "This is a project that I have worked on during my fourth year at INES-Ruhengeri. It is a web application that allows user to write and publish blog posts. It is built using React.js, Node.js, Express.js, and MongoDB.", "github": "https://github.com"}
    ]
    
    for project in projects:
        if project_filter == "All" or project_filter == project["year"]:
            st.subheader(f"🔹 {project['title']}")
            st.write(f"📌 {project['desc']}")
            st.write(f"🔗 [GitHub Repo]({project['github']})")
            st.divider()

# Skills Section
elif choice == "Skills":
    st.title("💡 Skills & Achievements")
    st.write("### Programming Languages")
    st.progress(80)  # Example: JavaScript 70%
    st.write("JavaScript")
    st.progress(70)  # Example: SQL 60%
    st.write("SQL")
    st.progress(60)  # Example: Python 80%
    st.write("Python")
    st.progress(80)
    st.write("Java")
    st.progress(70)
    st.write("C")
    st.progress(60)
    st.write("C++")
    
    st.write("### Certifications & Achievements")
    st.write("✔ Google Data Analytics Certification")
    st.write("✔ Finalist at INES Hackathon")

# Testimonials Section
elif choice == "Testimonials":
    st.title("🗣️ Testimonials")
    testimonials = [
        "Emmanuel is an outstanding software developer! - Dr. Theodore",
        "His job-matching platform was incredibly innovative. - Prof. Alice"
    ]
    for testimonial in testimonials:
        st.write(f"💬 *{testimonial}*")

# Timeline Section
elif choice == "Timeline":
    st.title("⏳ My Academic & Project Milestones")
    st.write("✅ Year 1: Completed my first Java project")
    st.write("🏆 Year 2: Participated in my first Hackathon")
    st.write("💼 Year 3: Internship at XYZ Company and Final Year Project Development")

# Contact Section
elif choice == "Contact":
    st.title("📩 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Message sent successfully! I'll get back to you soon.")
    
    st.write("### Connect with me:")
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    st.write("🔗 [GitHub](https://github.com)")
    st.write("📧 munyanezae610@gmail.com")

st.sidebar.success("Navigate through the sections to explore more!")
