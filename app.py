import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import numpy as np
import cv2
import os
import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.tokenizers import Tokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import matplotlib.pyplot as plt
import nltk
import io

# Ensure necessary downloads
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_image(image):
    image_array = np.array(image)
    
    # Ensure image has at least 3 channels before converting
    if len(image_array.shape) == 2:  # If already grayscale, use it directly
        gray = image_array
    elif len(image_array.shape) == 3 and image_array.shape[2] == 4:  # RGBA -> RGB
        image_array = cv2.cvtColor(image_array, cv2.COLOR_RGBA2RGB)
        gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    elif len(image_array.shape) == 3 and image_array.shape[2] == 3:  # RGB -> Grayscale
        gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    else:
        raise ValueError("Unsupported image format")

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    kernel = np.ones((2, 2), np.uint8)
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    
    return opened

def extract_text_from_image(image):
    tesseract_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=tesseract_config)
    return text.strip()

def extract_text_from_pdf(pdf_file):
    text = ""
    images = []
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text += page.get_text("text") + "\n"
        images.extend(page.get_images(full=True))
    
    extracted_images = []
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_data = base_image["image"]
        image = Image.open(io.BytesIO(image_data))
        extracted_images.append(image)
    
    return text.strip(), extracted_images

def extractive_summary_sumy(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    num_sentences = min(3, len(sent_tokenize(text)))
    summary = summarizer(parser.document, num_sentences)
    summary_text = "\n".join(str(sentence) for sentence in summary)
    return summary_text

def text_analysis(text):
    total_characters = len(text)
    words = word_tokenize(text)
    total_words = len(words)
    sentences = sent_tokenize(text)
    total_sentences = len(sentences)
    avg_words_per_sentence = total_words / total_sentences if total_sentences else 0
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    word_counts = Counter(filtered_words)
    
    st.write("### Text Analysis Report")
    st.write(f"*Total Characters:* {total_characters}")
    st.write(f"*Total Words:* {total_words}")
    st.write(f"*Total Sentences:* {total_sentences}")
    st.write(f"*Average Words per Sentence:* {avg_words_per_sentence:.2f}")
    
    st.write("### Top 10 Most Common Words")
    common_words = word_counts.most_common(10)
    for word, count in common_words:
        st.write(f"{word}: {count}")
    
    if word_counts:
        words, counts = zip(*common_words)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(words, counts, color='skyblue')
        ax.set_xlabel('Words')
        ax.set_ylabel('Frequency')
        ax.set_title('Top 10 Most Common Words')
        ax.set_xticks(range(len(words)))
        ax.set_xticklabels(words, rotation=45)
        st.pyplot(fig)

def search_word(text, keyword):
    occurrences = text.lower().count(keyword.lower())
    sentences_with_keyword = [sentence for sentence in sent_tokenize(text) if keyword.lower() in sentence.lower()]
    
    st.write(f"### Search Results for '{keyword}'")
    st.write(f"Total occurrences: {occurrences}")
    if sentences_with_keyword:
        st.write("### Sentences Containing the Word:")
        for sentence in sentences_with_keyword:
            st.write(f"- {sentence}")

def main():
    st.set_page_config(page_title="Text Search in Scanned Manuscripts", layout="wide")
    st.title("Text Search in Scanned Manuscript")
    
    uploaded_file = st.file_uploader("Upload a PDF or Image", type=['png', 'jpg', 'jpeg', 'pdf'])
    
    if uploaded_file:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        
        if file_extension in ['png', 'jpg', 'jpeg']:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            with st.spinner("Processing the image..."):
                preprocessed_image = preprocess_image(image)
                extracted_text = extract_text_from_image(preprocessed_image)
                st.write("### Extracted Text")
                st.write(extracted_text)
                
                summary_text = extractive_summary_sumy(extracted_text)
                st.write("### Extractive Summary")
                st.text(summary_text)
                
                text_analysis(extracted_text)
        
        elif file_extension == 'pdf':
            with st.spinner("Processing the PDF..."):
                extracted_text, extracted_images = extract_text_from_pdf(uploaded_file)
                st.write("### Extracted Text from PDF")
                st.write(extracted_text)
                
                summary_text = extractive_summary_sumy(extracted_text)
                st.write("### Extractive Summary")
                st.text(summary_text)
                
                text_analysis(extracted_text)
                
                if extracted_images:
                    st.write("### Extracted Images from PDF")
                    for img in extracted_images:
                        st.image(img, caption="Extracted Image", use_column_width=True)
                        
                        with st.spinner("Performing OCR on Extracted Image..."):
                            preprocessed_img = preprocess_image(img)
                            extracted_img_text = extract_text_from_image(preprocessed_img)
                            st.write("#### Text from Extracted Image")
                            st.write(extracted_img_text)
        
        search_query = st.text_input("Enter a word to search in the extracted text:")
        if search_query:
            search_word(extracted_text, search_query)
        
if __name__ == "__main__":
    main()