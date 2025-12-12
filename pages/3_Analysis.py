import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Analysis", page_icon="📈", layout="wide")

# Header
st.markdown("""
    <div style="
        background: linear-gradient(90deg, #667eea, #764ba2);
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 20px;">
        <h2 style="margin: 0;">📈 Model Analysis & Training</h2>
        <p style="font-size:16px; margin:5px 0 0 0;">
           Training Random Forest Classification Model
        </p>
    </div>
""", unsafe_allow_html=True)

# Check if data is preprocessed
if 'preprocessing_done' not in st.session_state or not st.session_state['preprocessing_done']:
    st.error("❌ Data belum diproses! Silakan lakukan **Preprocessing** terlebih dahulu.")
    st.info("Langkah-langkah: **Input Data** → **Preprocessing** → **Analysis**")
    st.stop()

# Get preprocessed data
df = st.session_state['df_processed'].copy()

st.info("""
**Petunjuk:**
- Pilih fitur (features) untuk training model
- Atur parameter Random Forest (n_estimators, max_depth, dll)
- Jalankan training dan evaluasi model
- Model akan dievaluasi dengan Confusion Matrix, Classification Report, dan Feature Importance
""")

# Show data info
st.subheader("📊 Data untuk Training")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Samples", df.shape[0])
with col2:
    st.metric("Total Features", df.shape[1])
with col3:
    if 'Depression' in df.columns:
        st.metric("Target Column", "Depression ✅")
    else:
        st.metric("Target Column", "Not Found ❌")

with st.expander("👁️ Lihat Data"):
    st.dataframe(df.head(10), use_container_width=True)

st.write("---")

# Check if Depression column exists
if 'Depression' not in df.columns:
    st.error("❌ Kolom target 'Depression' tidak ditemukan dalam dataset!")
    st.stop()

# Feature Selection
st.subheader("🎯 Pemilihan Features & Target")

# All columns except target
all_columns = df.columns.tolist()
if 'Depression' in all_columns:
    all_columns.remove('Depression')

# Remove ID column if exists
id_cols = [col for col in all_columns if col.lower() in ['id', 'index']]
for col in id_cols:
    all_columns.remove(col)

st.write(f"**Kolom tersedia:** {len(all_columns)} features")

# Feature selection options
selection_method = st.radio(
    "Pilih metode pemilihan features:",
    ["Gunakan semua features", "Pilih features manual"]
)

if selection_method == "Gunakan semua features":
    selected_features = all_columns
else:
    selected_features = st.multiselect(
        "Pilih features untuk training:",
        all_columns,
        default=all_columns
    )

if len(selected_features) == 0:
    st.warning("⚠️ Silakan pilih minimal 1 feature untuk training!")
    st.stop()

st.success(f"✅ Features terpilih: **{len(selected_features)}** features")

with st.expander("📋 Daftar Features Terpilih"):
    st.write(selected_features)

st.write("---")

# Model Parameters
st.subheader("⚙️ Parameter Model Random Forest")

col1, col2, col3 = st.columns(3)

with col1:
    n_estimators = st.slider(
        "Number of Trees (n_estimators)",
        min_value=10,
        max_value=200,
        value=100,
        step=10,
        help="Jumlah decision tree dalam forest"
    )

with col2:
    max_depth = st.slider(
        "Max Depth",
        min_value=5,
        max_value=50,
        value=20,
        step=5,
        help="Kedalaman maksimum setiap tree"
    )

with col3:
    test_size = st.slider(
        "Test Size (%)",
        min_value=10,
        max_value=40,
        value=20,
        step=5,
        help="Persentase data untuk testing"
    )

col4, col5 = st.columns(2)

with col4:
    random_state = st.number_input(
        "Random State",
        min_value=0,
        max_value=100,
        value=42,
        help="Untuk reproducibility"
    )

with col5:
    min_samples_split = st.slider(
        "Min Samples Split",
        min_value=2,
        max_value=20,
        value=2,
        help="Minimum samples required to split a node"
    )

st.write("---")

# Train Model Button
st.subheader("🚀 Training Model")

