import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Input Data", page_icon="📤", layout="wide")

# Header
st.markdown("""
    <div style="
        background: linear-gradient(90deg, #667eea, #764ba2);
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 20px;">
        <h2 style="margin: 0;">📤 Input Dataset</h2>
        <p style="font-size:16px; margin:5px 0 0 0;">
           Upload Dataset atau Gunakan Dataset Default
        </p>
    </div>
""", unsafe_allow_html=True)

# Info section
st.info("""
**Petunjuk:**
- Upload file CSV dengan format yang sesuai, atau
- Gunakan dataset default (student_depression_dataset.csv)
- Dataset harus memiliki kolom target bernama **'Depression'** (0 = No Depression, 1 = Depression)
- Setelah upload, data akan disimpan di session state untuk digunakan di halaman lain
""")

# Tabs untuk pilihan input
tab1, tab2 = st.tabs(["📁 Upload File CSV", "📂 Gunakan Dataset Default"])

# TAB 1: Upload CSV
with tab1:
    st.subheader("Upload File CSV")
    uploaded_file = st.file_uploader(
        "Pilih file CSV untuk dianalisis:",
        type=["csv"],
        help="Format: CSV dengan delimiter koma (,)"
    )
    
    if uploaded_file is not None:
        try:
            # Read CSV dengan handling karakter '?' sebagai NA
            df = pd.read_csv(uploaded_file, na_values=['?', 'NA', 'N/A', ''])
            
            st.success("✅ Dataset berhasil di-upload!")
            
            # Save ke session state
            st.session_state['df_original'] = df.copy()
            st.session_state['df_current'] = df.copy()
            st.session_state['data_loaded'] = True
            
            # Display info
            st.subheader("📊 Preview Dataset")
            st.dataframe(df.head(10), use_container_width=True)
            
            # Dataset statistics
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Jumlah Baris", df.shape[0])
            with col2:
                st.metric("Jumlah Kolom", df.shape[1])
            with col3:
                st.metric("Missing Values", df.isnull().sum().sum())
            with col4:
                st.metric("Duplicate Rows", df.duplicated().sum())
            
            # Column info
            st.subheader("ℹ️ Informasi Kolom")
            col_info = pd.DataFrame({
                'Nama Kolom': df.columns,
                'Tipe Data': df.dtypes.astype(str).values,
                'Missing Values': df.isnull().sum().values,
                'Unique Values': [df[col].nunique() for col in df.columns]
            })
            st.dataframe(col_info, use_container_width=True)
            
            # Check if Depression column exists
            if 'Depression' in df.columns:
                st.success("✅ Kolom target 'Depression' ditemukan!")
                
                # Show depression distribution
                depression_counts = df['Depression'].value_counts()
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("No Depression (0)", f"{depression_counts.get(0, 0):,}")
                with col2:
                    st.metric("Depression (1)", f"{depression_counts.get(1, 0):,}")
            else:
                st.warning("⚠️ Kolom target 'Depression' tidak ditemukan! Pastikan dataset memiliki kolom ini.")
            
            # Statistical summary
            with st.expander("📈 Statistik Deskriptif"):
                st.dataframe(df.describe(), use_container_width=True)
            
            # Show data types
            with st.expander("🔤 Kolom Kategorikal & Numerikal"):
                categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
                numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Kolom Kategorikal:**")
                    st.write(categorical_cols if categorical_cols else "Tidak ada")
                with col2:
                    st.write("**Kolom Numerikal:**")
                    st.write(numerical_cols if numerical_cols else "Tidak ada")
                    
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan saat membaca file: {e}")

# TAB 2: Use Default Dataset
with tab2:
    st.subheader("Dataset Default")
    
    # Path to default dataset
    default_path = "student_depression_dataset.csv"
    
    if os.path.exists(default_path):
        st.info(f"📂 Dataset default tersedia: `{default_path}`")
        
        if st.button("🔄 Load Dataset Default", type="primary"):
            try:
                # Read default dataset
                df = pd.read_csv(default_path, na_values=['?', 'NA', 'N/A', ''])
                
                st.success("✅ Dataset default berhasil di-load!")
                
                # Save to session state
                st.session_state['df_original'] = df.copy()
                st.session_state['df_current'] = df.copy()
                st.session_state['data_loaded'] = True
                
                # Display info
                st.subheader("📊 Preview Dataset")
                st.dataframe(df.head(10), use_container_width=True)
                
                # Dataset statistics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Jumlah Baris", df.shape[0])
                with col2:
                    st.metric("Jumlah Kolom", df.shape[1])
                with col3:
                    st.metric("Missing Values", df.isnull().sum().sum())
                with col4:
                    st.metric("Duplicate Rows", df.duplicated().sum())
                
                # Column info
                st.subheader("ℹ️ Informasi Kolom")
                col_info = pd.DataFrame({
                    'Nama Kolom': df.columns,
                    'Tipe Data': df.dtypes.astype(str).values,
                    'Missing Values': df.isnull().sum().values,
                    'Unique Values': [df[col].nunique() for col in df.columns]
                })
                st.dataframe(col_info, use_container_width=True)
                
                # Check Depression column
                if 'Depression' in df.columns:
                    st.success("✅ Kolom target 'Depression' ditemukan!")
                    
                    # Show depression distribution
                    depression_counts = df['Depression'].value_counts()
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.metric("No Depression (0)", f"{depression_counts.get(0, 0):,}")
                    with col2:
                        st.metric("Depression (1)", f"{depression_counts.get(1, 0):,}")
                
                # Statistical summary
                with st.expander("📈 Statistik Deskriptif"):
                    st.dataframe(df.describe(), use_container_width=True)
                
                # Show data types
                with st.expander("🔤 Kolom Kategorikal & Numerikal"):
                    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
                    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("**Kolom Kategorikal:**")
                        st.write(categorical_cols if categorical_cols else "Tidak ada")
                    with col2:
                        st.write("**Kolom Numerikal:**")
                        st.write(numerical_cols if numerical_cols else "Tidak ada")
                        
            except Exception as e:
                st.error(f"❌ Terjadi kesalahan saat membaca file: {e}")
    else:
        st.error(f"❌ File default tidak ditemukan di path: `{default_path}`")
        st.info("Silakan upload dataset menggunakan tab **Upload File CSV**")

# Show current status
st.write("---")
st.subheader("📋 Status Data")

if 'data_loaded' in st.session_state and st.session_state['data_loaded']:
    st.success("✅ Data telah dimuat dan siap untuk diproses!")
    st.info("""
    **Langkah Selanjutnya:**
    - Lanjut ke menu **🔧 Preprocessing** untuk membersihkan data
    - Atau lihat data yang sudah dimuat di bawah ini
    """)
    
    if st.checkbox("Tampilkan data yang dimuat"):
        df_current = st.session_state['df_current']
        st.dataframe(df_current, use_container_width=True)
else:
    st.warning("⚠️ Belum ada data yang dimuat. Silakan upload atau gunakan dataset default.")
