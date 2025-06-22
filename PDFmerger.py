import streamlit as st
import PyPDF2
import io

st.set_page_config(page_title="PDF Merger", page_icon="📎", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .title {
            font-size: 42px;
            color: rgb(169,0,217);
            text-align: center;
            margin-bottom: 0.5em;
        }
        .subtitle {
            font-size: 18px;
            text-align: center;
            color: #666;
            margin-bottom: 2em;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border: None;
            border-radius: 5px;
            padding: 10px 20px;
            margin-top: 10px;
        }
        .stDownloadButton>button {
            background-color: #2196F3;
            color: white;
            font-weight: bold;
            border: None;
            border-radius: 5px;
            padding: 10px 20px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title"> PDF Merger Tool</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Merge your PDFs directly in memory — fast, clean, and secure!</div>', unsafe_allow_html=True)

uploaded_files = st.file_uploader("📄 Upload PDF files", type="pdf", accept_multiple_files=True)

merged_name = st.text_input("✏️ Enter name for merged PDF (without .pdf)")

if st.button("🔗 Merge PDFs"):
    if uploaded_files and merged_name:
        merger = PyPDF2.PdfMerger()

        for file in uploaded_files:
            merger.append(file)

        merged_pdf = io.BytesIO()
        merger.write(merged_pdf)
        merger.close()
        merged_pdf.seek(0)

        st.success(f"🎉 PDF merged successfully! Ready to download.")

        st.download_button(
            label="⬇️ Download Merged PDF",
            data=merged_pdf,
            file_name=f"{merged_name}.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("⚠️ Please upload at least one PDF and enter a filename.")
