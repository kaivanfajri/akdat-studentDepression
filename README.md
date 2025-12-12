# 🧠 Sistem Analisis Depresi Siswa/Mahasiswa

**Tugas Besar Mata Kuliah Akuisisi Data**

Sistem analisis dan prediksi depresi pada siswa/mahasiswa menggunakan Machine Learning (Random Forest Classification) dengan Streamlit Dashboard.

---

## 📋 Deskripsi Project

Project ini menganalisis faktor-faktor yang mempengaruhi tingkat depresi pada siswa/mahasiswa menggunakan dataset dengan 27,000+ records. Sistem ini menerapkan Machine Learning untuk memprediksi dan menganalisis pola depresi berdasarkan berbagai variabel seperti tekanan akademik, pola tidur, kebiasaan makan, dan faktor psikologis lainnya.

---

## 🚀 Quick Start Guide

**Pertama kali clone project ini? Ikuti checklist berikut:**

```
☐ 1. Clone project dari GitHub
☐ 2. Buka terminal/command prompt di folder project
☐ 3. Buat virtual environment: python -m venv venv
☐ 4. Aktivasi venv: .\venv\Scripts\Activate.ps1 (Windows) atau source venv/bin/activate (Linux/Mac)
☐ 5. Install dependencies: pip install -r requirements.txt
☐ 6. Jalankan aplikasi: streamlit run Home.py
☐ 7. Buka browser: http://localhost:8501
```

**⏱️ Estimasi waktu setup: 5-10 menit**

---

## 📦 Instalasi Lengkap

### Step 1: Clone Project

```bash
git clone https://github.com/kaivanfajri/akdat-studentDepression.git
cd akdat-studentDepression
```

**Alternatif:** Download ZIP dari GitHub, lalu extract dan buka terminal di folder tersebut.

### Step 2: Buat Virtual Environment

> **⚠️ PENTING:** Virtual environment (venv) TIDAK ikut di-upload ke GitHub. Anda HARUS membuat venv baru setiap kali clone project ini.

**Windows:**

```bash
python -m venv venv
```

**Linux/Mac:**

```bash
python3 -m venv venv
```

### Step 3: Aktivasi Virtual Environment

**Windows PowerShell:**

```bash
.\venv\Scripts\Activate.ps1
```

**Jika error "running scripts is disabled":**

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

**Windows CMD:**

```bash
venv\Scripts\activate.bat
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

**✅ Berhasil jika muncul `(venv)` di awal terminal:**

```
(venv) PS C:\...\akdat-studentDepression>
```

### Step 4: Install Dependencies

**Pastikan venv sudah aktif (ada `(venv)` di terminal), lalu:**

```bash
pip install -r requirements.txt
```

**Dependencies yang akan terinstall:**

-   streamlit==1.28.0
-   pandas==2.1.1
-   numpy==1.24.3
-   scikit-learn==1.3.1
-   joblib==1.3.2
-   matplotlib==3.8.0
-   seaborn==0.13.0
-   plotly==5.17.0

**⏳ Tunggu 2-5 menit hingga selesai (tergantung koneksi internet)**

### Step 5: Verifikasi Instalasi

```bash
pip list
```

Pastikan semua library di atas muncul dalam list.

---

## 🎯 Cara Menjalankan Aplikasi

### 1. Pastikan Virtual Environment Aktif

Cek ada `(venv)` di awal terminal. Jika tidak ada, aktivasi dulu:

```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate.bat

