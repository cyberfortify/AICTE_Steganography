# **Secure Data hiding in image using Steganography**

🔒 **A Python-based GUI application that allows users to securely hide and retrieve text inside images using Steganography.**  

## 🚀 **Project Overview**
Steganography is the art of hiding information inside digital media in a way that makes it undetectable. This project implements **Least Significant Bit (LSB) Steganography**, allowing users to **embed** secret text inside an image and later **extract** it without altering the image’s appearance.

## 📌 **Features**
✅ **Supports Multiple Image Formats** – PNG, JPG, BMP, and TIFF  
✅ **Secure Steganography** – Text is hidden inside pixel data without visible distortion  
✅ **User-Friendly GUI** – Simple buttons for hiding & extracting text  
✅ **Fast & Efficient** – Quick encoding/decoding without performance lag  
✅ **Cross-Platform Compatibility** – Works on Windows, macOS, and Linux  

## 🛠️ **Technologies Used**
- **Python** – Core programming language  
- **Tkinter** – GUI for user interaction  
- **Pillow (PIL)** – Image processing  
- **NumPy** – Pixel data manipulation  

## 🎯 **How to Run the Project**
### **🔹 Step 1: Clone the Repository**
```sh
git clone https://github.com/cyberfortify/AICTE_Steganography.git
cd AICTE_Steganography
```

### **🔹 Step 2: Install Dependencies**
Make sure you have Python installed. Then, install required libraries:
```sh
pip install pillow numpy
```

### **🔹 Step 3: Run the Application**
- To **hide text in an image**, run:
  ```sh
  python hideText.py
  ```
- To **extract text from an image**, run:
  ```sh
  python unhideText.py
  ```
  
## 🎯 **How It Works**
1. **Hiding Text Process**  
   - The selected image is loaded into a NumPy array.  
   - The text message is converted to **binary** and embedded into the least significant bits (LSB) of pixel values.  
   - A delimiter (`###`) is added at the end of the message to indicate stopping point.  
   - The modified image is saved as a new stego-image.

2. **Extracting Text Process**  
   - The application reads the image pixel data.  
   - Extracts the **least significant bits** of each pixel to reconstruct the hidden binary text.  
   - Converts the binary data back into readable text.  
   - Stops reading at the predefined delimiter (`###`).  

## 🎯 **End Users**
👨‍💻 **Cybersecurity Experts** – Secure communication  
🕵️ **Investigative Journalists** – Hiding sensitive data  
🔐 **Government & Defense Agencies** – Classified data transmission  
📚 **Academics & Researchers** – Studying Steganography techniques  

## 🚀 **Future Scope**
🔮 **AES-Encrypted Steganography** – Encrypt text before hiding  
📱 **Mobile App Version** – Implement for Android/iOS  
🌐 **Web-Based Secure Communication** – Steganography over the cloud  
🖼️ **Hiding Data in Videos & Audio** – Expand beyond images  

## 📜 **License**
This project is **open-source** under the **MIT License**.

## 🔗 **GitHub Repository**
📌 [AICTE Steganography GitHub Repo](https://github.com/cyberfortify/AICTE_Steganography)  
