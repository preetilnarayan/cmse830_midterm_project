import streamlit as st
from PIL import Image
import os

def show_home():
    # Title and Subtitle
    st.title(" Student Success & Dropout Risk Analysis")
    st.markdown("""
    <style>
        .subtitle {
            font-size: 18px;
            color: #444;
            font-weight: 500;
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="subtitle">An interactive data-driven exploration for understanding factors influencing academic success.</p>', unsafe_allow_html=True)

    # Load Image
    script_dir = os.path.dirname(__file__)
    img_path = os.path.join(script_dir, "assets", "student_success_banner.png")

    if os.path.exists(img_path):
        image = Image.open(img_path)
        st.image(image, use_container_width=True)
    else:
        st.info("STUDENT SUCCESS VS DROPOUT IMAGE PLACEHOLDER")

    # App Overview
    st.markdown("## About the Project")
    st.write("""
    The **Student Success and Dropout Risk Analysis App** enables educators, researchers, and analysts to explore
    how **personal, social, and academic factors** influence student performance and dropout tendencies.
    
    Through this interactive dashboard, you can:
    - Explore and understand the dataset.
    - Identify patterns and correlations across multiple student attributes.
    - Uncover the most significant features driving success or risk.
    - Summarize actionable insights to support student retention strategies.
    """)

    # Navigation Guide
    st.markdown("## Navigate the App")
    st.write("""
    Use the **sidebar** on the left to move through key sections:
    - **Home** — Overview and introduction  
    - **Data Overview** — Explore raw dataset and structure  
    - **EDA & Insights** — Visualize trends, distributions, and group patterns  
    - **Feature Analysis** — Study factors that influence outcomes  
    - **Correlation Study** — Discover variable relationships  
    - **Summary Report** — Review conclusions and findings  
    """)

# Run the homepage
show_home()