# Linux/Mac
source venv/bin/activate
```

### 2. Jalankan Streamlit

```bash
streamlit run Home.py
```

**❌ JANGAN menggunakan:**

-   ~~`streamlit run app.py`~~ (file app.py tidak ada!)
-   ~~`python Home.py`~~ (ini bukan cara jalankan Streamlit)

### 3. Buka Browser

Aplikasi akan otomatis terbuka di:

```
http://localhost:8501
```

Jika tidak otomatis, buka browser dan ketik URL di atas.

### 4. Menghentikan Aplikasi

Tekan `Ctrl + C` di terminal.

---

## 📁 Struktur Project

```
akdat-studentDepression/
│
├── Home.py                          # 🏠 Halaman utama (ENTRYPOINT)
│
├── pages/                           # 📂 Halaman-halaman Streamlit
│   ├── 1_Input_Data.py             # 📤 Upload & load dataset
│   ├── 2_Preprocessing.py          # 🔧 Cleaning & preprocessing data
│   ├── 3_Analysis.py               # 📈 Training model & evaluasi
│   ├── 4_Visualizations.py         # 📊 Visualisasi data & hasil
│   └── 5_About_Us.py               # ℹ️  Info tim & mata kuliah
│
├── data/                            # 📁 Folder untuk data (auto-generated)
│   └── processed_dataset.csv       # Data hasil preprocessing
│
├── model/                           # 🤖 Folder untuk model (auto-generated)
│   └── random_forest_model.pkl     # Model yang sudah di-training
│
├── venv/                            # 🐍 Virtual environment (TIDAK DI-COMMIT)
│
├── student_depression_dataset.csv   # 📊 Dataset utama (27,000+ records)
├── requirements.txt                 # 📋 List dependencies
├── .gitignore                       # 🚫 File yang diabaikan Git
└── README.md                        # 📖 Dokumentasi (file ini)
```

**Catatan:**

-   `Home.py` adalah **entry point** - file yang harus dijalankan
-   Folder `pages/` berisi halaman-halaman yang otomatis muncul di sidebar Streamlit
-   Folder `data/` dan `model/` akan otomatis dibuat saat aplikasi berjalan
-   Folder `venv/` **TIDAK** di-upload ke GitHub (ada di .gitignore)

---

## ✨ Fitur Aplikasi

### 🏠 Home

-   Overview project dan tujuan analisis
-   Gambaran umum dataset
-   Workflow aplikasi
-   Status indicator untuk setiap tahap

### 📤 Input Data

-   Upload dataset custom (file .csv)
-   Load dataset default
-   Preview dataset (tabel interaktif)
-   Informasi lengkap: jumlah baris, kolom, missing values, duplikat
-   Statistik deskriptif

### 🔧 Preprocessing

-   Handling missing values (drop, mean, median, zero)
-   Remove duplicate rows
-   Encoding categorical variables (Label Encoding)
-   Scaling numerical features (Standard Scaler)
-   Preview data sebelum & sesudah preprocessing
-   Download processed data

### 📈 Analysis

-   Random Forest Classification
-   Parameter tuning (n_estimators, max_depth, min_samples_split, dll)
-   Train-test split (adjustable ratio)
-   Model evaluation:
    -   Accuracy, Precision, Recall, F1-Score
    -   Confusion Matrix
    -   Classification Report
    -   Feature Importance (Top features yang berpengaruh)
-   Save/load trained model

### 📊 Visualizations

-   **Distribusi Target:** Bar chart & pie chart untuk kelas Depression
-   **Correlation Heatmap:** Korelasi antar features
-   **Box Plots:** Deteksi outliers
-   **Pair Plots:** Relasi antar features
-   **K-Means Clustering:** Clustering analysis dengan visualisasi
-   **Distribusi Features:** Histogram untuk setiap feature
-   Interactive charts dengan Plotly

### ℹ️ About Us

-   Informasi mata kuliah
-   Metodologi penelitian
-   Tech stack yang digunakan
-   Informasi tim pengembang

---

## 📊 Dataset

**Filename:** `student_depression_dataset.csv`

**Jumlah Records:** 27,000+ siswa/mahasiswa

**Jumlah Features:** 18 kolom

### Deskripsi Kolom:

| Kolom                                  | Deskripsi                                    | Tipe        |
| -------------------------------------- | -------------------------------------------- | ----------- |
| `id`                                   | ID unik mahasiswa                            | Integer     |
| `Gender`                               | Jenis kelamin (Male/Female)                  | Categorical |
| `Age`                                  | Usia mahasiswa                               | Numeric     |
| `City`                                 | Kota asal                                    | Categorical |
| `Profession`                           | Status (Student/Working Professional)        | Categorical |
| `Academic Pressure`                    | Tingkat tekanan akademik (1-5)               | Numeric     |
| `Work Pressure`                        | Tingkat tekanan kerja (0-5)                  | Numeric     |
| `CGPA`                                 | Nilai IPK (0-10)                             | Numeric     |
| `Study Satisfaction`                   | Kepuasan belajar (1-5)                       | Numeric     |
| `Job Satisfaction`                     | Kepuasan kerja (0-5)                         | Numeric     |
| `Sleep Duration`                       | Durasi tidur per hari                        | Categorical |
| `Dietary Habits`                       | Kebiasaan makan (Healthy/Moderate/Unhealthy) | Categorical |
| `Degree`                               | Tingkat pendidikan                           | Categorical |
| `Have you ever had suicidal thoughts?` | Riwayat pikiran bunuh diri (Yes/No)          | Categorical |
| `Work/Study Hours`                     | Jam kerja/belajar per hari                   | Numeric     |
| `Financial Stress`                     | Tingkat stress finansial (1-5)               | Numeric     |
| `Family History of Mental Illness`     | Riwayat keluarga (Yes/No)                    | Categorical |
| **`Depression`**                       | **TARGET: Depresi (0=No, 1=Yes)**            | **Binary**  |

---

## 🔄 Workflow Penggunaan

1. **📤 Input Data**

    - Upload dataset Anda atau gunakan dataset default
    - Lihat preview dan informasi dataset
    - Cek missing values dan duplicates

2. **🔧 Preprocessing**

    - Pilih metode handling missing values
    - Hapus duplikat (optional)
    - Encode categorical variables
    - Scale numerical features (optional)
    - Download processed data

3. **📈 Analysis**

    - Pilih features untuk training
    - Atur parameter Random Forest
    - Train model
    - Lihat evaluasi: accuracy, confusion matrix, feature importance
    - Save model untuk digunakan nanti

4. **📊 Visualizations**

    - Eksplorasi distribusi target
    - Analisis korelasi antar features
    - Deteksi outliers dengan box plots
    - K-Means clustering
    - Lihat relasi antar features

5. **ℹ️ About Us**
    - Info lengkap tentang project dan tim

---

## 🔄 Update Project dari GitHub

**Jika ada perubahan baru di repository:**

```bash
# 1. Cek status
git status

