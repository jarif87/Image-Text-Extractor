# TextFromImageFlask

A modern, user-friendly Flask web application that extracts text from images (PNG, JPG, JPEG, WEBP) using Tesseract OCR. Upload an image, and the app processes it to display the extracted text alongside the image in a beautifully designed interface powered by Bootstrap and custom CSS animations.


## Features
- **Multi-Format Support**: Upload images in PNG, JPG, JPEG, or WEBP formats.
- **Text Extraction**: Uses Tesseract OCR to extract English text from images.
- **Modern UI**: Responsive design with Bootstrap 5, custom animations, and a gradient background.
- **Error Handling**: Clear feedback for invalid file types or upload issues.
- **Loading Feedback**: Displays a spinner during image processing.
- **Responsive Layout**: Works seamlessly on desktop and mobile devices.

## Installation

### Prerequisites
- Python 3.8+
- Tesseract OCR installed on your system:
  - **Windows**: Download from [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) and set the path in `app.py` if needed:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```
  - **Linux**: `sudo apt-get install tesseract-ocr`
  - **Mac**: `brew install tesseract`

### Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/jarif87/TextFromImageFlask.git
   cd TextFromImageFlask


2. **Create a virtual environment (optional but recommended):**

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```
pip install flask opencv-python pillow numpy pytesseract
```

4. **Ensure directory structure:**

```
TextFromImageFlask/
├── app.py
├── static/
│   └── css/
│       └── style.css
└── templates/
    └── index.html
```

5. **Run the application:**

```
python app.py
```

# Usage
1. **Upload an Image:**
- Click the file input to select a PNG, JPG, JPEG, or WEBP image containing text.

- Click the "Upload" button.

2. **View Results:**
- The app displays the uploaded image on the left.

- Extracted text appears in a table on the right.

3. **Handle Errors:**
- If you upload an invalid file (e.g., PDF), a red alert will show the error.

4. **Example Output:**
- Input Image: A JPG with the text "Hello World!"

5. **Output:**
- Image displayed in a card.

- Text: Hello World! in a striped table.

# Technologies Used
- Flask: Web framework for routing and templating.

- OpenCV: Image processing (grayscale conversion).

- Pillow: Image handling for multiple formats.

- Tesseract OCR: Text extraction from images.

- Bootstrap 5: Responsive UI framework.

- Font Awesome: Icons for upload, errors, and placeholders.

- Custom CSS: Animations, gradient background, and styling with Poppins font.

