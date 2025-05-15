# app.py
from flask import Flask, request, render_template, url_for
import os
import cv2
import numpy as np
from PIL import Image
import random
import string
import pytesseract

app = Flask(__name__)

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to home page
@app.route("/", methods=["GET", "POST"])
def index():
    # Execute if request is GET
    if request.method == "GET":
        return render_template("index.html", full_filename=None, error=None)

    # Execute if request is POST
    if request.method == "POST":
        # Check if file is uploaded
        if 'image_upload' not in request.files:
            return render_template("index.html", full_filename=None, error="No file uploaded.", text=None)
        
        image_upload = request.files['image_upload']
        
        # Check if a file was selected
        if image_upload.filename == '':
            return render_template("index.html", full_filename=None, error="No file selected.", text=None)
        
        # Validate file extension
        if not allowed_file(image_upload.filename):
            return render_template("index.html", full_filename=None, error="Invalid file type. Allowed: PNG, JPG, JPEG, WEBP.", text=None)

        # Get the original file extension
        file_ext = image_upload.filename.rsplit('.', 1)[1].lower()
        image = Image.open(image_upload)

        # Converting image to array
        image_arr = np.array(image.convert('RGB'))
        # Converting image to grayscale
        gray_img_arr = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)
        # Converting image back to grayscale for OCR
        image = Image.fromarray(gray_img_arr)

        # Generating unique image name with original extension
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(10)) + f'.{file_ext}'
        full_filename = name  # Just the filename, as it's saved in static/

        # Extracting text from image
        custom_config = r'-l eng --oem 3 --psm 6'
        text = pytesseract.image_to_string(image, config=custom_config)

        # Remove unwanted characters
        characters_to_remove = "!()@—*“>+-/,'|£#%$&^_~"
        new_string = text
        for character in characters_to_remove:
            new_string = new_string.replace(character, "")

        # Converting string into list for display
        new_string = new_string.split("\n")

        # Saving image to static/ with original format
        img = Image.fromarray(image_arr, 'RGB')
        img.save(os.path.join('static', name))

        # Returning template, filename, extracted text
        return render_template('index.html', full_filename=full_filename, text=new_string, error=None)

# Main function
if __name__ == '__main__':
    app.run(debug=True)