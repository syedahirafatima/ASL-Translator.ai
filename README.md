# American Sign Language Alphabet Recognizer
✔️ A Python project that recognizes the American Sign Language (ASL) alphabet using a Convolutional Neural Network (CNN) and OpenCV. <br>
✔️ This project can translate hand signs into both **text** and **voice** in real-time.


## 💡 Why I Built This Project
1. **Promote Accessibility:** Help bridge communication gaps for deaf and mute individuals ♿ 
2. **Enhance Human Connection:** Translate ASL into text and voice for smoother interaction.  
3. **Hands-On AI Learning:** Apply Python, OpenCV, and CNNs to a real-world problem 💻
4. **Real-Time Recognition:** Detect ASL alphabets live using webcam input 🎥 
5. **Text & Voice Output:** Make recognition practical with readable and spoken results.  
6. **Open-Source Contribution:** Provide a project others can learn from.
7. **Neural Network Experimentation:** Explore model accuracy and preprocessing techniques 🧠
8. **Technology Serving Humanity:** Use AI to create meaningful impact in people’s lives ❤️

## How to Run the Project

This project uses **Python**, **OpenCV**, and a **pre-trained CNN model** to recognize ASL alphabets from images or webcam input.

### 1. 1️⃣ Clone the Repository
```bash
git clone https://github.com/syedahirafatima/ASL-Translator.ai
cd ASL-Translator.ai
```

### 2. 2️⃣ Install Dependencies

Make sure you have Python installed (preferably Python 3.8+). All teh dependencies needed are in the `requirements.txt`, so install the required packages using pip:
```bash
pip install -r requirements.txt
```

### 3. 3️⃣ Run the Translator

To start recognizing ASL alphabets in real-time via webcam, run:
```bash
python translator.py
```

## Project Structure
1. `ASL.ipynb` – Jupyter notebook for experimenting with the model.<br>
2. `predict.py` – Contains functions to preprocess images and predict ASL alphabets.<br>
3. `translator.py` – Main script to translate webcam input into text and voice.<br>
4. `variables.py` – Stores project paths and configuration variables.<br>
5. `model.h5` – Pre-trained CNN model for ASL recognition.<br>
6. `dataset/` – Folder containing the ASL dataset (if needed for training or testing).<br>
7. `alphabet.png` – Reference image of the ASL alphabet.<br>
8. `requirements.txt` - contains all the dependencies<br>

   
## 📌 Requirements:
* Keras
* matplotlib
v numpy
* opencv-python
* pypiwin32
* pyttsx3
* pywin32
* PyYAML
* scipy
* six
* tensorflow

All the requirements can be installed from `requirements.txt` file


## 📌 License:
ASL-Translator.ai License - Testing Only

⚠️ Permission is hereby granted to clone, run, and test this project locally for personal use.  
⚠️ You may not modify, distribute, copy, or deploy this project publicly.  
⚠️ All rights reserved by the author.
