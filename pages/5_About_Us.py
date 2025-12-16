import streamlit as st

st.set_page_config(page_title="About Us", page_icon="ℹ️", layout="wide")

# Header
st.markdown("""
    <div style="
        background: linear-gradient(90deg, #667eea, #764ba2);
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 20px;">
        <h2 style="margin: 0;">ℹ️ About Us</h2>
        <p style="font-size:16px; margin:5px 0 0 0;">
           Informasi Mata Kuliah & Tim Pengembang
        </p>
    </div>
""", unsafe_allow_html=True)

# Card style
card_style = """
<style>
.about-card {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    border-left: 6px solid #667eea;
    margin-bottom: 20px;
}
.about-title {
    font-size: 22px;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 15px;
}
.about-content {
    font-size: 15px;
    color: #444444;
    line-height: 1.8;
}
.team-member {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    border-radius: 10px;
    margin: 10px 0;
    text-align: center;
}
.tech-badge {
    display: inline-block;
    background-color: #667eea;
    color: white;
    padding: 8px 15px;
    border-radius: 20px;
    margin: 5px;
    font-size: 14px;
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

# Project Information
st.markdown("""
<div class="about-card">
    <div class="about-title">🎓 Informasi Mata Kuliah</div>
    <div class="about-content">
        <b>Mata Kuliah:</b> Akuisisi Data<br>
        <b>Kelompok:</b> MBKM - Ikhwan Fajri Wanda<br>
        <b>Topik:</b> Sistem Analisis Depresi Mahasiswa<br>
        <b>Semester:</b> Ganjil 2025/2026<br>
        <b>Universitas:</b> Universitas Andalas<br>
        <b>Program Studi:</b> Sistem Informasi<br><br>
        <b>Deskripsi Project:</b><br>
        Project ini merupakan implementasi sistem analisis data untuk mengidentifikasi 
        faktor-faktor yang mempengaruhi tingkat depresi pada mahasiswa. Menggunakan 
        dataset dengan lebih dari 27,000 records, sistem ini menerapkan teknik machine 
        learning (Random Forest Classification) untuk memprediksi dan menganalisis 
        pola depresi berdasarkan berbagai variabel seperti tekanan akademik, pola tidur, 
        kebiasaan makan, dan faktor-faktor lainnya.
    </div>
</div>
""", unsafe_allow_html=True)

# Project Objectives and Dataset
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="about-card">
        <div class="about-title">🎯 Tujuan Project</div>
        <div class="about-content">
            <ul style="margin: 0; padding-left: 20px;">
                <li>Menganalisis dataset depresi mahasiswa secara komprehensif</li>
                <li>Mengidentifikasi faktor-faktor utama yang mempengaruhi depresi</li>
                <li>Membangun model prediksi menggunakan Random Forest</li>
                <li>Melakukan visualisasi data untuk insight yang actionable</li>
                <li>Evaluasi model dengan confusion matrix & metrics</li>
                <li>Menyediakan dashboard interaktif untuk eksplorasi data</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="about-card">
        <div class="about-title">📊 Dataset Information</div>
        <div class="about-content">
            <b>Nama Dataset:</b> Student Depression Dataset<br>
            <b>Sumber:</b> <a href="https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset/code" target="_blank" style="color: #667eea;">Kaggle</a><br>
            <b>Jumlah Records:</b> ~27,000+ mahasiswa<br>
            <b>Jumlah Features:</b> 18 kolom<br>
            <b>Target Variable:</b> Depression (Binary: 0/1)
        </div>
    </div>
    """, unsafe_allow_html=True)

# Technologies Used
st.markdown("<h2 style='text-align: center; color: #667eea;'>💻 Teknologi yang Digunakan</h2>", unsafe_allow_html=True)
st.write("")

st.markdown("""
<div style="text-align: center;">
    <span class="tech-badge">🐍 Python 3.8+</span>
    <span class="tech-badge">🎈 Streamlit</span>
    <span class="tech-badge">🐼 Pandas</span>
    <span class="tech-badge">🔢 NumPy</span>
    <span class="tech-badge">🤖 Scikit-learn</span>
    <span class="tech-badge">📊 Matplotlib</span>
    <span class="tech-badge">🎨 Seaborn</span>
    <span class="tech-badge">📈 Plotly</span>
    <span class="tech-badge">💾 Joblib</span>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("---")

# Team Members
st.markdown("<h2 style='text-align: center; color: #667eea;'>👥 Tim Pengembang</h2>", unsafe_allow_html=True)
st.write("")

# You can customize this section with your actual team members
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="team-member">
        <h3 style="margin: 0;">Ikhwan Hamidi</h3>
        <p style="margin: 10px 0 0 0; font-size: 14px;">
            NIM: 2311521003<br>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="team-member">
        <h3 style="margin: 0;">Muhammad Fajri</h3>
        <p style="margin: 10px 0 0 0; font-size: 14px;">
            NIM: 2311522015<br>
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="team-member">
        <h3 style="margin: 0;">Wanda Hamidah</h3>
        <p style="margin: 10px 0 0 0; font-size: 14px;">
            NIM: 2311523017<br>
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# Footer
st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
        <p style="margin: 0;">
            <b>Tugas Besar Akuisisi Data - Sistem Analisis Depresi Mahasiswa</b><br>
            Dibuat dengan ❤️ menggunakan Streamlit, Python, dan Scikit-learn<br>
            <small>© 2025 - Universitas Andalas</small>
        </p>
    </div>
""", unsafe_allow_html=True)

