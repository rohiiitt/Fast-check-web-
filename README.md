# Fact Check Agent

An AI-powered Fact Checking Web Application that extracts claims from PDF documents and evaluates their credibility using NLP and verification techniques.

## Features

* Upload PDF documents
* Extract factual claims automatically
* NLP-based claim detection
* Confidence scoring
* Fact classification
* Interactive Streamlit dashboard
* Duplicate claim filtering
* JSON result generation

---

## Tech Stack

* Python
* Streamlit
* spaCy
* Regex
* PDF Processing
* JSON
* Git & GitHub

---

## Project Structure

```text
fact-check-agent/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── utils/
│   ├── pdf_reader.py
│   ├── claim_extractor.py
│   ├── verifier.py
│   └── report.py
│
└── uploads/
```

---

## Installation

Clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
cd fact-check-agent
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download spaCy model:

```bash
python -m spacy download en_core_web_sm
```

---

## Run Locally

Start the application:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Usage

1. Open the application
2. Upload a PDF
3. Extract claims
4. Verify results
5. View confidence scores

---

## Environment Variables

Create `.env`

```env
OPENAI_API_KEY=YOUR_API_KEY
```

Do not commit `.env`.

---

## Deployment

Push code to GitHub:

```bash
git add .
git commit -m "deploy"
git push origin main
```

Deploy using Streamlit Community Cloud.

---

## Future Improvements

* Real-time web verification
* Multi-language support
* OCR support
* Improved confidence ranking
* Dashboard analytics

---

## Author

Rohit Kumar

---

## License

This project is for educational and research purposes.
