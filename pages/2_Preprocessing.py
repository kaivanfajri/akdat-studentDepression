import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

st.set_page_config(page_title="Preprocessing", page_icon="🔧", layout="wide")

# Header
st.markdown("""
    <div style="
        background: linear-gradient(90deg, #667eea, #764ba2);
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 20px;">
        <h2 style="margin: 0;">🔧 Data Preprocessing</h2>
        <p style="font-size:16px; margin:5px 0 0 0;">
           Membersihkan dan Mempersiapkan Data untuk Analisis
        </p>
    </div>
""", unsafe_allow_html=True)

# Check if data is loaded
if 'data_loaded' not in st.session_state or not st.session_state['data_loaded']:
    st.error("❌ Data belum dimuat! Silakan upload dataset di menu **Input Data** terlebih dahulu.")
    st.stop()

# Get data from session state
df = st.session_state['df_current'].copy()

st.info("""
**Petunjuk:**
- Pilih langkah-langkah preprocessing yang ingin dilakukan
- Setiap langkah akan diterapkan secara berurutan
- Preview hasil preprocessing akan ditampilkan
- Data hasil preprocessing akan disimpan untuk tahap Analysis
""")

# Show original data
st.subheader("📊 Data Sebelum Preprocessing")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Jumlah Baris", df.shape[0])
with col2:
    st.metric("Jumlah Kolom", df.shape[1])
with col3:
    st.metric("Missing Values", df.isnull().sum().sum())
with col4:
    st.metric("Duplicate Rows", df.duplicated().sum())

with st.expander("👁️ Lihat Data Awal"):
    st.dataframe(df.head(10), use_container_width=True)

st.write("---")

# PREPROCESSING STEPS
st.subheader("⚙️ Pilih Langkah Preprocessing")

# Create tabs for preprocessing steps
tab1, tab2, tab3, tab4 = st.tabs([
    "1️⃣ Missing Values", 
    "2️⃣ Duplicate Rows", 
    "3️⃣ Encoding Categorical", 
    "4️⃣ Review & Apply"
])

# Initialize preprocessing options in session state
if 'preprocessing_steps' not in st.session_state:
    st.session_state['preprocessing_steps'] = {
        'handle_missing': False,
        'missing_method': 'drop',
        'remove_duplicates': False,
        'encode_categorical': False
    }

# TAB 1: Handle Missing Values
with tab1:
    st.markdown("### 🔍 Deteksi Missing Values")
    
    missing_info = df.isnull().sum()
    missing_info = missing_info[missing_info > 0]
    
    if len(missing_info) > 0:
        st.warning(f"⚠️ Ditemukan {df.isnull().sum().sum()} missing values di {len(missing_info)} kolom")
        
        # Show missing values detail
        missing_df = pd.DataFrame({
            'Kolom': missing_info.index,
            'Jumlah Missing': missing_info.values,
            'Persentase (%)': (missing_info.values / len(df) * 100).round(2)
        })
        st.dataframe(missing_df, use_container_width=True)
        
        # Options for handling missing values
        st.markdown("### ⚙️ Pilih Metode Penanganan")
        
        handle_missing = st.checkbox(
            "Tangani Missing Values",
            value=st.session_state['preprocessing_steps']['handle_missing']
        )
        st.session_state['preprocessing_steps']['handle_missing'] = handle_missing
        
        if handle_missing:
            missing_method = st.radio(
                "Pilih metode:",
                ["Drop baris dengan missing values", 
                 "Isi dengan mean (untuk numerik) dan mode (untuk kategorikal)",
                 "Isi dengan median (untuk numerik) dan mode (untuk kategorikal)",
                 "Isi dengan nilai 0"],
                index=0
            )
            
            if missing_method == "Drop baris dengan missing values":
                st.session_state['preprocessing_steps']['missing_method'] = 'drop'
            elif "mean" in missing_method:
                st.session_state['preprocessing_steps']['missing_method'] = 'mean'
            elif "median" in missing_method:
                st.session_state['preprocessing_steps']['missing_method'] = 'median'
            else:
                st.session_state['preprocessing_steps']['missing_method'] = 'zero'
            
            st.info(f"✅ Metode terpilih: **{missing_method}**")
    else:
        st.success("✅ Tidak ada missing values dalam dataset!")

