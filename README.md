# DocuMind AI

DocuMind AI is a document assistant that helps users work with different types of documents using AI.

I built this project to make it easier to understand documents instead of manually reading everything from beginning to end.

## What can it do?

You can upload documents such as PDF, DOCX, TXT files, and images.

The application can:

- answer questions about an uploaded document
- generate a summary
- identify the type of document
- analyze resumes
- explain medical reports in simple language
- analyze books and study notes
- generate quizzes and flashcards from notes
- explain government documents
- help understand forms
- extract important actions, dates, and deadlines
- translate documents
- compare documents

It also supports OCR for images and scanned PDFs.

## Technologies Used

- Python
- Streamlit
- Groq API
- LangChain
- Hugging Face Embeddings
- PyMuPDF
- python-docx
- Tesseract OCR

## How to run the project

Clone the repository:

```bash
git clone https://github.com/deepikamau9794-blip/DocuMindAI.git
cd DocuMindAI
```

Create a virtual environment using Python 3.11:

```bash
py -3.11 -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project folder and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

## Note

The AI responses are generated based on the uploaded document.

Medical report analysis is only for general understanding and should not be considered medical advice.

Government document analysis is only for general understanding and should not be considered legal advice.

## Author

Deepika Kushwaha