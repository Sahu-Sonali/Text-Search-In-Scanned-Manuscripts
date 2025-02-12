from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

# Initialize the Flask app
app = Flask(__name__)

# Function to process an image and extract text
def extract_text(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    return text

# API endpoint to handle image uploads and search queries
@app.route('/api/search', methods=['POST'])
def search_text_api():
    # Get the file and search query from the request
    file = request.files.get('file')
    query = request.form.get('query')

    if not file or not query:
        return jsonify({"error": "File and query are required"}), 400

    # Extract text from the uploaded file
    extracted_text = extract_text(file.read())
    # Find lines containing the search query
    results = [line for line in extracted_text.splitlines() if query.lower() in line.lower()]

    return jsonify({"results": results})

# Run the API server
if __name__ == '__main__':
    app.run(port=5000)