# TAB 2: Handle Duplicates
with tab2:
    st.markdown("### 🔍 Deteksi Duplicate Rows")
    
    n_duplicates = df.duplicated().sum()
    
    if n_duplicates > 0:
        st.warning(f"⚠️ Ditemukan {n_duplicates} baris duplikat ({n_duplicates/len(df)*100:.2f}%)")
        
        # Show duplicate rows
        if st.checkbox("Tampilkan baris duplikat"):
            duplicate_rows = df[df.duplicated(keep=False)]
            st.dataframe(duplicate_rows, use_container_width=True)
        
        # Option to remove duplicates
        remove_duplicates = st.checkbox(
            "Hapus baris duplikat",
            value=st.session_state['preprocessing_steps']['remove_duplicates']
        )
        st.session_state['preprocessing_steps']['remove_duplicates'] = remove_duplicates
        
        if remove_duplicates:
            st.info("✅ Baris duplikat akan dihapus")
    else:
        st.success("✅ Tidak ada baris duplikat dalam dataset!")

# TAB 3: Encode Categorical Variables
with tab3:
    st.markdown("### 🔤 Encoding Categorical Variables")
    
    # Identify categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    if len(categorical_cols) > 0:
        st.info(f"📋 Ditemukan {len(categorical_cols)} kolom kategorikal: {', '.join(categorical_cols)}")
        
        # Show unique values for each categorical column
        with st.expander("👁️ Lihat Unique Values"):
            for col in categorical_cols:
                st.write(f"**{col}:** {df[col].nunique()} unique values")
                st.write(df[col].value_counts().head(10))
                st.write("---")
        
        # Option to encode
        encode_categorical = st.checkbox(
            "Encode kolom kategorikal menggunakan Label Encoding",
            value=st.session_state['preprocessing_steps']['encode_categorical'],
            help="Label Encoding akan mengubah kategori menjadi angka. Sleep Duration dan Financial Stress akan dikonversi dengan ordinal/numerical mapping yang sesuai."
        )
        st.session_state['preprocessing_steps']['encode_categorical'] = encode_categorical
        
        if encode_categorical:
            st.info("✅ Kolom kategorikal akan di-encode menggunakan Label Encoding")
            st.success("⚡ Sleep Duration akan dikonversi ke angka (4, 5.5, 7.5, 9 jam)")
            st.success("⚡ Financial Stress sudah dalam bentuk angka (1-5), akan dibersihkan")
            st.warning("⚠️ Catatan: Kolom target 'Depression' tidak akan di-encode karena sudah numerik")
    else:
        st.success("✅ Tidak ada kolom kategorikal yang perlu di-encode!")

