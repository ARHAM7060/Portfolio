import streamlit as st
import json
import os
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# === CONFIG ===
st.set_page_config(page_title="👨‍💻 Portfolio | Mohd Arham", layout="wide", page_icon="💼")

# === LOAD PROFILE IMAGE ===
image_path = "assets/profile.jpg"  # Add your profile photo here
if os.path.exists(image_path):
    profile_img = Image.open(image_path)
else:
    profile_img = None

# === FUNCTION TO LOAD LOTTIE ===
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
profile_lottie = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_mjlh3hcy.json")
project_lottie = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_w51pcehl.json")

# === SIDEBAR ===
st.sidebar.title("📚 Navigation")
section = st.sidebar.radio("Go to", ["🏠 Home", "📂 Projects", "👤 In-depth Profile", "📞 Contact"])

# === HOME ===
if section == "🏠 Home":
    col1, col2 = st.columns([1, 3])
    with col1:
        if profile_img:
            st.image(profile_img, width=180)
    with col2:
        st.title("Mohd Arham")
        st.subheader("Machine Learning | Data Science | Python Developer")
        st.write("📧 mohdarham7060@gmail.com | 📞 +91-7060538955")
        st.write("[GitHub](https://github.com/ARHAM7060) | [LinkedIn](http://www.linkedin.com/in/arhamai) | [Portfolio](https://yourportfolio.com)")
    st.markdown("---")
    st_lottie(profile_lottie, height=250, key="profile")

# === PROJECTS SECTION ===
elif section == "📂 Projects":
    st.header("📂 My Projects")
    st_lottie(project_lottie, height=200, key="project")

    projects_file = "data/projects.json"
    if os.path.exists(projects_file):
        with open(projects_file, "r") as f:
            projects = json.load(f)
    else:
        projects = []

    for project in projects:
        with st.container():
            st.subheader(f"🔹 {project['title']}")
            st.write(project["description"])
            st.markdown(f"**Tech Stack:** `{', '.join(project['tech'])}`")
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown(f"🔗 [Live Demo]({project['demo']})")
            with col2:
                st.markdown(f"📁 [Source Code]({project['github']})")
            st.markdown("---")

# === IN-DEPTH PROFILE ===
elif section == "👤 Full Profile":
    st.header("👤 Detailed Profile")
    st.write("""
        - 🎓 **Bsc Hons Applied Maths**: Jamia Millia Islamia University, 8.1 CGPA
        - 🛠️ **Skills**: Python, Machine Learning, MySQL, Deep Learning, NLP, Power Bi, Excel, etc.
        - 🧠 **Strengths**: Problem Solving, Communication, Quick Learner
        - 🏆 **Certifications**: Data Science Intern at Unified Mentor
        - 🌱 **Currently Learning**: Deep Learning, NLP
    """)

# === CONTACT ===
elif section == "📞 Contact":
    st.header("📞 Get in Touch")
    st.write("""
    - 📧 Email: mohdarham7060@gmail.com
    - 📱 Phone: +91-7060538955
    - 🐙 GitHub: [github.com/yourusername](https://github.com/yourusername)
    - 🔗 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
    - 🌐 Portfolio: [yourportfolio.com](https://yourportfolio.com)
    """)

# === FOOTER ===
st.markdown("\n---")
st.caption("Made with ❤️ using Streamlit")