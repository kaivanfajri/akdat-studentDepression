# 🧠 Sistem Analisis Depresi Mahasiswa

Tugas Besar Mata Kuliah Akuisisi Data - Sistem Analisis dan Prediksi Depresi pada Mahasiswa menggunakan Machine Learning

## 📋 Deskripsi Project

Project ini merupakan implementasi sistem analisis data untuk mengidentifikasi faktor-faktor yang mempengaruhi tingkat depresi pada mahasiswa. Menggunakan dataset dengan lebih dari 27,000 records, sistem ini menerapkan teknik machine learning (Random Forest Classification) untuk memprediksi dan menganalisis pola depresi berdasarkan berbagai variabel seperti tekanan akademik, pola tidur, kebiasaan makan, dan faktor-faktor lainnya.

## ✨ Fitur Utama

### 🏠 Home

-   Overview project dan tujuan analisis
-   Informasi dataset
-   Alur penggunaan aplikasi
-   Feature highlights

### 📤 Input Data

-   Upload dataset custom (.csv)
-   Gunakan dataset default
-   Preview dataset lengkap
-   Informasi kolom dan statistik data
-   Deteksi missing values dan duplicates

### 🔧 Preprocessing

-   Handling missing values (drop, fill mean, fill median, fill zero)
-   Remove duplicate rows
-   Encoding categorical variables (Label Encoding)
-   Scaling numerical data (Standard Scaler)
-   Preview sebelum dan sesudah preprocessing
-   Export processed data

### 📈 Analysis

-   Random Forest Classification model
-   Parameter tuning (n_estimators, max_depth, etc.)
-   Train-test split dengan stratified sampling
-   Model evaluation:
    -   Accuracy, Precision, Recall, F1-Score
    -   Confusion Matrix
    -   Classification Report
    -   Feature Importance
-   Export trained model (.pkl)

### 📊 Visualizations

-   Distribusi target (Depression vs No Depression)
-   Correlation heatmap
-   Box plots untuk outlier detection
-   Pair plots untuk relasi antar features
-   K-Means clustering analysis
-   Distribusi features (categorical & numerical)
-   Interactive charts dengan Plotly

### ℹ️ About Us

-   Informasi mata kuliah
-   Metodologi penelitian
-   Teknologi yang digunakan
-   Informasi tim pengembang

## 🛠️ Teknologi

-   **Python 3.8+**
-   **Streamlit** - Web framework untuk dashboard
-   **Pandas** - Data manipulation
-   **NumPy** - Numerical computing
-   **Scikit-learn** - Machine learning
-   **Matplotlib & Seaborn** - Data visualization
-   **Plotly** - Interactive visualizations
-   **Joblib** - Model serialization

## 📦 Instalasi

### 1. Clone atau Download Project

```bash
cd akdatStudentDepression
```

### 2. Buat Virtual Environment (Opsional tapi Direkomendasikan)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🚀 Cara Menjalankan

### Jalankan Aplikasi Streamlit

```bash
streamlit run Home.py
```

Aplikasi akan terbuka di browser pada `http://localhost:8501`

## 📁 Struktur Project

```
akdatStudentDepression/
├── Home.py                          # Halaman utama
├── pages/
│   ├── 1_Input_Data.py             # Upload & load dataset
│   ├── 2_Preprocessing.py          # Data preprocessing
│   ├── 3_Analysis.py               # Model training & evaluation
│   ├── 4_Visualizations.py         # Data visualizations
│   └── 5_About_Us.py               # Info tim & mata kuliah
├── data/                           # Folder untuk menyimpan data
│   └── processed_dataset.csv       # Data hasil preprocessing (generated)
├── model/                          # Folder untuk menyimpan model
│   └── random_forest_model.pkl     # Trained model (generated)
├── venv/                           # Virtual environment (optional)
├── student_depression_dataset.csv  # Dataset utama
├── requirements.txt                # Dependencies
└── README.md                       # Dokumentasi
```

## 📊 Dataset

**File**: `student_depression_dataset.csv`

**Jumlah Records**: ~27,000+ mahasiswa

**Features** (18 kolom):