# 2. Pull perubahan terbaru
git pull origin main

# 3. Update dependencies (jika ada perubahan di requirements.txt)
pip install -r requirements.txt --upgrade

# 4. Jalankan aplikasi
streamlit run Home.py
```

---

## 🎓 Teknologi yang Digunakan

| Kategori                | Library/Framework | Versi  |
| ----------------------- | ----------------- | ------ |
| **Web Framework**       | Streamlit         | 1.28.0 |
| **Data Processing**     | Pandas            | 2.1.1  |
| **Numerical Computing** | NumPy             | 1.24.3 |
| **Machine Learning**    | Scikit-learn      | 1.3.1  |
| **Model Serialization** | Joblib            | 1.3.2  |
| **Visualization**       | Matplotlib        | 3.8.0  |
| **Statistical Viz**     | Seaborn           | 0.13.0 |
| **Interactive Charts**  | Plotly            | 5.17.0 |

**Python Version:** 3.8+

---

## 📈 Performance Model

**Model:** Random Forest Classification

**Default Parameters:**

-   `n_estimators`: 100 trees
-   `max_depth`: 20
-   `min_samples_split`: 2
-   `random_state`: 42
-   `n_jobs`: -1 (use all processors)

**Expected Performance:**

-   **Accuracy:** ~85-92%
-   **Precision:** ~85-90%
-   **Recall:** ~85-90%
-   **F1-Score:** ~85-90%

_Note: Performance bervariasi tergantung preprocessing dan parameter tuning_

### Top Features yang Berpengaruh:

1. **Suicidal Thoughts** (Most important)
2. Academic Pressure
3. Sleep Duration
4. Financial Stress
5. Family History of Mental Illness
6. Work/Study Hours
7. CGPA
8. Dietary Habits

---

## ❓ FAQ (Frequently Asked Questions)

### Q1: Kenapa harus membuat venv setiap kali clone project?

**A:** Virtual environment (venv) tidak di-upload ke GitHub karena:

-   Ukurannya besar (ratusan MB)
-   Bersifat lokal untuk setiap komputer
-   Ada di `.gitignore`

Jadi setiap kali clone, Anda harus membuat venv baru.

### Q2: Apa itu virtual environment dan kenapa penting?

**A:** Virtual environment adalah isolated Python environment yang:

-   Mengisolasi dependencies project ini dari project Python lain
-   Mencegah konflik versi library
-   Best practice dalam Python development

### Q3: Bagaimana cara tahu venv sudah aktif?

**A:** Lihat di awal terminal, ada `(venv)` seperti ini:

```
(venv) PS C:\Users\...\akdat-studentDepression>
```

### Q4: Lupa aktivasi venv, apa yang terjadi?

**A:** Error seperti:

-   `streamlit: command not found`
-   `ModuleNotFoundError: No module named 'streamlit'`

**Solusi:** Aktivasi venv dulu, baru jalankan aplikasi.

### Q5: Error "cannot be loaded because running scripts is disabled"?

**A:** Ini masalah Windows PowerShell. Solusi:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Q6: Cara keluar dari virtual environment?

**A:** Ketik `deactivate` di terminal.

### Q7: Dataset tidak ditemukan saat aplikasi jalan?

**A:** Pastikan file `student_depression_dataset.csv` ada di root folder project (sejajar dengan `Home.py`).

### Q8: Port 8501 sudah digunakan aplikasi lain?

**A:** Jalankan dengan port berbeda:

```bash
streamlit run Home.py --server.port 8502
```

### Q9: Aplikasi lambat atau freeze?

**A:** Coba clear cache:

```bash
streamlit cache clear
```

### Q10: Bisa pakai Python versi berapa?

**A:** Minimum Python 3.8. Recommended: Python 3.9 atau 3.10.

---

## 🐛 Troubleshooting

### Error: `streamlit: command not found`

**Penyebab:** Virtual environment belum aktif atau Streamlit belum terinstall.

**Solusi:**

```bash
# Aktivasi venv dulu
.\venv\Scripts\Activate.ps1  # Windows

