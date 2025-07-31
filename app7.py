import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import together
import os
import pdfplumber
from PIL import Image
import pytesseract
import pdfplumber

# Setting API key (better: store this in environment variables)
together.api_key = "tgp_v1_OtkB6oDYcGvbnScheGQXnuALP9bklewZ4SCm5iXrOJ4"

# App title
st.title(" AI-Powered Data Analyst Agent")
st.markdown("Upload a file and ask data-related questions. Let LLaMA help you analyze it!")

# File Upload
uploaded_file = st.file_uploader("Upload your data file (CSV, XLSX, PDF, TXT, JPG, PNG)", type=["csv", "xlsx", "pdf", "txt", "jpg", "png", "jpeg"])

# File Parsing
def parse_file(file):
    ext = file.name.split('.')[-1].lower()
    if ext == 'csv':
        return pd.read_csv(file)
    elif ext == 'xlsx':
        return pd.read_excel(file)
    elif ext == 'pdf':
        with pdfplumber.open(file) as pdf:
            return '\n'.join(page.extract_text() for page in pdf.pages)
    elif ext == 'txt':
        return file.read().decode("utf-8")
    elif ext in ['jpg', 'jpeg', 'png']:
        return pytesseract.image_to_string(Image.open(file))
    else:
        return None

# Ask LLaMA
def ask_llama(prompt, max_tokens=200):
    try:
        response = together.Complete.create(
            model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
            prompt=f"### Instruction:\n{prompt}\n\n### Response:",
            max_tokens=max_tokens,
            temperature=0.5,
            stop=["###", "\n\n"]
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f" Error: {e}"

# Display parsed data and insights
if uploaded_file is not None:
    data = parse_file(uploaded_file)

    if isinstance(data, pd.DataFrame):
        st.success("File successfully parsed as DataFrame!")
        st.write("### Preview of Data")
        st.dataframe(data.head())

        st.write("### Basic Summary")
        st.write(data.describe(include='all'))

        # Visualization options
        st.write("### Generate Visualization")
        col1, col2 = st.columns(2)
        with col1:
            x_col = st.selectbox("Select X-axis", data.columns)
        with col2:
            y_col = st.selectbox("Select Y-axis", data.columns)

        plot_type = st.selectbox("Select Plot Type", ["bar", "scatter", "hist"])

        if st.button("Generate Plot"):
            plt.figure(figsize=(10, 5))
            if plot_type == "bar":
                sns.barplot(data=data, x=x_col, y=y_col)
            elif plot_type == "scatter":
                sns.scatterplot(data=data, x=x_col, y=y_col)
            elif plot_type == "hist":
                data[x_col].hist()
            st.pyplot(plt)

        # LLaMA Question Input
        st.write("### Ask LLaMA a Question About Your Data")
        question = st.text_input("Enter your question:")
        if st.button("Ask AI"):
            with st.spinner("Thinking..."):
                output = ask_llama(question)
            st.write(" LLaMA says:")
            st.success(output)

    elif isinstance(data, str):
        st.write("### Extracted Text")
        st.text(data)

        # Allow question on unstructured text
        question = st.text_input("Ask something about the text:")
        if st.button("Ask AI"):
            output = ask_llama(f"Text:\n{data[:1000]}\n\nQuestion: {question}")
            st.success(output)

    else:
        st.error(" Unsupported or unreadable file.")