import streamlit as st

# Page config
st.set_page_config(
    page_title="Analisis Depresi Siswa/Mahasiswa",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header dengan gradient
st.markdown("""
    <div style="
        background: linear-gradient(90deg, #667eea, #764ba2);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 20px;">
        <h1 style="margin: 0;">🧠 Sistem Analisis Depresi Siswa/Mahasiswa</h1>
        <p style="font-size:18px; margin:10px 0 0 0;">
           Tugas Besar Akuisisi Data - Analisis & Prediksi Depresi pada Siswa/Mahasiswa
        </p>
    </div>
""", unsafe_allow_html=True)

# Card style
card_style = """
<style>
.card {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    border-left: 6px solid #667eea;
    transition: 0.3s;
    margin-bottom: 20px;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
}
.card-title {
    font-size: 20px;
    font-weight: bold;
    color: #667eea;
    margin-bottom: 10px;
}
.card-desc {
    font-size: 15px;
    color: #444444;
    text-align: justify;
    line-height: 1.6;
}
.workflow-step {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
    font-weight: bold;
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

# Introduction
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">📊 Gambaran Umum Project</div>
        <div class="card-desc">
        Project ini menganalisis faktor-faktor yang mempengaruhi <b>depresi pada mahasiswa</b> 
        menggunakan machine learning. Dataset mencakup berbagai aspek seperti tekanan akademik, 
        pola tidur, kebiasaan makan, riwayat keluarga, dan pemikiran bunuh diri.
        <br><br>
        Model <b>Random Forest Classification</b> digunakan untuk memprediksi tingkat depresi 
        berdasarkan fitur-fitur tersebut.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">🎯 Tujuan Analisis</div>
        <div class="card-desc">
        <ul style="margin: 0; padding-left: 20px;">
            <li>Mengidentifikasi pola depresi pada mahasiswa</li>
            <li>Menemukan faktor-faktor yang paling berpengaruh</li>
            <li>Membangun model prediksi depresi</li>
            <li>Visualisasi distribusi dan korelasi data</li>
            <li>Evaluasi performa model dengan metrics</li>
        </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">📋 Dataset Information</div>
        <div class="card-desc">
        <b>Dataset:</b> Student Depression Dataset<br>
        <b>Total Records:</b> ~27,000+ mahasiswa<br>
        <b>Features:</b> 18 kolom<br>
        <b>Target:</b> Depression (0 = No, 1 = Yes)<br><br>
        <b>Fitur Utama:</b><br>
        Gender, Age, Academic Pressure, CGPA, Sleep Duration, Dietary Habits, 
        Suicidal Thoughts, Family History, Work/Study Hours, Financial Stress
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# Workflow
st.markdown("<h2 style='text-align: center; color: #667eea;'>🔄 Alur Penggunaan Aplikasi</h2>", unsafe_allow_html=True)
st.write("")

workflow_cols = st.columns(5)

with workflow_cols[0]:
    st.markdown("""
        <div class="workflow-step">
            <div style="text-align: center; font-size: 30px;">📤</div>
            <div style="text-align: center;">1. Input Data</div>
        </div>
        <p style="text-align: center; color: #666;">
        Upload dataset CSV atau gunakan dataset default
        </p>
    """, unsafe_allow_html=True)

with workflow_cols[1]:
    st.markdown("""
        <div class="workflow-step">
            <div style="text-align: center; font-size: 30px;">🔧</div>
            <div style="text-align: center;">2. Preprocessing</div>
        </div>
        <p style="text-align: center; color: #666;">
        Cleaning, encoding, handling missing values
        </p>
    """, unsafe_allow_html=True)

with workflow_cols[2]:
    st.markdown("""
        <div class="workflow-step">
            <div style="text-align: center; font-size: 30px;">📈</div>
            <div style="text-align: center;">3. Analysis</div>
        </div>
        <p style="text-align: center; color: #666;">
        Training Random Forest & evaluasi model
        </p>
    """, unsafe_allow_html=True)

with workflow_cols[3]:
    st.markdown("""
        <div class="workflow-step">
            <div style="text-align: center; font-size: 30px;">📊</div>
            <div style="text-align: center;">4. Visualizations</div>
        </div>
        <p style="text-align: center; color: #666;">
        Distribusi data & korelasi
        </p>
    """, unsafe_allow_html=True)

with workflow_cols[4]:
    st.markdown("""
        <div class="workflow-step">
            <div style="text-align: center; font-size: 30px;">ℹ️</div>
            <div style="text-align: center;">5. About Us</div>
        </div>
        <p style="text-align: center; color: #666;">
        Informasi tim & mata kuliah
        </p>
    """, unsafe_allow_html=True)

st.write("---")

# Features Section - Simplified
st.markdown("<h2 style='text-align: center; color: #667eea;'>✨ Fitur Aplikasi</h2>", unsafe_allow_html=True)
st.write("")

st.markdown("""
<div class="card" style="max-width: 900px; margin: 0 auto;">
    <div class="card-title" style="text-align: center;">🚀 Fitur Utama Sistem</div>
    <div class="card-desc">
    <b>📥 Input & Preprocessing:</b> Upload dataset, handling missing values, feature engineering (Sleep Duration & Financial Stress), encoding categorical<br><br>
    <b>🤖 Machine Learning:</b> Random Forest Classification dengan parameter tuning, evaluasi lengkap (Accuracy, Confusion Matrix, Feature Importance)<br><br>
    <b>📊 Visualisasi:</b> Interactive charts (Plotly), correlation heatmap, box plots, distribution plots by Depression status<br><br>
    <b>💡 UI/UX:</b> User-friendly interface, progress indicators, session state management, responsive design
    </div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# Getting Started
st.markdown("<h2 style='text-align: center; color: #667eea;'>🚀 Cara Memulai</h2>", unsafe_allow_html=True)
st.write("")

st.info("""
**Langkah-langkah:**
1. 📤 Buka menu **Input Data** di sidebar
2. 📁 Upload dataset CSV Anda atau gunakan dataset default
3. 🔧 Lakukan **Preprocessing** untuk membersihkan data
4. 📈 Jalankan **Analysis** untuk training model Random Forest
5. 📊 Eksplorasi **Visualizations** untuk insight lebih dalam
6. ℹ️ Lihat **About Us** untuk info mata kuliah dan tim

**Tips:**
- Pastikan dataset memiliki kolom target bernama 'Depression'
- Gunakan fitur preprocessing secara berurutan untuk hasil optimal
- Eksperimen dengan parameter model untuk akurasi terbaik
""")

# Footer
st.write("")
st.write("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
        <p style="margin: 0;">
            <b>Tugas Besar Akuisisi Data</b><br>
            Sistem Analisis Depresi Mahasiswa menggunakan Machine Learning<br>
            <small>Dibuat dengan ❤️ menggunakan Streamlit & Scikit-learn</small>
        </p>
    </div>
""", unsafe_allow_html=True)
