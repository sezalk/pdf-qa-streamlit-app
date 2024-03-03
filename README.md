# PDF Question Answering App

This is a simple Streamlit web application that allows users to upload a PDF file and ask questions related to its content. The app uses the `PyPDF2` library to extract text from the uploaded PDF file and the `transformers` library to answer questions based on the extracted text.

## Getting Started

To run this Streamlit app on your local machine, follow these steps:

1. **Install Python**: Make sure you have Python installed on your computer. You can download Python from the [official Python website](https://www.python.org/downloads/).

2. **Install Required Libraries**: Open a terminal or command prompt and install the required libraries using pip:

   ```bash
   pip install streamlit transformers PyPDF2
   ```

3. **Run the Application**: Open a terminal or command prompt, navigate to the directory where you saved `pdf_qa_app.py`, and run the following command:

   ```bash
   streamlit run pdf_qa_app.py
   ```

4. **Access the App**: After running the command, Streamlit will start a local server, and it will provide a URL (usually starting with `http://localhost`). Open a web browser and go to that URL to access the PDF Question Answering app.

## Usage

Once you access the app in your web browser, follow these steps:

1. **Upload PDF File**: Click on the "Upload a PDF file" button and select a PDF file from your computer.

2. **View PDF Content**: The app will display the content of the uploaded PDF file.

3. **Ask Questions**: Type your question in the text input field provided.

4. **Get Answer**: Click on the "Get Answer" button to get the answer to your question based on the content of the PDF file.
