# 📜 Text Search in Scanned Manuscripts

Text Search in Scanned Manuscripts is a Python-based application that enables users to extract and search text from scanned images of historical or handwritten documents. Using Tesseract OCR for text recognition, OpenCV for image preprocessing, and NLP libraries like NLTK or spaCy for text analysis, the tool provides an interactive Streamlit interface for uploading images, extracting text, and performing keyword-based searches. It's ideal for researchers, archivists, and digital humanities projects.

This project provides a streamlined pipeline to **extract, preprocess, and search text** in scanned manuscript images and pdf using OCR and NLP techniques.

## 🔍 Features

- 🧠 Optical Character Recognition (OCR) using [Tesseract](https://github.com/tesseract-ocr/tesseract)
- 🧼 Image preprocessing with OpenCV (thresholding, denoising, etc.)
- 🗂️ Text cleaning and tokenization with NLTK or spaCy
- 🔎 Keyword search and snippet retrieval
- 🖼️ Streamlit interface for easy image uploads and querying

---

              Project Architecture Diagram (Text Format)
```mermaid
flowchart TD

A[User Uploads<br/>(PDF / Image)] --> B[File Identification<br/>(Image or PDF)]

B --> C1[Image Preprocessing<br/>(OpenCV)]
B --> C2[Extract PDF Text<br/>(PyMuPDF)]
B --> C3[Extract Images from PDF]

C1 --> D1[OCR Text (Tesseract)]
C3 --> C4[Preprocess Extracted Images]
C4 --> D2[OCR Text (Tesseract)]
C2 --> D3[Raw PDF Text]

D1 --> E[Combine All Extracted Text]
D2 --> E
D3 --> E

E --> F[NLP Processing Module<br/>- LSA Summary<br/>- Word Frequency<br/>- Keyword Search]

F --> G[Streamlit Visualization<br/>Text • Images • Summary • Charts • Search Results]

---


                   