if st.button("🎯 Mulai Training Model", type="primary"):
    
    with st.spinner("⏳ Training model... Mohon tunggu..."):
        
        # Prepare data
        X = df[selected_features]
        y = df['Depression']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, 
            test_size=test_size/100, 
            random_state=random_state,
            stratify=y
        )
        
        # Training info
        st.info(f"""
        **Data Split:**
        - Training set: {len(X_train)} samples ({100-test_size}%)
        - Test set: {len(X_test)} samples ({test_size}%)
        """)
        
        # Create progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Initialize model
        status_text.text("Initializing Random Forest model...")
        progress_bar.progress(0.2)
        
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            random_state=random_state,
            n_jobs=-1
        )
        
        # Train model
        status_text.text("Training model...")
        progress_bar.progress(0.4)
        
        model.fit(X_train, y_train)
        
        # Predict
        status_text.text("Making predictions...")
        progress_bar.progress(0.6)
        
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        
        # Calculate metrics
        status_text.text("Calculating metrics...")
        progress_bar.progress(0.8)
        
        train_accuracy = accuracy_score(y_train, y_pred_train)
        test_accuracy = accuracy_score(y_test, y_pred_test)
        
        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred_test)
        
        # Classification report
        report = classification_report(y_test, y_pred_test, output_dict=True)
        
        # Feature importance
        feature_importance = pd.DataFrame({
            'Feature': selected_features,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        progress_bar.progress(1.0)
        status_text.text("✅ Training selesai!")
        
        # Save model and results to session state
        st.session_state['model'] = model
        st.session_state['X_train'] = X_train
        st.session_state['X_test'] = X_test
        st.session_state['y_train'] = y_train
        st.session_state['y_test'] = y_test
        st.session_state['y_pred_test'] = y_pred_test
        st.session_state['train_accuracy'] = train_accuracy
        st.session_state['test_accuracy'] = test_accuracy
        st.session_state['confusion_matrix'] = cm
        st.session_state['classification_report'] = report
        st.session_state['feature_importance'] = feature_importance
        st.session_state['model_trained'] = True
        
        # Save model to file
        try:
            joblib.dump(model, 'model/random_forest_model.pkl')
        except:
            pass
    
    st.success("🎉 Model berhasil di-training!")
    
    st.write("---")
    
    # Display Results
    st.subheader("📊 Hasil Evaluasi Model")
    
    # Accuracy metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Training Accuracy",
            f"{train_accuracy*100:.2f}%",
            help="Akurasi pada data training"
        )
    
    with col2:
        st.metric(
            "Test Accuracy",
            f"{test_accuracy*100:.2f}%",
            delta=f"{(test_accuracy - train_accuracy)*100:.2f}%",
            help="Akurasi pada data testing"
        )
    
    with col3:
        st.metric(
            "Precision",
            f"{report['weighted avg']['precision']*100:.2f}%",
            help="Weighted average precision"
        )
    
    with col4:
        st.metric(
            "Recall",
            f"{report['weighted avg']['recall']*100:.2f}%",
            help="Weighted average recall"
        )
    
    # Confusion Matrix
    st.subheader("🔲 Confusion Matrix")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['No Depression', 'Depression'],
                yticklabels=['No Depression', 'Depression'])
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.set_title('Confusion Matrix')
    st.pyplot(fig)
    
    # Classification Report
    st.subheader("📋 Classification Report")
    
    report_df = pd.DataFrame(report).T
    report_df = report_df.drop(['accuracy'], errors='ignore')
    
    # Format the report
    st.dataframe(
        report_df.style.format("{:.3f}").background_gradient(cmap='RdYlGn', subset=['precision', 'recall', 'f1-score']),
        use_container_width=True
    )
    
    # Feature Importance
    st.subheader("⭐ Feature Importance")
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot top 15 features
    top_n = min(15, len(feature_importance))
    top_features = feature_importance.head(top_n)
    
    ax.barh(range(top_n), top_features['Importance'])
    ax.set_yticks(range(top_n))
    ax.set_yticklabels(top_features['Feature'])
    ax.set_xlabel('Importance')
    ax.set_title(f'Top {top_n} Most Important Features')
    ax.invert_yaxis()
    
    # Add value labels
    for i, v in enumerate(top_features['Importance']):
        ax.text(v, i, f' {v:.3f}', va='center')
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Show feature importance table
    with st.expander("📊 Lihat Semua Feature Importance"):
        st.dataframe(feature_importance, use_container_width=True)
    
    st.write("---")
    st.info("""
    **Langkah Selanjutnya:**
    - Lanjut ke menu **📊 Visualizations** untuk eksplorasi data lebih lanjut
    - Model sudah tersimpan dan siap digunakan
    """)

# Show existing model if available
elif 'model_trained' in st.session_state and st.session_state['model_trained']:
    st.success("✅ Model sudah di-training sebelumnya!")
    
    st.write("---")
    st.subheader("📊 Hasil Training Sebelumnya")
    
    # Show metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Training Accuracy", f"{st.session_state['train_accuracy']*100:.2f}%")
    with col2:
        st.metric("Test Accuracy", f"{st.session_state['test_accuracy']*100:.2f}%")
    with col3:
        report = st.session_state['classification_report']
        st.metric("Precision", f"{report['weighted avg']['precision']*100:.2f}%")
    with col4:
        st.metric("Recall", f"{report['weighted avg']['recall']*100:.2f}%")
    
    # Show confusion matrix
    st.subheader("🔲 Confusion Matrix")
    cm = st.session_state['confusion_matrix']
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['No Depression', 'Depression'],
                yticklabels=['No Depression', 'Depression'])
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.set_title('Confusion Matrix')
    st.pyplot(fig)
    
    # Show feature importance
    st.subheader("⭐ Feature Importance (Top 10)")
    feature_importance = st.session_state['feature_importance']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    top_features = feature_importance.head(10)
    
    ax.barh(range(10), top_features['Importance'])
    ax.set_yticks(range(10))
    ax.set_yticklabels(top_features['Feature'])
    ax.set_xlabel('Importance')
    ax.set_title('Top 10 Most Important Features')
    ax.invert_yaxis()
    
    plt.tight_layout()
    st.pyplot(fig)
    
    if st.button("🔄 Train Ulang Model"):
        st.session_state['model_trained'] = False
        st.rerun()
