import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Visualizations", page_icon="📊", layout="wide")

# Header
st.markdown("""
    <div style="
        background: linear-gradient(90deg, #667eea, #764ba2);
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 20px;">
        <h2 style="margin: 0;">📊 Data Visualizations</h2>
        <p style="font-size:16px; margin:5px 0 0 0;">
           Eksplorasi & Visualisasi Data Depression
        </p>
    </div>
""", unsafe_allow_html=True)

# Check if data is available
if 'df_original' not in st.session_state or st.session_state['df_original'] is None:
    st.error("❌ Data belum dimuat! Silakan upload dataset di menu **Input Data** terlebih dahulu.")
    st.stop()

# Get data (use original before preprocessing for better visualization)
df = st.session_state['df_original'].copy()

st.info("""
**Petunjuk:**
- Visualisasi menggunakan **data original** (sebelum preprocessing) untuk kemudahan interpretasi
- Pilih jenis visualisasi yang ingin dilihat
- Setiap visualisasi memberikan insight berbeda tentang data
- Gunakan interactive charts untuk eksplorasi lebih detail
""")

# Show data info
st.subheader("📊 Dataset Overview")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Samples", df.shape[0])
with col2:
    st.metric("Total Features", df.shape[1])
with col3:
    st.metric("Missing Values", df.isnull().sum().sum())
with col4:
    if 'Depression' in df.columns:
        st.metric("Depression Cases", df['Depression'].sum())

st.write("---")

# Visualization Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Distribusi Target",
    "🔥 Correlation Heatmap",
    "📦 Box Plots",
    "📈 Feature Distributions"
])

# TAB 1: Target Distribution
with tab1:
    st.subheader("📊 Distribusi Target: Depression")
    
    if 'Depression' in df.columns:
        depression_counts = df['Depression'].value_counts()
        
        # Create columns for layout
        col1, col2 = st.columns(2)
        
        with col1:
            # Pie chart
            fig = px.pie(
                values=depression_counts.values,
                names=['No Depression', 'Depression'],
                title='Distribusi Kasus Depresi',
                color_discrete_sequence=['#4CAF50', '#F44336'],
                hole=0.3
            )
            fig.update_traces(textposition='inside', textinfo='percent+label+value')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Bar chart
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.countplot(data=df, x='Depression', palette=['#4CAF50', '#F44336'], ax=ax)
            ax.set_xticklabels(['No Depression', 'Depression'])
            ax.set_xlabel('Depression Status')
            ax.set_ylabel('Count')
            ax.set_title('Jumlah Kasus per Kategori')
            
            # Add value labels
            for container in ax.containers:
                ax.bar_label(container)
            
            st.pyplot(fig)
        
        # Statistics
        st.markdown("### 📈 Statistik")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Samples", len(df))
        with col2:
            no_depression = depression_counts.get(0, 0)
            st.metric("No Depression", f"{no_depression} ({no_depression/len(df)*100:.1f}%)")
        with col3:
            depression = depression_counts.get(1, 0)
            st.metric("Depression", f"{depression} ({depression/len(df)*100:.1f}%)")
    else:
        st.error("Kolom 'Depression' tidak ditemukan!")

# TAB 2: Correlation Heatmap
with tab2:
    st.subheader("🔥 Correlation Heatmap")
    
    # Get numerical columns only
    numerical_df = df.select_dtypes(include=['int64', 'float64'])
    
    if len(numerical_df.columns) > 1:
        # Calculate correlation
        corr = numerical_df.corr()
        
        # Create heatmap
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0,
                    square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
        ax.set_title('Correlation Matrix of Numerical Features', fontsize=16, pad=20)
        plt.tight_layout()
        st.pyplot(fig)
        
        # Show highest correlations with Depression
        if 'Depression' in corr.columns:
            st.markdown("### 🎯 Korelasi Tertinggi dengan Depression")
            
            depression_corr = corr['Depression'].sort_values(ascending=False)
            depression_corr = depression_corr.drop('Depression')
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Positive Correlation:**")
                positive_corr = depression_corr[depression_corr > 0].head(5)
                for feature, value in positive_corr.items():
                    st.write(f"• {feature}: {value:.3f}")
            
            with col2:
                st.markdown("**Negative Correlation:**")
                negative_corr = depression_corr[depression_corr < 0].head(5)
                for feature, value in negative_corr.items():
                    st.write(f"• {feature}: {value:.3f}")
    else:
        st.warning("Tidak cukup kolom numerikal untuk membuat correlation heatmap")