# TAB 4: Review and Apply
with tab4:
    st.markdown("### 📋 Review Preprocessing Steps")
    
    # Show selected steps
    steps = st.session_state['preprocessing_steps']
    
    st.write("**Langkah-langkah yang akan diterapkan:**")
    
    step_count = 0
    if steps['handle_missing']:
        step_count += 1
        st.success(f"✅ {step_count}. Handle missing values: **{steps['missing_method']}**")
    
    if steps['remove_duplicates']:
        step_count += 1
        st.success(f"✅ {step_count}. Remove duplicate rows")
    
    if steps['encode_categorical']:
        step_count += 1
        st.success(f"✅ {step_count}. Encode categorical variables")
    
    if step_count == 0:
        st.warning("⚠️ Belum ada langkah preprocessing yang dipilih!")
    
    st.write("---")
    
    # Apply preprocessing button
    if st.button("🚀 Jalankan Preprocessing", type="primary", disabled=(step_count == 0)):
        
        with st.spinner("⏳ Sedang memproses data..."):
            df_processed = df.copy()
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            current_step = 0
            total_steps = step_count
            
            # Step 1: Handle missing values
            if steps['handle_missing']:
                current_step += 1
                progress_bar.progress(current_step / total_steps)
                status_text.text(f"Step {current_step}/{total_steps}: Handling missing values...")
                
                method = steps['missing_method']
                
                if method == 'drop':
                    df_processed = df_processed.dropna()
                elif method == 'mean':
                    # Fill numeric with mean
                    numeric_cols = df_processed.select_dtypes(include=['int64', 'float64']).columns
                    df_processed[numeric_cols] = df_processed[numeric_cols].fillna(df_processed[numeric_cols].mean())
                    # Fill categorical with mode
                    cat_cols = df_processed.select_dtypes(include=['object']).columns
                    for col in cat_cols:
                        df_processed[col] = df_processed[col].fillna(df_processed[col].mode()[0] if len(df_processed[col].mode()) > 0 else 'Unknown')
                elif method == 'median':
                    # Fill numeric with median
                    numeric_cols = df_processed.select_dtypes(include=['int64', 'float64']).columns
                    df_processed[numeric_cols] = df_processed[numeric_cols].fillna(df_processed[numeric_cols].median())
                    # Fill categorical with mode
                    cat_cols = df_processed.select_dtypes(include=['object']).columns
                    for col in cat_cols:
                        df_processed[col] = df_processed[col].fillna(df_processed[col].mode()[0] if len(df_processed[col].mode()) > 0 else 'Unknown')
                elif method == 'zero':
                    df_processed = df_processed.fillna(0)
            
            # Step 2: Remove duplicates
            if steps['remove_duplicates']:
                current_step += 1
                progress_bar.progress(current_step / total_steps)
                status_text.text(f"Step {current_step}/{total_steps}: Removing duplicates...")
                
                df_processed = df_processed.drop_duplicates()
            
            # Step 3: Encode categorical
            if steps['encode_categorical']:
                current_step += 1
                progress_bar.progress(current_step / total_steps)
                status_text.text(f"Step {current_step}/{total_steps}: Encoding categorical variables...")
                
                # Feature Engineering: Convert Sleep Duration to numerical
                if 'Sleep Duration' in df_processed.columns:
                    sleep_mapping = {
                        "Less than 5 hours": 4.0,
                        "'Less than 5 hours'": 4.0,
                        "5-6 hours": 5.5,
                        "'5-6 hours'": 5.5,
                        "7-8 hours": 7.5,
                        "'7-8 hours'": 7.5,
                        "More than 8 hours": 9.0,
                        "'More than 8 hours'": 9.0,
                        "Others": 6.0  # Default value
                    }
                    df_processed['Sleep Duration'] = df_processed['Sleep Duration'].map(sleep_mapping)
                    # Fill any unmapped values with median
                    if df_processed['Sleep Duration'].isnull().any():
                        df_processed['Sleep Duration'] = df_processed['Sleep Duration'].fillna(6.0)
                
                # Financial Stress is already numerical (1.0-5.0), convert to integer
                if 'Financial Stress' in df_processed.columns:
                    # Convert to numeric, handling '?' as NaN
                    df_processed['Financial Stress'] = pd.to_numeric(df_processed['Financial Stress'], errors='coerce')
                    # Fill NaN with median (3.0)
                    if df_processed['Financial Stress'].isnull().any():
                        df_processed['Financial Stress'] = df_processed['Financial Stress'].fillna(3.0)
                    # Convert to integer
                    df_processed['Financial Stress'] = df_processed['Financial Stress'].astype(int)
                
                # Get remaining categorical columns (exclude Sleep Duration and Financial Stress)
                categorical_cols = df_processed.select_dtypes(include=['object']).columns.tolist()
                
                # Save label encoders for later use
                label_encoders = {}
                
                for col in categorical_cols:
                    le = LabelEncoder()
                    df_processed[col] = le.fit_transform(df_processed[col].astype(str))
                    label_encoders[col] = le
                
                # Save encoders to session state
                st.session_state['label_encoders'] = label_encoders
            
            progress_bar.progress(1.0)
            status_text.text("✅ Preprocessing selesai!")
            
            # Save processed data
            st.session_state['df_processed'] = df_processed.copy()
            st.session_state['df_current'] = df_processed.copy()
            st.session_state['preprocessing_done'] = True
            
            # Save to data folder
            try:
                df_processed.to_csv('data/processed_dataset.csv', index=False)
            except:
                pass
        
        st.success("🎉 Preprocessing berhasil!")
        
        # Show results
        st.markdown("### 📊 Hasil Preprocessing")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Jumlah Baris", df_processed.shape[0], delta=df_processed.shape[0] - df.shape[0])
        with col2:
            st.metric("Jumlah Kolom", df_processed.shape[1])
        with col3:
            st.metric("Missing Values", df_processed.isnull().sum().sum())
        with col4:
            st.metric("Duplicate Rows", df_processed.duplicated().sum())
        
        # Show processed data
        st.subheader("👁️ Preview Data Setelah Preprocessing")
        st.dataframe(df_processed.head(10), use_container_width=True)
        
        st.info("""
        **Langkah Selanjutnya:**
        - Lanjut ke menu **📈 Analysis** untuk training model Random Forest
        - Data hasil preprocessing sudah tersimpan dan siap digunakan
        """)

# Show processed data if available
if 'preprocessing_done' in st.session_state and st.session_state['preprocessing_done']:
    st.write("---")
    st.success("✅ Data sudah diproses sebelumnya!")
    
    if st.checkbox("Tampilkan data hasil preprocessing"):
        df_proc = st.session_state['df_processed']
        st.dataframe(df_proc, use_container_width=True)
        
        # Stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Baris", df_proc.shape[0])
        with col2:
            st.metric("Kolom", df_proc.shape[1])
        with col3:
            st.metric("Missing", df_proc.isnull().sum().sum())
