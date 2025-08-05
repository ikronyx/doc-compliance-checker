import pdfplumber
import docx
import pandas as pd
import extract_msg
import os

def extract_text(file):
    ext = os.path.splitext(file.name)[1].lower()

    if ext == ".pdf":
        with pdfplumber.open(file) as pdf:
            return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

    elif ext == ".docx":
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

    elif ext == ".xlsx":
        dfs = pd.read_excel(file, sheet_name=None)
        return "\n\n".join([df.to_string() for df in dfs.values()])

    elif ext == ".msg":
        msg = extract_msg.Message(file)
        return f"Subject: {msg.subject}\n\nBody:\n{msg.body}"

    else:
        return "Unsupported file type."
