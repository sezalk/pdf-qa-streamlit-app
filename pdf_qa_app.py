import streamlit as st
from transformers import pipeline
import PyPDF2
import tempfile
import os


def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as f:
        reader = PyPDF2.PdfFileReader(f)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text


def save_uploaded_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        return tmp_file.name


def answer_questions(text, question):
    qa_pipeline = pipeline("question-answering")
    result = qa_pipeline(question=question, context=text)
    return result["answer"]


def main():
    st.title("PDF Question Answering App")

    
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        
        pdf_path = save_uploaded_file(uploaded_file)

        
        with open(pdf_path, "rb") as f:
            pdf_content = f.read()
        st.write("PDF content:")
        st.write(pdf_content)

        
        text = extract_text_from_pdf(pdf_path)

        
        st.write("Extracted text:")
        st.write(text)

        
        question = st.text_input("Ask a question:")
        if st.button("Get Answer"):
            if question.strip() == "":
                st.warning("Please enter a question.")
            else:
                
                answer = answer_questions(text, question)
                st.write("Answer:", answer)

        
        os.unlink(pdf_path)

if __name__ == "__main__":
    main()