# Install streamlit
pip install streamlit
```

### Error: `ModuleNotFoundError: No module named 'pandas'`

**Penyebab:** Dependencies belum terinstall atau venv belum aktif.

**Solusi:**

```bash
# Pastikan venv aktif (ada (venv) di terminal)
pip install -r requirements.txt
```

### Error: `FileNotFoundError: student_depression_dataset.csv`

**Penyebab:** Dataset tidak ada atau salah path.

**Solusi:**

-   Pastikan file `student_depression_dataset.csv` ada di root folder
-   Cek typo di nama file
-   Download dataset dari repository jika tidak ada

### Error: `PermissionError` saat save model

**Penyebab:** Folder `model/` tidak ada atau tidak punya permission.

**Solusi:**

```bash
mkdir model  # Buat folder model manual
```

### Error: Aplikasi tidak bisa dibuka di browser

**Penyebab:** Port 8501 sudah dipakai atau firewall.

**Solusi:**

```bash
# Gunakan port lain
streamlit run Home.py --server.port 8502

# Atau cek apa yang pakai port 8501
netstat -ano | findstr :8501  # Windows
lsof -i :8501  # Linux/Mac
```

### Error: `cannot be loaded because running scripts is disabled`

**Penyebab:** Windows PowerShell execution policy terlalu strict.

**Solusi:**

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Aplikasi jalan tapi page blank/error

**Solusi:**

```bash
# Clear cache dan cookies browser
# Atau clear Streamlit cache
streamlit cache clear

# Restart aplikasi
Ctrl+C  # Stop aplikasi
streamlit run Home.py  # Start lagi
```

### Dependencies terinstall tapi masih error

**Solusi:**

```bash
# Reinstall semua dependencies
pip uninstall -r requirements.txt -y
pip install -r requirements.txt

# Atau upgrade semua
pip install -r requirements.txt --upgrade
```

---

## 📝 Catatan Penting

1. **File yang HARUS ada:**

    - `Home.py` - Entry point aplikasi
    - `student_depression_dataset.csv` - Dataset
    - `requirements.txt` - List dependencies
    - `pages/` folder dengan 5 file Python

2. **File yang TIDAK di-upload ke GitHub:**

    - Folder `venv/` - Virtual environment
    - Folder `__pycache__/` - Python cache
    - File `.pyc` - Compiled Python

3. **Preprocessing:**

    - Harus dilakukan sebelum training model
    - Session state digunakan untuk simpan data antar halaman
    - Karakter `?`, `NA`, `N/A` dianggap missing values

4. **Model Training:**

    - Preprocessing harus selesai dulu
    - Model disimpan sebagai `.pkl` file
    - Bisa di-load kembali di session berikutnya

5. **Dataset Requirements:**
    - Harus ada kolom bernama `Depression` (target)
    - Format: CSV dengan header
    - Encoding: UTF-8

---

## 👥 Tim Pengembang

**Tugas Besar Akuisisi Data 2025**

-   **[Nama Anggota 1]** - Project Lead & ML Engineer
-   **[Nama Anggota 2]** - Data Analyst & Preprocessing
-   **[Nama Anggota 3]** - UI/UX & Visualization Developer

_Sesuaikan dengan anggota tim Anda_

---

## 📚 Referensi & Resources

-   **Streamlit Documentation:** https://docs.streamlit.io/
-   **Scikit-learn Documentation:** https://scikit-learn.org/
-   **Pandas Documentation:** https://pandas.pydata.org/
-   **Random Forest Algorithm:** https://scikit-learn.org/stable/modules/ensemble.html#forest

---

## 📄 Lisensi

Project ini dibuat untuk keperluan **akademik** (Tugas Besar Mata Kuliah Akuisisi Data).

**For Educational Purpose Only**

---

## 🆘 Butuh Bantuan?

Jika mengalami masalah:

1. Baca **FAQ** dan **Troubleshooting** di atas
2. Cek apakah sudah mengikuti **semua langkah instalasi**
3. Pastikan **venv aktif** sebelum jalankan aplikasi
4. Cek **struktur folder** sudah benar

---

**Made with ❤️ for Akuisisi Data**

_Last Updated: December 12, 2025_
