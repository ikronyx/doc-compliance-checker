
import streamlit as st
from file_parser import extract_text
from gpt_checker import check_compliance
from utils import load_checklist, results_to_dataframe

st.set_page_config(page_title="Document Compliance Checker", layout="wide")
st.title("📄 AI-Powered Document Compliance Checker")

uploaded_file = st.file_uploader("Upload your document", type=["pdf", "docx", "xlsx", "eml", "msg"])
checklist_file = st.file_uploader("Upload checklist JSON", type=["json"])

if uploaded_file and checklist_file:
    with st.spinner("Extracting text..."):
        doc_text = extract_text(uploaded_file)

    with st.spinner("Loading checklist..."):
        checklist = load_checklist(checklist_file)

    if st.button("Run Compliance Check"):
        with st.spinner("Analyzing with GPT-4..."):
            results = check_compliance(doc_text, checklist)
            df = results_to_dataframe(results)
            st.success("Analysis complete!")
            st.dataframe(df)

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇ Download CSV", csv, "results.csv", "text/csv")
