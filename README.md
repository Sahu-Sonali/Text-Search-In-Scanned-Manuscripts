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
                   ┌───────────────────────────┐
                   │       User Uploads        │
                   │    (PDF / Image File)     │
                   └─────────────┬─────────────┘
                                 │
                                 ▼
                   ┌───────────────────────────┐
                   │   File Identification     │
                   │ (Image or PDF Detection)  │
                   └─────────────┬─────────────┘
                                 │
     ┌───────────────────────────┼───────────────────────────┐
     ▼                           ▼                           ▼
┌───────────┐            ┌───────────────┐         ┌──────────────────┐
│ Image      │            │ Extract PDF   │         │ Extract Images   │
│ Preprocess │            │ Text (Fitz)   │         │ from PDF Pages   │
└─────┬──────┘            └──────┬────────┘         └──────────┬───────┘
      │                           │                             │
      ▼                           ▼                             ▼
┌─────────────┐         ┌─────────────────────┐        ┌──────────────────┐
│ OCR Text    │         │ Combine All Extracted│        │ Preprocess Image │
│ (Tesseract) │         │ Text (PDF + Images)  │        └───────┬─────────┘
└──────┬──────┘         └─────────────────────┘                │
       │                                                       ▼
       ▼                                             ┌──────────────────┐
┌──────────────┐                                     │ OCR on Extracted │
│ Final Raw     │                                     │ PDF Images      │
│ Text Output   │                                     └───────┬─────────┘
└───────┬────────┘                                             │
        ▼                                                       ▼
                   ┌───────────────────────────┐
                   │  NLP Processing Module    │
                   │  - Summarization (LSA)    │
                   │  - Word Frequency         │
                   │  - Search Keyword         │
                   └─────────────┬─────────────┘
                                 ▼
                   ┌───────────────────────────┐
                   │ Streamlit Visualization   │
                   │  ● Text Output            │
                   │  ● Images                 │
                   │  ● Summary                │
                   │  ● Charts                 │
                   │  ● Search Result          │
                   └───────────────────────────┘