-   `id` - ID mahasiswa
-   `Gender` - Jenis kelamin
-   `Age` - Usia
-   `City` - Kota asal
-   `Profession` - Profesi (Student/Working)
-   `Academic Pressure` - Tingkat tekanan akademik (1-5)
-   `Work Pressure` - Tingkat tekanan kerja (0-5)
-   `CGPA` - Grade Point Average
-   `Study Satisfaction` - Kepuasan belajar (1-5)
-   `Job Satisfaction` - Kepuasan kerja (0-5)
-   `Sleep Duration` - Durasi tidur
-   `Dietary Habits` - Kebiasaan makan
-   `Degree` - Tingkat pendidikan
-   `Have you ever had suicidal thoughts?` - Pemikiran bunuh diri
-   `Work/Study Hours` - Jam kerja/belajar per hari
-   `Financial Stress` - Tingkat stress finansial (1-5)
-   `Family History of Mental Illness` - Riwayat keluarga
-   `Depression` - **Target variable** (0 = No Depression, 1 = Depression)

## 🔄 Workflow Penggunaan

1. **Input Data**

    - Upload dataset atau gunakan dataset default
    - Lihat preview dan informasi dataset

2. **Preprocessing**

    - Pilih langkah preprocessing (missing values, duplicates, encoding, scaling)
    - Jalankan preprocessing
    - Download data hasil preprocessing

3. **Analysis**

    - Pilih features untuk training
    - Atur parameter model Random Forest
    - Training model
    - Evaluasi hasil dengan confusion matrix dan metrics
    - Download trained model

4. **Visualizations**

    - Eksplorasi berbagai visualisasi
    - Distribusi target dan features
    - Correlation analysis
    - K-Means clustering
    - Interactive charts

5. **About Us**
    - Lihat informasi lengkap tentang project dan tim

## 📈 Model Performance

Model yang digunakan: **Random Forest Classification**

**Default Parameters**:

-   n_estimators: 100
-   max_depth: 20
-   min_samples_split: 2
-   random_state: 42

**Expected Performance**:

-   Accuracy: ~85-90%
-   Precision: ~85-88%
-   Recall: ~85-90%
-   F1-Score: ~85-89%

_Note: Performance dapat bervariasi tergantung preprocessing dan parameter tuning_

## 🎯 Hasil Analisis

### Top Features yang Mempengaruhi Depresi:

1. Suicidal Thoughts
2. Academic Pressure
3. Sleep Duration
4. Financial Stress
5. Family History of Mental Illness
6. Work/Study Hours
7. CGPA
8. Dietary Habits

## 📝 Catatan Penting

-   Dataset harus memiliki kolom target bernama `Depression` (0/1)
-   Karakter '?', 'NA', 'N/A' akan dianggap sebagai missing values
-   Preprocessing harus dilakukan sebelum training model
-   Session state digunakan untuk menyimpan data antar halaman
-   Model dan data akan tersimpan di folder `model/` dan `data/`

## 🐛 Troubleshooting

### Error: ModuleNotFoundError

```bash
pip install -r requirements.txt
```

### Error: Dataset tidak ditemukan

Pastikan file `student_depression_dataset.csv` ada di root folder project

### Error: Port sudah digunakan

```bash
streamlit run Home.py --server.port 8502
```

### Clear Cache Streamlit

```bash
streamlit cache clear
```

## 👥 Tim Pengembang

-   **Anggota 1** - Project Lead & ML Engineer
-   **Anggota 2** - Data Analyst & Visualization
-   **Anggota 3** - UI/UX Designer & Developer

_Silakan sesuaikan dengan anggota tim Anda_

## 📚 Referensi

1. Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5-32.
2. Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python.
3. Streamlit Documentation: https://docs.streamlit.io/
4. Scikit-learn Documentation: https://scikit-learn.org/

## 📧 Kontak

-   **Email**: team@example.com
-   **GitHub**: github.com/yourrepo
-   **Universitas**: [Nama Universitas]

## 📄 License

Project ini dibuat untuk keperluan akademik (Tugas Besar Akuisisi Data).

---

**Dibuat dengan ❤️ untuk Tugas Besar Akuisisi Data**

© 2024 - All Rights Reserved