# TAB 3: Box Plots
with tab3:
    st.subheader("📦 Box Plots - Deteksi Outliers")
    
    # Get numerical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    # Remove ID columns
    numerical_cols = [col for col in numerical_cols if col.lower() not in ['id', 'index']]
    
    if len(numerical_cols) > 0:
        # Select features for box plot
        selected_feature = st.selectbox(
            "Pilih feature untuk box plot:",
            numerical_cols
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Box plot without grouping
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.boxplot(data=df, y=selected_feature, color='skyblue', ax=ax)
            ax.set_title(f'Box Plot: {selected_feature}')
            st.pyplot(fig)
        
        with col2:
            # Box plot grouped by Depression if available
            if 'Depression' in df.columns:
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.boxplot(data=df, x='Depression', y=selected_feature, 
                           palette=['#4CAF50', '#F44336'], ax=ax)
                ax.set_xticklabels(['No Depression', 'Depression'])
                ax.set_title(f'Box Plot: {selected_feature} by Depression Status')
                st.pyplot(fig)
        
        # Multiple box plots
        st.markdown("### 📊 Multiple Box Plots")
        
        # Select multiple features
        n_features = st.slider("Jumlah features untuk ditampilkan:", 4, min(12, len(numerical_cols)), 6)
        selected_features = numerical_cols[:n_features]
        
        # Create subplots
        n_cols = 3
        n_rows = (n_features + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4))
        axes = axes.flatten() if n_features > 1 else [axes]
        
        for idx, feature in enumerate(selected_features):
            sns.boxplot(data=df, y=feature, color='lightblue', ax=axes[idx])
            axes[idx].set_title(f'{feature}')
        
        # Hide empty subplots
        for idx in range(n_features, len(axes)):
            axes[idx].axis('off')
        
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.warning("Tidak ada kolom numerikal untuk box plot")

# TAB 4: Feature Distributions
with tab4:
    st.subheader("📈 Distribusi Features")
    
    # Categorical features distribution
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    numerical_cols = [col for col in numerical_cols if col.lower() not in ['id', 'index']]
    
    # Categorical distributions
    if len(categorical_cols) > 0:
        st.markdown("### 📊 Distribusi Features Kategorikal")
        
        selected_cat = st.selectbox("Pilih feature kategorikal:", categorical_cols)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Count plot
            fig, ax = plt.subplots(figsize=(10, 6))
            value_counts = df[selected_cat].value_counts().head(10)
            sns.barplot(x=value_counts.values, y=value_counts.index, palette='viridis', ax=ax)
            ax.set_xlabel('Count')
            ax.set_ylabel(selected_cat)
            ax.set_title(f'Distribusi {selected_cat} (Top 10)')
            
            # Add value labels
            for i, v in enumerate(value_counts.values):
                ax.text(v, i, f' {v}', va='center')
            
            st.pyplot(fig)
        
        with col2:
            # Pie chart
            fig = px.pie(
                values=value_counts.values,
                names=value_counts.index,
                title=f'Proporsi {selected_cat} (Top 10)',
                color_discrete_sequence=px.colors.sequential.Viridis
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Group by Depression if available
        if 'Depression' in df.columns:
            st.markdown(f"### 🎯 {selected_cat} vs Depression Status")
            
            # Crosstab
            crosstab = pd.crosstab(df[selected_cat], df['Depression'], normalize='index') * 100
            
            if len(crosstab) <= 15:  # Only show if not too many categories
                fig, ax = plt.subplots(figsize=(12, 6))
                crosstab.plot(kind='bar', ax=ax, color=['#4CAF50', '#F44336'])
                ax.set_xlabel(selected_cat)
                ax.set_ylabel('Percentage (%)')
                ax.set_title(f'{selected_cat} vs Depression Status')
                ax.legend(['No Depression', 'Depression'])
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.info("Terlalu banyak kategori untuk ditampilkan dalam grouped chart")
    
    # Numerical distributions
    if len(numerical_cols) > 0:
        st.markdown("### 📈 Distribusi Features Numerikal")
        
        selected_num = st.selectbox("Pilih feature numerikal:", numerical_cols)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Histogram
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.hist(df[selected_num].dropna(), bins=30, color='skyblue', edgecolor='black')
            ax.set_xlabel(selected_num)
            ax.set_ylabel('Frequency')
            ax.set_title(f'Histogram: {selected_num}')
            ax.axvline(df[selected_num].mean(), color='red', linestyle='--', label=f'Mean: {df[selected_num].mean():.2f}')
            ax.legend()
            st.pyplot(fig)
        
        with col2:
            # KDE plot
            fig, ax = plt.subplots(figsize=(10, 6))
            
            if 'Depression' in df.columns:
                # KDE by Depression status
                for depression_val in df['Depression'].unique():
                    subset = df[df['Depression'] == depression_val][selected_num].dropna()
                    label = 'Depression' if depression_val == 1 else 'No Depression'
                    color = '#F44336' if depression_val == 1 else '#4CAF50'
                    subset.plot(kind='kde', ax=ax, label=label, color=color, linewidth=2)
                
                ax.set_xlabel(selected_num)
                ax.set_ylabel('Density')
                ax.set_title(f'Density Plot: {selected_num} by Depression Status')
                ax.legend()
            else:
                df[selected_num].plot(kind='kde', ax=ax, color='blue', linewidth=2)
                ax.set_xlabel(selected_num)
                ax.set_ylabel('Density')
                ax.set_title(f'Density Plot: {selected_num}')
            
            st.pyplot(fig)
        
        # Statistics
        st.markdown("### 📊 Statistik Deskriptif")
        
        stats = df[selected_num].describe()
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Mean", f"{stats['mean']:.2f}")
        with col2:
            st.metric("Median", f"{stats['50%']:.2f}")
        with col3:
            st.metric("Std Dev", f"{stats['std']:.2f}")
        with col4:
            st.metric("Min", f"{stats['min']:.2f}")
        with col5:
            st.metric("Max", f"{stats['max']:.2f}")

st.write("---")
st.success("✅ Visualisasi data selesai! Gunakan insight ini untuk memahami data lebih baik.")
