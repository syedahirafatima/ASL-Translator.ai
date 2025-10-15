# American Sign Language Alphabet Recognizer
✔️ A Python project that recognizes the American Sign Language (ASL) alphabet using a Convolutional Neural Network (CNN) and OpenCV. <br>
✔️ This project can translate hand signs into both **text** and **voice** in real-time.

# Real-Time ASL Alphabet Recognition (Demo Screenshots)
Below are demo screenshots showing how the ASL Translator detects and predicts American Sign Language alphabets in real time.<br>
Here, it recognizes the sequence H-E-L-L-O 👋 demonstrating accurate detection for multiple letters.
<p align="center">
  <img src="https://github.com/user-attachments/assets/5522dd57-22b6-4c06-b4f5-bcf87a8a9be1" alt="H" width="300"/>
  <img src="https://github.com/user-attachments/assets/54cdd6e5-850f-4679-8f3f-9939d35a75f7" alt="E" width="300"/><br>
  <img src="https://github.com/user-attachments/assets/9d660d72-c491-431a-9add-b17a93a2def5" alt="L" width="300"/>
  <img src="https://github.com/user-attachments/assets/53712e7a-b043-4fbb-80ba-60d1db8a8148" alt="L" width="300"/><br>
  <img src="https://github.com/user-attachments/assets/8aec64fc-f458-447d-a66f-8d5af0f71862" alt="O" width="300"/><br>
</p>

# Trained ASL Alphabets Overview
The ASL Translator model has been trained on A–Z American Sign Language alphabets. <br>
Each alphabet is represented by multiple hand gesture samples to help the model learn shape variations and improve accuracy. <br>

<p align="center"> <img src="https://github.com/user-attachments/assets/2ad8a7ad-391b-48c7-b066-12d05404099a" alt="Trained ASL Alphabets" width="400"/> </p>


## 💡 Why I Built This Project
1. **Promote Accessibility:** Help bridge communication gaps for deaf and mute individuals ♿ <br>
2. **Enhance Human Connection:** Translate ASL into text and voice for smoother interaction.  <br>
3. **Hands-On AI Learning:** Apply Python, OpenCV, and CNNs to a real-world problem 💻<br>
4. **Real-Time Recognition:** Detect ASL alphabets live using webcam input 🎥 <br>
5. **Text & Voice Output:** Make recognition practical with readable and spoken results.  <br>
6. **Open-Source Contribution:** Provide a project others can learn from.<br>
7. **Neural Network Experimentation:** Explore model accuracy and preprocessing techniques 🧠<br>
8. **Technology Serving Humanity:** Use AI to create meaningful impact in people’s lives ❤️<br>

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
6. `alphabet.png` – Reference image of the ASL alphabet.<br>
7. `requirements.txt` - contains all the dependencies<br>
8.  `README.md` - contains all the instructions<br>

   
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
