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


         
+---------------------------------------------+
|                 User Input                  |
|     (Upload Image or PDF Document)          |
+-------------------------+-------------------+
                          |
                          v
+---------------------------------------------+
|            File Type Identification          |
|   (Check if file is Image or PDF format)     |
+-------------------------+-------------------+
                          |
          +---------------+---------------+
          |                               |
          v                               v
+-----------------------------+   +-----------------------------+
|      Image Processing       |   |        PDF Processing       |
|  - OpenCV Preprocessing     |   |  - Extract Text (PyMuPDF)   |
|  - Noise Removal            |   |  - Extract Embedded Images  |
|  - Thresholding             |   |  - Convert PDF Pages to Img |
+-------------+---------------+   +---------------+-------------+
              |                                   |
              v                                   v
+-----------------------------+   +-----------------------------+
|         OCR Module          |   |       OCR on PDF Images     |
|      (Tesseract OCR)        |   |       (Tesseract OCR)       |
+-------------+---------------+   +---------------+-------------+
              |                                   |
              +---------------+-------------------+
                              |
                              v
+-------------------------------------------------------------+
|                     NLP Processing Module                   |
|  - Text Cleaning                                            |
|  - Text Summarization (LSA)                                 |
|  - Keyword Extraction                                       |
|  - Search Within Document                                   |
+-----------------------------+-------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                   Streamlit User Interface                   |
|  - Display Extracted Text                                    |
|  - Display Images                                            |
|  - Display Summary                                           |
|  - Word Frequency Charts                                     |
|  - Search Results                                            |
+-------------------------------------------------------------+

                   
---


