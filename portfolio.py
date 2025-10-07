import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Jay Agrawal | AI/ML Engineer Portfolio",
    page_icon=":rocket:",
    layout="wide"
)

# --- HEADER SECTION ---
st.title("Hi, I'm Jay Agrawal 👋")
st.subheader("AI/ML Engineer | Data Scientist | Computer Vision & Deep Learning Enthusiast")

st.write(
    """
    Welcome to my portfolio! I'm passionate about applying Artificial Intelligence and Machine Learning 
    to solve real-world challenges. Explore my projects, skills, and research experience below.
    """
)

# --- SUMMARY SECTION ---
st.header("Summary")
st.write(
    """
    I’m an AI/ML Engineer with hands-on experience in machine learning, deep learning, and computer vision.
    I completed a one-year research project on **AI-assisted design in nanophotonics**, where I used neural networks 
    and optimization algorithms (Differential Evolution) to solve an inverse design problem.
    Skilled in **Python**, **TensorFlow**, and **model optimization**, I’m seeking a full-time role where I can 
    leverage AI to create impactful, data-driven solutions.
    """
)

# --- EDUCATION SECTION ---
st.header("Education")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Master of Technology – Artificial Intelligence")
    st.write("**Pandit Deendayal Energy University, Gandhinagar**  \n*June 2025*  \n**CGPA:** 8.32")
    st.write("Relevant Coursework: Neural Networks, Pattern Recognition, Machine Learning, OpenCV, Time Series Analysis")

with col2:
    st.subheader("Bachelor of Engineering – Computer Engineering")
    st.write("**Sal Engineering and Technical Institute (GTU)**  \n*July 2023*  \n**CGPA:** 7.59")

# --- SKILLS SECTION ---
st.header("Technical Skills")
st.write(
    """
    **Languages & Tools:** Python, Jupyter Notebook, Git, GitHub  
    **ML/DL Frameworks:** TensorFlow, Keras, Scikit-learn, XGBoost  
    **Computer Vision:** OpenCV, Transfer Learning, InceptionV3  
    **Data Handling:** Pandas, NumPy, Matplotlib, Seaborn  
    **Optimization:** Differential Evolution, Model Evaluation (MSE, R², Accuracy)
    """
)

# --- EXPERIENCE SECTION ---
st.header("Professional Experience")

st.subheader("Machine Learning Intern | Maxgen Technologies Pvt. Ltd.")
st.write("*Feb 2023 – Apr 2023*")
st.write(
    """
    - Gained hands-on experience with TensorFlow, Keras, and Scikit-learn.  
    - Developed a **Skin Disease Detection** model using deep learning and OpenCV.  
    - Tools Used: Python, TensorFlow, Pandas, Jupyter Notebook, Google Colab.
    """
)

st.subheader("Data Science & ML Intern | BrainyBeam Technologies Pvt. Ltd.")
st.write("*Jun 2022 – Jul 2022*")
st.write(
    """
    - Built a **Recommendation System using Sentiment Analysis**.  
    - Applied NLP preprocessing and exploratory data analysis using Python and Kaggle datasets.  
    - Tools Used: Python, Pandas, NLTK, Jupyter Notebook.
    """
)

# --- RESEARCH EXPERIENCE ---
st.header("Research Experience & Publications")

st.subheader("AI-Assisted Design Discovery in Nanophotonics – PDEU")
st.write("*July 2024 – May 2025*")
st.write(
    """
    - Solved an **inverse design problem** using Deep Neural Networks and Differential Evolution.  
    - Optimized 8-layer **Distributed Bragg Reflectors (Sb₂S₃/SiO₂)** for spectral filtering applications.  
    - Reduced simulation time from **15 minutes per run** to **milliseconds** using a surrogate DNN model.  
    - Presented at **ETOT–I Conference (Andhra Pradesh, Jan 2025)** and preparing journal submissions.
    """
)

# --- ACADEMIC PROJECTS SECTION ---
st.header("Academic Projects")

st.subheader("Fruit Classification (Fresh vs Rotten)")
st.write(
    """
    - Built an image classifier using **InceptionV3 with transfer learning** achieving 97% accuracy.  
    - Collected and preprocessed dataset, applied augmentation, and validated performance.  
    - Tools Used: Python, TensorFlow, Keras, OpenCV, Google Colab.
    """
)

st.subheader("House Price Prediction")
st.write(
    """
    - Performed exploratory data analysis and feature engineering on housing data.  
    - Used **XGBoost regression** achieving an R² score of 0.82 on the test dataset.  
    - Tools Used: Python, Scikit-learn, Pandas, Matplotlib, Seaborn.
    """
)

# --- OTHER WORK EXPERIENCE ---
st.header("Other Work Experience")
st.subheader("Research & Teaching Assistant | PDEU")
st.write(
    """
    - Assisted lab sessions for AI/ML courses and guided student projects.  
    - Supported professors in grading and technical mentoring.
    """
)

# --- CONTACT SECTION ---
st.header("Contact Me")
st.write(
    """
    - 📧 **Email:** [agrawaljay654@gmail.com](mailto:agrawaljay654@gmail.com)  
    - 🔗 **LinkedIn:** [linkedin.com/in/jay-agrawal-87321a215](https://linkedin.com/in/jay-agrawal-87321a215)  
    - 💻 **GitHub:** [github.com/Jay-agrawal15](https://github.com/Jay-agrawal15)  
    - 📍 **Location:** Ahmedabad, India
    """
)

# --- CONTACT FORM ---
st.subheader("Send a Message")
with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button(label="Send")

    if submit_button:
        st.success("Thank you! Your message has been sent successfully.")
