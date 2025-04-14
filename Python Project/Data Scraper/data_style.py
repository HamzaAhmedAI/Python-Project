import streamlit as st
import pandas as pd
import os
from io import BytesIO  # Corrected import

st.set_page_config(page_title='Data Sweeper Pro', layout="wide", page_icon="🧹")

# ==================== CUSTOM STYLING ====================
st.markdown("""
    <style>
    /* Main page styling */
    .main {
        background: #0f172a;
        color: #f8fafc;
        max-width: 1200px;
    }
    
    /* Modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Gradient header */
    .gradient-header {
        background: linear-gradient(45deg, #6366f1, #a855f7);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        margin: 1rem 0;
    }
    
    /* Enhanced file uploader */
    .stFileUploader>div {
        border: 2px dashed #334155 !important;
        border-radius: 15px;
        background: #1e293b !important;
    }
    
    /* Modern buttons */
    .stButton>button {
        background: #6366f1;
        color: white !important;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: #4f46e5 !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 6px rgba(99, 102, 241, 0.2);
    }
    
    /* Dataframe styling */
    .dataframe {
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Success message */
    .success-box {
        padding: 1rem;
        background: #1e293b;
        border-left: 4px solid #10b981;
        border-radius: 6px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== APP CONFIGURATION ====================

st.markdown('<h1 class="gradient-header">Data Sweeper Pro</h1>', unsafe_allow_html=True)
st.caption("Transform your files between CSV/Excel formats with built-in data cleaning and visualization")

# ==================== FILE UPLOAD ====================
uploaded_files = st.file_uploader(
    "📤 Upload your files (CSV or Excel)",
    type=['csv', 'xlsx'],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        with st.expander(f"**Processing:** {file.name}", expanded=True):
            try:
                file_ext = os.path.splitext(file.name)[-1].lower()
                
                # ==================== FILE LOADING ====================
                if file_ext == ".csv":
                    df = pd.read_csv(file)
                elif file_ext == ".xlsx":
                    df = pd.read_excel(file, engine='openpyxl')
                
                # ==================== FILE INFO SECTION ====================
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("File Size", f"{(file.size/1024):.2f} KB")
                with col2:
                    st.metric("Rows × Columns", f"{df.shape[0]} × {df.shape[1]}")
                
                # ==================== DATA PREVIEW ====================
                st.subheader("🔍 Data Preview")
                st.dataframe(df.head().style
                                .set_properties(**{
                                    'background-color': '#1e293b',
                                    'color': '#f8fafc',
                                    'border': '1px solid #334155'
                                })
                                .set_table_styles([{
                                     'selector': 'tr:nth-of-type(odd)',
                                     'props': [('background-color', '#2d3748')]
                                 }]))
                
                # ==================== DATA CLEANING ====================
                st.subheader("🧹 Cleaning Options")
                cleaning_col1, cleaning_col2 = st.columns(2)
                
                with cleaning_col1:
                    if st.button(f"Remove Duplicates", key=f"dup_{file.name}"):
                        initial_rows = df.shape[0]
                        df = df.drop_duplicates()
                        new_rows = df.shape[0]
                        st.success(f"Removed {initial_rows - new_rows} duplicates!")
                        
                with cleaning_col2:
                    if st.button(f"Fill Missing Values", key=f"na_{file.name}"):
                        numeric_cols = df.select_dtypes(include=['number']).columns
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                        st.success("Missing values filled with column means!")
                
                # ==================== COLUMN SELECTION ====================
                st.subheader("🎯 Column Selection")
                selected_columns = st.multiselect(
                    "Choose columns to keep:",
                    options=df.columns,
                    default=df.columns,
                    key=f"cols_{file.name}"
                )
                df = df[selected_columns]


                # ==================== DATA VISUALIZATION ====================
                st.subheader("📊 Data Visualization")
                if st.checkbox(f"Show Visualization for {file.name}"):
                    st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])
                    
                
                # ==================== FILE CONVERSION ====================
                st.subheader("🔄 Conversion Options")
                conversion_type = st.radio(
                    f"Convert {file.name} to:",
                    ["CSV", "Excel"],
                    horizontal=True,
                    key=f"conv_{file.name}"
                )
                
                buffer = BytesIO()
                if st.button(f"Convert {file.name}", key=f"btn_{file.name}"):
                    with st.spinner(f"Converting {file.name}..."):
                        if conversion_type == "CSV":
                            df.to_csv(buffer, index=False)
                            file_name = file.name.replace(file_ext, ".csv")
                            mime_type = "text/csv"
                        else:
                            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                                df.to_excel(writer, index=False)
                            file_name = file.name.replace(file_ext, ".xlsx")
                            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        
                        buffer.seek(0)
                        st.download_button(
                            label=f"📥 Download {conversion_type}",
                            data=buffer,
                            file_name=file_name,
                            mime=mime_type,
                            key=f"dl_{file.name}"
                        )
                        st.balloons()
                        
            except Exception as e:
                st.error(f"Error processing {file.name}: {str(e)}")

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #64748b; padding: 2rem 0;">
        🚀 Powered by Streamlit | Made with ❤️ by Hamza Ahmed
    </div>
""", unsafe_allow_html=True)